import sys
if __name__=="__main__":
    password_file=open("./password.txt","w")
    password_file.write(sys.argv[1])
