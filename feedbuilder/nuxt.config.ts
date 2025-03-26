// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  ssr: true,
  routeRules: {
    '/': { ssr: false }
  },
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
    '@nuxt/image',
    '@nuxt/icon',
    '@nuxtjs/google-fonts',
    '@vueuse/nuxt',
    'vuetify-nuxt-module'
  ],
  css: [
    '~/assets/css/main.css',
    // '~/node_modules/bootstrap/dist/css/bootstrap.min.css'
  ],
  googleFonts: {
    families: {
      Roboto: {
        wght: '100..700'
      },
      Ubuntu: {
        wght: '100..700'
      }
    }
  }
})