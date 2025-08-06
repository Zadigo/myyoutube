import tailwind from '@tailwindcss/vite'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  
  devtools: {
    enabled: true,

    timeline: {
      enabled: true
    }
  },
  
  ssr: true,
  
  routeRules: {
    '/': { ssr: false }
  },

  vite: {
    plugins: [
      tailwind()
    ]
  },

  modules: [
    '@pinia/nuxt',
    '@nuxt/image',
    '@nuxt/icon',
    '@nuxt/fonts',
    '@vueuse/nuxt'
  ],

  vuefire: {
    config: {
      apiKey: process.env.NUXT_FIREBASE_API_KEY,
      authDomain: process.env.NUXT_FIREBASE_AUTH_DOMAIN,
      dbUrl: process.env.NUXT_FIREBASE_DB_URL,
      storageBucket: process.env.NUXT_FIREBASE_STORAGE_BUCKET,
      appId: process.env.NUXT_FIREBASE_APP_ID,
      measurementId: process.env.NUXT_FIREBASE_MEASUREMENT_ID,
      messageSenderId: process.env.NUXT_FIREBASE_MESSAGE_SENDER_ID,
      projectId: process.env.NUXT_FIREBASE_PROJECT_ID
    }
  },
  
  css: [
    '~/assets/css/main.css'
  ],

  // https://www.fontpair.co/all
  fonts: {
    provider: 'google',
    families: [
      {
        name: 'Raleway',
        display: 'swap'
      },
      // Titles
      {
        name: 'Poppins',
        display: 'swap'
      },
      {
        name: 'Be Vietnam Pro',
        display: 'swap'
      }
    ]
  },

  nitro: {
    storage: {
      redis: {
        driver: 'redis',
        host: '127.0.0.1',
        port: 6379,
        username: '',
        password: 'django-local-testing'
      }
    }
  }
})
