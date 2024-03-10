const routes = [
  {
    path: '/',
    component: () => import('../layouts/BaseSite.vue'),
    children: [
      {
        path: '',
        name: 'feed',
        meta: {
          requiresAuthentication: false,
          requiresNav: true
        },
        component: async () => import('../pages/FeedPage.vue')
      },
      {
        path: 'video/:id(vd_\\w+)',
        name: 'video_details',
        meta: {
          requiresAuthentication: false,
          requiresNav: true
        },
        component: async () => import('../pages/VideoPage.vue')
      },
      {
        path: 'playlists',
        name: 'playlists',
        meta: {
          requiresAuthentication: true,
          requiresNav: true
        },
        component: async () => import('../pages/FeedPage.vue')
      },
      {
        path: 'notifications',
        children: [
          {
            path: '',
            name: 'notifications',
            meta: {
              requiresAuthentication: true,
              requiresNav: true
            },
            component: async () => import('../pages/NotificationsPage.vue')
          },
          {
            path: 'messages',
            name: 'notifications_messages',
            meta: {
              requiresAuthentication: true,
              requiresNav: true
            },
            component: async () => import('../pages/NotificationsPage.vue')
          },
          {
            path: 'uploads',
            name: 'notifications_uploads',
            meta: {
              requiresAuthentication: true,
              requiresNav: true
            },
            component: async () => import('../pages/NotificationsPage.vue')
          }
        ]
        // name: 'notifications',
        // meta: { requiresAuthentication: false },
        // component: async () => import('../pages/NotificationsPage.vue')
      },
      {
        path: 'my-studio',
        name: 'my_studio',
        meta: {
          requiresAuthentication: true,
          requiresNav: true
        },
        component: async () => import('../pages/StudioPage.vue')
      },
      {
        path: 'settings',
        children: [
          {
            path: '',
            name: 'settings',
            meta: {
              requiresAuthentication: true,
              requiresNav: false,
              requiresSettingsNav: true
            },
            component: async () => import('../pages/SettingsPage.vue')
          },
          {
            path: 'algorithm',
            name: 'settings_algorithm',
            meta: {
              requiresAuthentication: true,
              requiresNav: false,
              requiresSettingsNav: true
            },
            component: async () => import('../pages/settings/AlgorithmPage.vue')
          },
          {
            path: 'notifications',
            name: 'settings_notifications',
            meta: {
              requiresAuthentication: true,
              requiresNav: false,
              requiresSettingsNav: true
            },
            component: async () => import('../pages/settings/NotificationsPage.vue')
          },
          {
            path: 'performance',
            name: 'settings_performance',
            meta: {
              requiresAuthentication: true,
              requiresNav: false,
              requiresSettingsNav: true
            },
            component: async () => import('../pages/settings/PerformancePage.vue')
          },
          {
            path: 'privacy',
            name: 'settings_privacy',
            meta: {
              requiresAuthentication: true,
              requiresNav: false,
              requiresSettingsNav: true
            },
            component: async () => import('../pages/settings/PrivacyPage.vue')
          },
          {
            path: 'advanced',
            name: 'settings_advanced',
            meta: {
              requiresAuthentication: true,
              requiresNav: false,
              requiresSettingsNav: true
            },
            component: async () => import('../pages/settings/AdvancedPage.vue')
          }
        ]
      }
    ]
  }
]

export default routes
