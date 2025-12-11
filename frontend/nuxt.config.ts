import tailwindcss from '@tailwindcss/vite'

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
    '/': { ssr: false },
    '/videos/**': { ssr: true },
    '/playlists': { ssr: false },
    '/settings/**': { ssr: false },
    '/studio/**': { ssr: false },
    '/school': { ssr: false },
    '/channels': { ssr: false },
    '/fact-checking': { ssr: false },
    '/community-notes/**': { swr: true, cache: { maxAge: 30 * 60 }},
    '/login': { ssr: false },
    '/notification': { swr: true, cache: { maxAge: 30 * 60 }},
    '/search': { ssr: false }
  },

  app: {
    pageTransition: {
      name: 'page',
      mode: 'out-in'
    }
  },

  vite: {
    plugins: [
      tailwindcss()
    ]
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
  
  runtimeConfig: {
    public: {
      // Django
      djangoProdUrl: process.env.NUXT_DJANGO_PROD_URL || 'http://127.0.0.1:8000',
      djangoModerationProdUrl: process.env.NUXT_DJANGO_MODERATION_PROD_URL || 'http://127.0.0.1:8001',
      djangoNotificationsProdUrl: process.env.NUXT_DJANGO_NOTIFICATIONS_PROD_URL || 'http://127.0.0.1:8002',
      djangoDonationsProdUrl: process.env.NUXT_DJANGO_DONATIONS_PROD_URL || 'http://127.0.0.1:8003',
      djangoCommentsProdUrl: process.env.NUXT_DJANGO_COMMENTS_PROD_URL || 'http://127.0.0.1:8004',

      // Quart & Go APIs
      apiCategories: process.env.NUXT_QUART_CATEGORIES_PROD_URL || 'http://127.0.0.1:5000',
      apiReports: process.env.NUXT_QUART_REPORTS_PROD_URL || 'http://127.0.0.1:5001',
      apiUploads: process.env.NUXT_GO_UPLOADS_PROD_URL || 'http://127.0.0.1:8080',
      
      // Stripe
      stripeSecretKey: process.env.NUXT_STRIPE_TEST_SECRET_KEY,
      stripePublishableKey: process.env.NUXT_STRIPE_TEST_PUBLISHABLE_KEY,
      stripeAccount: process.env.NUXT_STRIPE_TEST_PUBLISHABLE_KEY,
      stripeApiVersion: '2024-06-20',
      stripeLocale: 'fr'
    }
  },
  
  modules: [
    '@nuxt/eslint',
    '@nuxt/hints',
    '@nuxt/test-utils/module',
    '@unlok-co/nuxt-stripe',
    '@nuxtjs/sitemap',
    '@nuxt/image',
    '@vueuse/nuxt',
    '@nuxtjs/i18n',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@pinia/nuxt',
    'vue-sonner/nuxt',
    'nuxt-authentication',
    'nuxt-vuefire',
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
        weights: ['100', '200', '300', '400', '500', '600', '700', '800']
      },
      // Titles
      {
        name: 'Manrope',
        display: 'swap',
        weights: ['200', '300', '400', '500', '600', '700', '800']
      }
    ]
  },

  nuxtAuthentication: {
    enabled: false
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
