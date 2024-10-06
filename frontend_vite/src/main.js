import { createApp } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { createPinia } from 'pinia'
import { createVuetify } from 'vuetify'
import { createVueSession } from './plugins/vue-storages'

import App from './App.vue'

import Router from './router'
import createPlugins from './plugins'

import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
// import { aliases, mdi } from 'vuetify/iconsets/mdi'
import { aliases, fa } from 'vuetify/iconsets/fa'

import 'bootstrap/dist/css/bootstrap.min.css'
import '@mdi/font/css/materialdesignicons.css'
import 'mdb-ui-kit/css/mdb.min.css'
import 'vuetify/styles'
import './style.css'
import './dashboard.css'

const defaultPlugins = createPlugins()
const session = createVueSession()
const pinia = createPinia()
const vuetify = createVuetify({
  components,
  directives,
  // icons: {
  //   defaultSet: 'mdi',
  //   aliases,
  //   sets: {
  //     mdi
  //   }
  // }
  icons: {
    defaultSet: 'fa',
    aliases,
    sets: {
      fa
    }
  }
})

const app = createApp(App)
app.use(Router)
app.use(vuetify)
app.use(pinia)
app.use(session)
app.use(defaultPlugins)
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
