import dayjs from 'dayjs'

export default defineNuxtPlugin(async nuxtApp => {
  return {
    provide: {
      $dayjs: dayjs,
      $date: dayjs()
    }
  }
})
