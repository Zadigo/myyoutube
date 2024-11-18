import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { createPinia } from 'pinia';
import { createApp, toRaw } from 'vue';
import { createVuetify } from "vuetify";
import { createVueLocalStorage, createVueSession, VueSessionInstance } from './plugins/vue-storages';

import DayJsAdapter from "@date-io/dayjs";
import App from './App.vue';
import installPlugins from './plugins';
import Router from './router';

import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { aliases, mdi } from "vuetify/iconsets/mdi";
import colors from "vuetify/util/colors";

import './style.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap';
import 'mdb-ui-kit/css/mdb.min.css';
import 'vuetify/styles';

const app = createApp(App)

const pinia = createPinia()

const localstorage = createVueLocalStorage()
const session = createVueSession()

const vuetify = createVuetify({
    components,
    directives,
    date: {
        adapter: DayJsAdapter,
    },
    theme: {
        themes: {
            light: {
                dark: false,
                colors: {
                    primary: colors.red.darken1,
                },
            },
        },
    },
    icons: {
        defaultSet: "mdi",
        aliases,
        sets: {
            mdi,
        },
    },
});

pinia.use(({ store }) => {
    store.$session = toRaw(VueSessionInstance)
})

app.use(pinia)
app.use(Router)
app.use(vuetify)
app.use(localstorage)
app.use(session)
app.use(installPlugins())
app.component('FontAwesomeIcon', FontAwesomeIcon)

app.mount('#app')
