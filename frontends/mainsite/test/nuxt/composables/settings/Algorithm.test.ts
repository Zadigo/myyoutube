import { beforeEach, describe, expect, it } from 'vitest'
import { useAlgorithmSettingsComposable, useAlgorithmSettingsStore  } from '../../../../app/composables/index.ts'
import { mountSuspended } from '@nuxt/test-utils/runtime'
import { defineComponent, toValue } from 'vue'
import type { AlgorithmConditionBlock } from '../../../../app/data/validation/settings/index.ts'

const conditions: AlgorithmConditionBlock[] = []

describe('useAlgorithmSettingsComposable', () => {
  let result: ReturnType<typeof useAlgorithmSettingsComposable>

  beforeEach(async () => {
    const componentB = defineComponent({
      template: '<div></div>',
      setup() {
        useAlgorithmSettingsStore()
      }
    })

    const componentA = defineComponent({
      template: `
      <div>
        <component-b />
      </div>
      `,
      components: {
        'component-b': componentB
      },
      setup() {
        result = useAlgorithmSettingsComposable()
        result.conditions.value = conditions

        return {
          result
        }
      }
    })

    await mountSuspended(componentA)

    result.conditions.value = []
  })

  it('should return an object with the expected properties', async () => {
    expect(result).toBeDefined()

    expect(result.conditions).toBeDefined()
    expect(result.create).toBeDefined()
    expect(result.remove).toBeDefined()
    expect(result.getCurrentBlock).toBeDefined()

    expect(result.create).toBeInstanceOf(Function)
    expect(result.remove).toBeInstanceOf(Function)
    expect(result.getCurrentBlock).toBeInstanceOf(Function)

    const value = result.getCurrentBlock(0)
    expect(toValue(value)).toBeUndefined()
  })

  it('should create a new condition block', async () => {
    expect(result).toBeDefined()
    await result.create()
    expect(result.conditions.value.length).toBe(1)

    const newBlock = result.conditions.value[0]
    expect(newBlock).toEqual({
      id: 1,
      theme: '',
      keyword_operator: 'Exact match',
      keywords: [],
      keywords_subconditions: [],
      video_sections: [],
      join_operator: 'And',
      negation: false
    })
  })

  it('should remove a condition block', async () => {
    expect(result).toBeDefined()
    await result.create()

    result.remove(0)
    expect(result.conditions.value.length).toBe(0)
  })
})

describe('useAlgorithmSettingsStore', () => {
  it('should throw an error if used outside of a provider', () => {
    expect(() => useAlgorithmSettingsStore()).toThrow(new Error('injectLocal must be called in setup'))
  })
})
