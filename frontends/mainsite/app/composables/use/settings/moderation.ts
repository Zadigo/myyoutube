import type { BlockedChannel, BlockedKeyword } from '~/types'

/**
 * Composables for managing blocked channels in the settings.
 * It provides functionality to fetch and manage blocked channels.
 */
export function useBlockedChannels() {
  const blockedChannels = computedAsync(() => {
    return $fetch<BlockedChannel[]>('/user-channels/blocked', {
      method: 'GET',
      baseURL: useRuntimeConfig().public.djangoProdUrl
    })
  })

  const channels = toRef(() => blockedChannels.value || [])
  const hasChannels = computed(() => channels.value.length > 0)

  const showCreateList = ref<boolean>(false)
  const showBlockLists = ref<boolean>(false)


  return {
    /**
     * Flag to control the visibility of the create list modal.
     */
    showCreateList,
    /**
     * Flag to control the visibility of the block lists modal.
     */
    showBlockLists,
    /**
     * List of blocked channels.
     */
    channels,
    /**
     * Flag indicating whether there are blocked channels.
     */
    hasChannels
  }
}

/**
 * Composables for managing block lists in the settings.
 * It provides functionality to fetch and manage block lists.
 */
export function useBlockLists() { }

/**
 * Composables for managing blocked keywords in the settings.
 * It provides functionality to add, remove, and manage blocked keywords.
 */
const [ useBlockedKeywordsComposable, _useBlockedKeywordsStore ] = createInjectionState(() => {
  const keywords = reactive<BlockedKeyword[]>([])

  const newKeyword = ref<BlockedKeyword>({ word: '', duration: 'Forever' })
  const { history, undo, redo } = useRefHistory(newKeyword)

  function create() {
    keywords.push({ ...newKeyword.value })
  }

  function remove(index: number) {
    keywords.splice(index, 1)
  }

  const excludeFollowedAccounts = ref<boolean>(false)

  const hasKeywords = computed(() => keywords.length > 0)

  return {
    hasKeywords,
    /**
     * Applies the blocking only to videos from accounts that are not followed
     */
    excludeFollowedAccounts,
    /**
     * New keyword to be added.
     */
    newKeyword,
    /**
     * History management for the new keyword input.
     */
    history,
    /**
     * List of blocked keywords.
     */
    keywords,
    create,
    remove,
    undo,
    redo
  }
})

export { useBlockedKeywordsComposable }

export function useBlockedKeywordsStore() {
  const store = _useBlockedKeywordsStore()
  if (!store) {
    throw new Error('useBlockedKeywordsStore must be used within a provider.')
  }
  return store
}
