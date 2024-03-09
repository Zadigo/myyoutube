import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'
import { useAuthentication } from '../store/authentication'

const Router = createRouter({
  history: createWebHistory(),
  scrollBehavior: () => ({ top: 0, left: 0 }),
  routes
})

Router.beforeEach((to, from, next) => {
  const store = useAuthentication()
  store
  next()
})

export default Router
