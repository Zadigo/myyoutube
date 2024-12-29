import { createPinia } from 'pinia'
import { createApp } from 'vue'
import App from './App.vue'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { loadFonts } from './plugins'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'
import '@mdi/font/css/materialdesignicons.css'
import '@/assets/style.css'
import '@/assets/loading.css'
import '@/plugins/fontawesome'

import router from './router'
import i18n from './i18n'

loadFonts()

const pinia = createPinia()

const app = createApp(App)

// TODO: Delete on next update
app.config.unwrapInjectedRef = true

app.component('FontAwesomeIcon', FontAwesomeIcon)
app.use(router)
app.use(pinia)
app.use(i18n)
app.mount('#app')
