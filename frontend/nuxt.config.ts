import tailwindcss from "@tailwindcss/vite"

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: {
    enabled: true,
    timeline: {
      enabled: true
    }
  },
  ssr: true,

  routeRules: {
    '/': { ssr: false },
    '/videos/**': { ssr: true, swr: true, cache: { maxAge: 30 * 60 } },
    '/playlists': { ssr: false },
    '/settings/**': { ssr: false },
    '/studio/**': { ssr: false },
    '/school': { prerender: true },
    '/channels': { ssr: false },
    '/fact-checking': { ssr: false },
    '/community-notes/**': { ssr: false, swr: true, cache: { maxAge: 30 * 60 } },
    '/login': { prerender: true },
    '/notification': { ssr:false, swr: true, cache: { maxAge: 30 * 60 } },
    '/search': { ssr: false }
  },

  app: {
    pageTransition: {
      name: 'page',
      mode: 'out-in'
    }
  },

  vuefire: {
    config: {
      apiKey: process.env.NUXT_PUBLIC_FIREBASE_API_KEY,
      authDomain: process.env.NUXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
      dbUrl: process.env.NUXT_PUBLIC_FIREBASE_DB_URL,
      storageBucket: process.env.NUXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
      appId: process.env.NUXT_PUBLIC_FIREBASE_APP_ID,
      measurementId: process.env.NUXT_PUBLIC_FIREBASE_MEASUREMENT_ID,
      messageSenderId: process.env.NUXT_PUBLIC_FIREBASE_MESSAGE_SENDER_ID,
      projectId: process.env.NUXT_PUBLIC_FIREBASE_PROJECT_ID
    }
  },

  modules: [
    '@pinia/nuxt',
    '@vueuse/nuxt',
    '@nuxt/fonts',
    '@nuxtjs/seo',
    '@nuxt/test-utils',
    '@nuxt/hints',
    '@nuxt/image',
    '@nuxt/icon',
    'nuxt-authentication',
    'nuxt-vuefire',
    '@nuxtjs/i18n',
    '@nuxt/a11y'
  ],

  css: [
    '~/assets/css/tailwind.css'
  ],

  fonts: {
    provider: 'google',
    families: [
      {
        name: 'Sora',
        display: 'swap',
        weights: [ '100', '200', '300', '400', '500', '600', '700', '800' ]
      },
      // Titles
      {
        name: 'Manrope',
        display: 'swap',
        weights: [ '200', '300', '400', '500', '600', '700', '800' ]
      }
    ]
  },

  nuxtAuthentication: {
    enabled: false,
    domain: 'http://127.0.0.1:8000',
  },

  i18n: {
    baseUrl: './',
    langDir: './locales',
    defaultLocale: 'fr',
    vueI18n: './i18n.config.ts',
    locales: [
      {
        code: 'en',
        language: 'en-US',
        file: 'en-US.json',
        dir: 'ltr'
      },
      {
        code: 'fr',
        language: 'fr-FR',
        file: 'fr-FR.json',
        dir: 'ltr'
      }
    ]
  },

  vite: {
    plugins: [
      tailwindcss(),
    ],

    optimizeDeps: {
      include: [
        'primevue/config',
        'dayjs', // CJS
        'dayjs/plugin/calendar', // CJS
        'dayjs/plugin/duration', // CJS
        'dayjs/plugin/relativeTime', // CJS
        'dayjs/plugin/timezone', // CJS
        'dayjs/plugin/utc', // CJS
        'primevue/inputtext',
        'primevue/skeleton',
        'primevue/card',
        'primevue/select',
        'primevue/button',
        'primevue/menu',
        'tailwind-merge',
        'zod'
      ]
    }
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
