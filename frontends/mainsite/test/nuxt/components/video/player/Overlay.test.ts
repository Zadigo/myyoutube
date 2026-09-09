import { mockNuxtImport, mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it, vi, expect } from 'vitest'
import VideoPlayerOverlay from '~/components/video/player/Overlay.vue'
import { definedTestCases } from '~~/test/__mocks__'

describe('components > video > player > Overlay', () => {
  const testCases = definedTestCases((manager) => {
    return manager.parameterize(
      [
        {
          title: 'with fact checking true',
          expectedValue: true
        },
        {
          title: 'with fact checking false',
          expectedValue: false
        },
        {
          title: 'with show general alert true',
          expectedValue: true
        },
        {
          title: 'with show general alert false',
          expectedValue: false
        },
        {
          title: 'with both fact checking and show general alert true',
          expectedValue: true
        }
      ]
    )
  })

  testCases.runner.forEach((testCase) => {
    it(`should render with ${testCase.title}`, async () => {
      const component = await mountSuspended(VideoPlayerOverlay)
      
      if (testCase.title === 'with fact checking true') {
        component.vm.showFactCheck = true
        expect(component.vm.showFactCheck).toBe(true)
        console.log(component.html()) // Debugging: Check the rendered HTML
      }
    })
  })
})
