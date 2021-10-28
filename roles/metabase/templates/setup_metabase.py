import requests
import json
from uuid import UUID
import sys
import time
import subprocess
class Prefs:
    site_name: str
    site_locale: str
    allow_tracking: bool

    def __init__(self, site_name: str, site_locale: str, allow_tracking: bool) -> None:
        self.site_name = site_name
        self.site_locale = site_locale
        self.allow_tracking = allow_tracking
    def toJson(self):
        return dict(site_name=self.site_name,site_locale=self.site_locale,allow_tracking=self.allow_tracking)


class User:
    first_name: str
    last_name: str
    email: str
    password: str
    site_name: str

    def __init__(self, first_name: str, last_name: str, email: str, password: str, site_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.site_name = site_name
    def toJson(self):
        return dict(first_name=self.first_name,last_name=self.last_name,email=self.email,password=self.password,site_name=self.site_name)


class SetUp:
    token: UUID
    prefs: Prefs
    database: None
    user: User

    def __init__(self, token: UUID, prefs: Prefs, database: None, user: User) -> None:
        self.token = token
        self.prefs = prefs
        self.database = database
        self.user = user
    def toJson(self):
        return dict(token=self.token,prefs=self.prefs,database=self.database,user=self.user)
class SetUpEncoder(json.JSONEncoder):
    def default(self,obj):
        if hasattr(obj,"toJson"):
            return obj.toJson()
        else:
            return json.JSONEncoder.default(self,obj)

def get_setup_token(url:str,port:str)->str:
    base_url=url
    port=port
    token_api="/api/session/properties"
    get_token_api=base_url+":"+port+token_api
    data=requests.get(get_token_api)
    data_json=str(data.json()).replace("\'","\"").replace("True","true").replace("False","false").replace("None","null");
    data_load=json.loads(data_json)
    setup_token=str(data_load["setup-token"]);
    return setup_token

def register(url:str,port:str,token:str,site_name:str,site_locale:str,allow_tracking:bool,first_name:str,last_name:str,email:str,password:str)->int:
    base_url=url
    port=port
    setup_api="/api/setup"
    setup_url=base_url+":"+port+setup_api
    setup_data=SetUp(
        token=token,prefs=Prefs(
            site_name=site_name,
            site_locale=site_locale,
            allow_tracking=allow_tracking,
        ),database=None,user=User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            site_name=site_name
        )
        )
    header={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Content-Type":"application/json",
        "Cookie":"metabase.DEVICE=9d1cabd0-ed8b-43fa-9642-b9ff23c97485; metabase.SESSION=e80b657e-8bfa-40f2-87f1-088e96f66e88"
    }
    setup_response=requests.post(setup_url,data=json.dumps(setup_data.__dict__,cls=SetUpEncoder),headers=header)
    return setup_response.status_code

def parse_config_file():
    config_file=open("./config.json")
    return json.load(config_file)

def check_health(base_url:str,port:str):
    check_health_api="/api/health"
    check_health_url=base_url+":"+port+check_health_api;
    return requests.get(check_health_url).status_code
if __name__=="__main__":
    config=parse_config_file()
    while check_health(base_url=config["url"],port=config["port"])!=200:
        subprocess.Popen(["sleep","2"])
         time.sleep(2)
    setup_token=get_setup_token(config["url"],config["port"])
    status_code=0;
    while status_code!=200:
        status_code=register(
        url=config["url"],
        port=config["port"],
        token=setup_token,
        site_name=config["site_name"],
        site_locale=config["site_locale"],
        email=config["email"],
        allow_tracking=config["allow_tracking"],
        first_name=config["first_name"],
        last_name=config["last_name"],
        password=sys.argv[1],
        )
        subprocess.Popen(["sleep","2"])
        time.sleep(2)






