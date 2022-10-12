import { loadLayout, loadView, scrollToTop } from "@/composables/utils"
import { createRouter, createWebHistory } from "vue-router"

const routes = [
  {
    path: '/',
    name: 'home_view',
    component: loadView('TimelinePageView')
  },
  {
    // path: '/video/:id([a-zA-Z0-9]+)',
    path: '/video',
    name: 'video_view',
    component: loadView('LongVideoView')
  },
  {
    // path: '/video/:id([a-zA-Z0-9]+)',
    path: '/short-videos',
    component: loadLayout('BaseShorts'),
    children: [
      {
        path: '',
        name: 'short_videos_view',
        component: loadView('shorts/ListView')
      },
      {
        path: '@google/video/ifFVs4GIvnudorr4356',
        name: 'short_video_details_view',
        component: loadView('shorts/DetailsView')
      }
    ]
  },
  {
    // path: '/channel/:id([a-zA-Z0-9]+)',
    path: '/channel',
    name: 'channel_view',
    component: loadView('ChannelView')
  },
  {
    path: '/account',
    component: loadLayout('BaseAccount'),
    children: [
      {
        path: '',
        name: 'account_view',
        component: loadView('account/MyAccount')
      },
      {
        path: 'notifications',
        name: 'account_notifications_view',
        component: loadView('account/NotificationsView')
      },
      {
        path: 'algorithm',
        name: 'algorithm_preference_view',
        component: loadView('account/AlgorithmPreferenceView')
      },
      {
        path: 'privacy',
        name: 'account_privacy_view',
        component: loadView('account/PrivacyView')
      },
      {
        path: 'performance',
        name: 'account_performance_view',
        component: loadView('account/PerformanceView')
      },
      {
        path: 'advanced',
        name: 'account_advanced_view',
        component: loadView('account/AdvancedView')
      }
    ]
  },
  {
    path: '/playlists',
    name: 'playlists_view',
    component: loadView('PlaylistsView')
  },
  {
    path: '/notfications',
    name: 'notifications_view',
    component: loadView('NotificationsView')
  },
  {
    path: '/my-studio',
    name: 'my_studio_view',
    component: loadView('MyStudioView')
  }
]

export default createRouter({
  history: createWebHistory(),
  scrollBehavior: scrollToTop,
  routes: routes
})
