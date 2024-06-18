/// <reference types="vitest" />
import { defineConfig, loadEnv } from 'vite'

import path from 'path'
import vue from '@vitejs/plugin-vue'
import eslint from 'vite-plugin-eslint'

export default defineConfig(({ mode }) => {
  const root = process.cwd()
  const env = loadEnv(mode, root)
  process.env = { ...process.env, ...env }

  return {
    resolve: {
      alias: {
        '@/': path.resolve(__dirname, 'src'),
        'src': path.resolve(__dirname, 'src'),
        'components': path.resolve(__dirname, 'src/components'),
        'layouts': path.resolve(__dirname, 'src/layouts'),
        'pages': path.resolve(__dirname, 'src/pages'),
        'store': path.resolve(__dirname, 'src/store'),
        'data': path.resolve(__dirname, 'src/data'),
        'composables': path.resolve(__dirname, 'src/composables')
      },
      extensions: ['.mjs', '.js', '.mts', '.ts', '.jsx', '.tsx', '.json', '.vue']
    },
    define: {
      __APP_ENV__: JSON.stringify(env)
    },
    plugins: [
      vue(),
      eslint({ lintOnStart: true })
    ],
    test: {
      alias: {},
      browser: {
        enabled: true,
        name: 'chrome'
      }
    }
  }
})
