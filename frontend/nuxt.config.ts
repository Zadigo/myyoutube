import tailwindcss from '@tailwindcss/vite'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  ssr: true,

  routeRules: {
    '/': { ssr: false },
    '/videos/**': { ssr: true },
    '/playlists': { ssr: false },
    '/settings/**': { ssr: false },
    '/studio/**': { ssr: false },
    '/school': { ssr: false },
    '/channels': { ssr: false },
    '/fact-checking': { ssr: false },
    '/community-notes': { swr: true, cache: { maxAge: 30 * 60 }},
    '/login': { ssr: false },
    '/notification': { swr: true, cache: { maxAge: 30 * 60 }},
    '/search': { ssr: false }
  },

  vite: {
    plugins: [
      tailwindcss()
    ]
  },

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
  
  runtimeConfig: {
    public: {
      // Django
      djangoProdUrl: process.env.NUXT_DJANGO_PROD_URL || 'http://127.0.0.1:8000',
      apiCategories: process.env.NUXT_DJANGO_PROD_URL || 'http://127.0.0.1:5000',
      apiReports: process.env.NUXT_DJANGO_PROD_URL || 'http://127.0.0.1:5001',
      
      // Stripe
      stripeSecretKey: process.env.NUXT_STRIPE_TEST_SECRET_KEY,
      stripePublishableKey: process.env.NUXT_STRIPE_TEST_PUBLISHABLE_KEY,
      stripeAccount: process.env.NUXT_STRIPE_TEST_PUBLISHABLE_KEY,
      stripeApiVersion: '2024-06-20',
      stripeLocale: 'fr'
    }
  },
  
  // '@artmizu/nuxt-prometheus',
  // 'vuetify-nuxt-module',
  // '@nuxtjs/i18n',

  modules: [
    '@nuxt/eslint',
    '@vesp/nuxt-fontawesome',
    '@nuxt/test-utils/module',
    '@unlok-co/nuxt-stripe',
    '@nuxtjs/sitemap',
    '@nuxt/image',
    '@pinia/nuxt',
    '@vueuse/nuxt',
    '@nuxtjs/i18n',
    '@nuxt/fonts',
    '@nuxt/icon',
    'vue-sonner/nuxt',
    'nuxt-vuefire'
  ],

  css: [
    '~/assets/css/tailwind.css'
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

  fontawesome: {
    icons: {
      regular: [
        'thumbs-up',
        'thumbs-down'
      ],
      solid: [
        'a',
        'arrow-right',
        'arrow-left',
        'bell',
        'bell-slash',
        'building-shield',
        'bullhorn',
        'bars',
        'circle-check',
        'caret-down',
        'caret-up',
        'compress',
        'comment',
        'comments',
        'chart-simple',
        'cog',
        'dollar-sign',
        'download',
        'expand',
        'ellipsis-vertical',
        'face-smile',
        'filter',
        'filter-circle-xmark',
        'gift',
        'home',
        'heart',
        'list',
        'lock',
        'microchip',
        'note-sticky',
        'save',
        'share',
        'star',
        'store',
        'store',
        'sort',
        'pen',
        'plus',
        'play',
        'pause',
        'ranking-star',
        'trash',
        'tv',
        'user',
        'user-minus',
        'upload',
        'thumbs-up',
        'thumbs-down',
        'volume-up',
        'volume-low',
        'volume-high',
      ],
      brands: []
    }
  },

  // test: true,
  // testUtils: {
  //   vitestConfig: {
  //     css: true,
  //     deps: {
  //       optimizer: {
  //         ssr: {
  //           include: ['@nuxt/test-utils']
  //         }
  //       }
  //     }
  //   }
  // },

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
