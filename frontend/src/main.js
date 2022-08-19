import { createPinia } from 'pinia'
import { createApp } from 'vue'
import App from './App.vue'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { loadFonts } from './plugins'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'
import '@/assets/style.css'
import '@/assets/loading.css'
import '@/plugins/fontawesome'

import router from './router'

loadFonts()

const pinia = createPinia()

const app = createApp(App)
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.use(router)
app.use(pinia)
app.mount('#app')
