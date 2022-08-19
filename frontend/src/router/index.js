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
        component: loadView('account/AlgorithmPreferenceView')
      },
      {
        path: 'algorithm',
        name: 'algorithm_preference_view',
        component: loadView('account/AlgorithmPreferenceView')
      }
    ]
  }
]

export default createRouter({
  history: createWebHistory(),
  scrollBehavior: scrollToTop,
  routes: routes
})
