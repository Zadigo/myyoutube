import { axios, client } from './axios'
import { loadFonts } from './font'
import './fontawesome'
import dayjs from './dayjs'

loadFonts()

function createPlugins () {
  return (app) => {
    app.config.globalProperties.$axios = axios
    app.config.globalProperties.$client = client
    app.config.globalProperties.$date = dayjs

    if (import.meta.env.MODE === 'development') {
      window.dayjs = dayjs
    }
    app.mixin({
      data () {
        return {
          currentDate: dayjs().toString()
        }
      }
    })
  }
}

export default createPlugins
