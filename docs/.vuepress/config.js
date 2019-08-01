module.exports = {
    title: 'MetaBase Image Guide',
    description: 'Just playing around',
    themeConfig: {

      //页眉
      nav: [
        { text: 'Home', link: '/' },
        { text: 'Guide', link: '/guide/' },
        { text: 'External', link: 'https://google.com' },
        {
          text: 'Languages',
          items: [
            { text: 'English', link: '/' },
            { text: '中文', link: '/zh/' }
          ]
        },
      ],

      //侧边栏导航
      sidebar: [
        {
          title: 'Getting Started',
          collapsable: false,
          children: [
            '/overview',
            '/stack-installation',
            '/stack-components',
            '/stack-accounts',
          ]
        },

        {
          title: 'Best Practices',
          collapsable: false,
          children: [
            '/solution-smtp',
            '/solution-https',
            '/solution-dns',
            '/solution-migration',
            '/solution-backup',
            '/solution-upgrade',
          ]
        },

        {
          title: 'Administrator',
          collapsable: false,
          children: [
            '/admin-services',
            '/admin-mysql',
            '/admin-linux',
          ]
        },

        {
          title: 'Configuration on Cloud',
          collapsable: false,
          children: [
            '/getimage',
            '/cloud-server',
          ]
        },

        {
          title: 'Other',
          collapsable: false,
          children: [
            '/faq',
            '/troubleshooting',
          ]
        },
        
      ],

      displayAllHeaders: false, // 默认值：false
      activeHeaderLinks: true, // 默认值：true

    }
  }