import { loadLayout, loadView } from "@/composables/utils"
import { createRouter, createWebHistory } from "vue-router"

const routes = [
  {
    path: '/',
    name: 'home_view',
    component: loadView('VideoView')
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
    name: 'short_videos_view',
    component: loadView('ShortVideosView')
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
  routes: routes
})
