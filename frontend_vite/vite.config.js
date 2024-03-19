import { defineConfig, loadEnv } from 'vite'

import path from 'path'
import vue from '@vitejs/plugin-vue'
import eslint from 'vite-plugin-eslint'

// https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [
//     vue()
//   ],
// })

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')

  return {
    resolve: {
      alias: {
        '@/': path.resolve(__dirname, 'src'),
        'components': path.resolve(__dirname, 'src/components'),
        'layouts': path.resolve(__dirname, 'src/layouts'),
        'pages': path.resolve(__dirname, 'src/pages'),
        'store': path.resolve(__dirname, 'src/store'),
        'data': path.resolve(__dirname, 'src/data')
      },
      extensions: ['.mjs', '.js', '.mts', '.ts', '.jsx', '.tsx', '.json', '.vue']
    },
    define: {
      __APP_ENV__: JSON.stringify(env)
    },
    plugins: [
      vue(),
      eslint()
    ]
  }
})
