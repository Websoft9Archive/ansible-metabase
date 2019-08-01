module.exports = {

//针对不同项目，需要修改的参数有：base,title,description,repo以及nav,sidebar 文件夹下的导航js文件

base: '/docs/metabase/',
dest: '.vuepress/html',

//vuepress多语言，区别于主题多语言
locales: {
    '/': {
      lang: 'en-US', // 将会被设置为 <html> 的 lang 属性
      title: 'Metabase Image Guide',
      description: 'You can get the Installation of Image,Administrator,Configuration of the OwnCloud from this documentation.'
    },
    '/zh/': {
      lang: 'zh-CN',
      title: 'Metabase 镜像手册',
      description: 'You can get the Installation of Image,Administrator,Configuration of the OwnCloud from this documentation.'
    }
},

themeConfig: {
	 
	//Basic configuration
	displayAllHeaders: false, // 默认值：false
  activeHeaderLinks: true, // 默认值：true
  displayAllHeaders: false, // 默认值：false
  sidebar: 'auto', // 默认值：false

  //Github 
  repo: 'Websoft9/ansible-metabase',
  editLinks: true,
  docsDir: 'docs',
  docsBranch: 'master',

  //主题多语言
  locales: {
    '/': {
      label: 'English',
      selectText: 'Languages',
      editLinkText: 'Edit this page on GitHub',
      lastUpdated: 'Last Updated',
      serviceWorker: {
         updatePopup: {
         message: "New content is available.",
         buttonText: "Refresh"
          }
        },
  
    //top-menu
    nav: require('./nav/en'),
    //left-menu
    sidebar:require('./sidebar/en'),
  },  
  
  '/zh/': {
    label: '中文',
    selectText: '语言',
    editLinkText: '在Github上编辑',
    lastUpdated: 'Last Updated',
    serviceWorker: {
      updatePopup: {
        message: "此文档有可用的更新",
        buttonText: "刷新"
      }
    },
  
    //页眉
    nav: require('./nav/zh'),
    //侧边栏导航
    sidebar: require('./sidebar/zh'),
  
  },
  
},   
}
}