import path from 'path'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  // ssr: false,
  // routeRules: {},
  runtimeConfig: {
    public: {
      DJANGO_PROD_URL: process.env.NUXT_DJANGO_PROD_URL,
      STRIPE_SECRET_KEY: process.env.NUXT_STRIPE_TEST_SECRET_KEY,
      STRIPE_PUBLISHABLE_KEY: process.env.NUXT_STRIPE_TEST_PUBLISHABLE_KEY,
      STRIPE_ACCOUNT: process.env.NUXT_STRIPE_TEST_PUBLISHABLE_KEY,
      STRIPE_API_VERSION: '2024-06-20',
      STRIPE_LOCALE: 'fr'
    }
  },
  modules: [
    '@nuxt/eslint',
    '@pinia/nuxt',
    '@artmizu/nuxt-prometheus',
    '@vesp/nuxt-fontawesome',
    '@nuxtjs/google-fonts',
    '@nuxt/test-utils/module',
    '@unlok-co/nuxt-stripe',
    '@nuxtjs/sitemap',
    '@nuxt/image',
    '@nuxtjs/i18n',
    'nuxt-gtag',
    // 'nuxt-meta-pixel', // BUG: This raises an error with minimatch
    'nuxt-clarity-analytics',
    'nuxt-openapi-docs-module',
    'vuetify-nuxt-module',
    'vue-sonner/nuxt'
  ],
  alias: {
    '@': path.resolve(__dirname, './'),
    '@types': './types'
  },
  css: [
    '@/assets/style.scss',
    '~/node_modules/bootstrap/dist/css/bootstrap.min.css',
    '~/node_modules/mdb-ui-kit/css/mdb.min.css',
    '~/node_modules/animate.css/animate.min.css',
  ],
  googleFonts: {
    families: {
      Ubuntu: {
        wght: '100..700'
      },
      Roboto: {
        wght: '100..700'
      },
      Lato: {
        wght: '100..700'
      },
      "Noto Sans": {
        wght: '100..700'
      }
    }
  },
  fontawesome: {
    icons: {
      regular: [],
      solid: [
        'chart-simple',
        'cog',
        'home'
      ],
      brands: []
    }
  },
  test: true,
  testUtils: {
    vitestConfig: {
      alias: {
        '@': path.resolve(__dirname, './')
      },
      css: true,
      deps: {
        optimizer: {
          ssr: {
            include: ['@nuxt/test-utils']
          }
        }
      }
    }
  },
  i18n: {
    baseUrl: './',
    langDir: './locales',
    defaultLocale: 'fr',
    vueI18n: './i18n.config.ts',
    locales: [
      { code: 'en', language: 'en-US', file: 'en-US.json', dir: 'ltr' },
      { code: 'fr', language: 'fr-FR', file: 'fr-FR.json', dir: 'ltr' }
    ]
  },
})
