import { createApp } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { createPinia } from 'pinia'

import App from './App.vue'

import Router from './router'
import createPlugins from './plugins'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'
import './style.css'

const defaultPlugins = createPlugins()
const pinia = createPinia()

const app = createApp(App)
app.use(Router)
app.use(pinia)
app.use(defaultPlugins)
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
