import { App } from "vue";
import { authClient, client, quartClient } from "./axios";

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
      app.config.globalProperties.$quartClient = quartClient
      app.config.globalProperties.$authClient = authClient
      app.config.globalProperties.$date = dayjs

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
