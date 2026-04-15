import type { AlgorithmConditionBlock } from "~/data"

const [useAlgorithmSettingsComposable, _useAlgorithmSettingsStore] = createInjectionState(() => {
  const conditions = ref<AlgorithmConditionBlock[]>([])

    watchArray(conditions, (newList, oldList) => {
      // Do something
      console.log(newList,  oldList)
    })

    const getCurrentBlock = reactify((index: number) => {
      return conditions.value[index]
    })

  const { count: currentIndex, inc } = useCounter(0)

  async function create() {
    inc()

    conditions.value.push({
      id: currentIndex.value,
      theme: '',
      keyword_operator: 'Exact match',
      keywords: [],
      keywords_subconditions: [],
      video_sections: [],
      join_operator: 'And',
      negation: false
    })
  }

  async function remove(index: number) {
    conditions.value.splice(index, 1)
  }

  return {
    conditions,
    create,
    remove,
    getCurrentBlock
  }
})

export { useAlgorithmSettingsComposable }

export function useAlgorithmSettingsStore() {
  const store = _useAlgorithmSettingsStore()
  if (!store) {
    throw new Error('useAlgorithmSettingsStore must be used within a provider.')
  }
  return store
}
