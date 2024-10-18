import { App } from "vue";
import { authClient, client } from "./axios";

import './font'
import './fontawesome'
import dayjs from "./dayjs";

if (import.meta.env.DEV) {
  window.AxiosClient = client
}

export default function installPlugins () {
  return {
    install (app: App) {
      app.config.globalProperties.$client = client
      app.config.globalProperties.$authClient = authClient

      app.mixin({
        data () {
          return {
            currentDate: dayjs().toString()
          }
        }
      })
    }
  }
}

// import { axios, client } from './axios'
// import { loadFonts } from './font'
// // import { useVueSession } from './vue-storages'

// import dayjs from './dayjs'

// import './fontawesome'

// function createPlugins () {
//   return (app) => {
//     loadFonts()

//     app.config.globalProperties.$axios = axios
//     app.config.globalProperties.$client = client
//     app.config.globalProperties.$date = dayjs

//     if (import.meta.env.MODE === 'development') {
//       window.dayjs = dayjs
//       window.client = client
//       window.axios = axios
//     }
//     app.mixin({
//       data () {
//         return {
//           currentDate: dayjs().toString()
//         }
//       }
//     })
//   }
// }

// export default createPlugins

// export {
//   client,
//   useVueSession
// }
