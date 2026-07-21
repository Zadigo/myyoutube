import { defineConfig } from 'vitest/config'
import { defineVitestProject } from '@nuxt/test-utils/config'
import { fileURLToPath } from 'node:url'

export default defineConfig({
  test: {
    exclude: [ 'node_modules', '.nuxt', 'dist', 'test/nuxt' ],
    coverage: {
      enabled: true,
      provider: 'v8',
      reporter: [ 'text', 'json', 'html' ]
    },
    env: {
      NODE_ENV: 'test'
    },
    projects: [
      await defineVitestProject({
        test: {
          name: 'unit',
          include: [ 'test/unit/**/*.{test,spec}.ts' ],
          environment: 'node',
          testTimeout: 20000
        }
      }),
      await defineVitestProject({
        test: {
          name: 'nuxt',
          include: [ 'test/nuxt/**/*.{test,spec}.ts' ],
          environment: 'nuxt',
          testTimeout: 20000
        }
      }),
      await defineVitestProject({
        test: {
          name: 'integration',
          include: [ 'test/integration/**/*.{test,spec}.ts' ],
          environment: 'node',
          testTimeout: 20000
        }
      })
    ]
  },
  resolve: {
    alias: {
    }
  }
})
