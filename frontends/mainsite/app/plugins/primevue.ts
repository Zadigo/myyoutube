import PrimeVue from 'primevue/config'

// https://volt.primevue.org/nuxt/

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(PrimeVue, {
    unstyled: true
  })
})
