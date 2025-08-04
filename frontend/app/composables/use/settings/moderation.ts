import type { BlockedChannel, BlockedKeyword } from '~/types'

export function useBlockedChannels() {
  /**
   * Fetch the list of blocked channels.
   */
  const { execute, data } = useAsyncData(() => {
    return $fetch<BlockedChannel[]>('/user-channels/blocked', {
      method: 'GET',
      baseURL: useRuntimeConfig().public.djangoProdUrl
    })
  }, {
    immediate: false
  })

  onBeforeMount(async () => {
    await execute()
  })

  const channels = toRef(() => data.value || [])
  const hasChannels = computed(() => channels.value.length > 0)

  const showCreateList = ref<boolean>(false)
  const showBlockLists = ref<boolean>(false)


  return {
    showCreateList,
    showBlockLists,
    channels,
    hasChannels
  }
}

/**
 * Composables for managing blocked keywords in the settings.
 * It provides functionality to add, remove, and manage blocked keywords.
 */
export function useBlockedKeywords() {
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
}

export function useBlockLists() {}
