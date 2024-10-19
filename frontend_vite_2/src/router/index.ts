import { createRouter, createWebHistory } from 'vue-router'
// import { useAuthentication } from '../store/authentication'

const Router = createRouter({
  history: createWebHistory(),
  scrollBehavior: () => ({ top: 0, left: 0 }),
  routes: [
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
                    path: 'video/:id(vid_[a-zA-Z0-9]+)',
                    name: 'video_details',
                    meta: {
                        requiresAuthentication: false,
                        requiresNav: true
                    },
                    component: async () => import('../pages/VideoPage.vue')
                },
                {
                    path: 'channel/:id(ch_[a-zA-Z0-9]+)',
                    name: 'channel_details',
                    meta: {
                    requiresAuthentication: false,
                    requiresNav: true
                    },
                    component: async () => import('../pages/ChannelPage.vue')
                },
                // {
                //     path: 'playlists',
                //     name: 'playlists',
                //     meta: {
                //     requiresAuthentication: true,
                //     requiresNav: true
                //     },
                //     component: async () => import('../pages/PlaylistsPage.vue')
                // },
                // {
                //     path: 'notifications',
                //     children: [
                //         {
                //             path: '',
                //             name: 'notifications',
                //             meta: {
                //             requiresAuthentication: true,
                //             requiresNav: true
                //             },
                //             component: async () => import('../pages/NotificationsPage.vue')
                //         },
                //         {
                //             path: 'messages',
                //             name: 'notifications_messages',
                //             meta: {
                //             requiresAuthentication: true,
                //             requiresNav: true
                //             },
                //             component: async () => import('../pages/NotificationsPage.vue')
                //         },
                //         {
                //             path: 'uploads',
                //             name: 'notifications_uploads',
                //             meta: {
                //             requiresAuthentication: true,
                //             requiresNav: true
                //             },
                //             component: async () => import('../pages/NotificationsPage.vue')
                //         }
                //     ]
                //     // name: 'notifications',
                //     // meta: { requiresAuthentication: false },
                //     // component: async () => import('../pages/NotificationsPage.vue')
                // },
                {
                    path: 'my-studio',
                    children: [
                        {
                            path: '',
                            name: 'my_studio',
                            meta: {
                            requiresAuthentication: true,
                            requiresNav: true
                            },
                            component: async () => import('../pages/studio/HomePage.vue')
                        },
                        {
                            path: 'upload',
                            name: 'my_studio_upload',
                            meta: {
                            requiresAuthentication: true,
                            requiresNav: true
                            },
                            component: async () => import('../pages/studio/UploadPage.vue')
                        },
                        {
                            path: 'videos/:id',
                            name: 'edit_my_studio_video',
                            meta: {
                            requiresAuthentication: true,
                            requiresNav: true
                            },
                            component: async () => import('../pages/studio/EditVideoPage.vue')
                        }
                    ]
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
        },
        {
            path: '/login',
            name: 'login',
            component: async () => import('../pages/LoginPage.vue')
        }
    ]
})

// Router.beforeEach((to, from, next) => {
//   const store = useAuthentication()
//   store
//   next()
// })

export default Router
