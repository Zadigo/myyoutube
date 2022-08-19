import { loadView } from "@/composables/utils"
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
    component: loadView('VideoView')
  }
]

export default createRouter({
  history: createWebHistory(),
  routes: routes
})
