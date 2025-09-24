import type { ApiResponse, VideoComment } from "~/types"

export const sortActions = [
  'Newest',
  'Oldest',
  'Most popular',
  'Least popular'
] as const

export type SortActions = (typeof sortActions)[number]

export type SortActionsMenuItem = {
  label: SortActions
}

/**
 * Composable to handle comments fetching and sorting
 */
export async function useCommentsComposable() {
  const comments = ref<VideoComment[]>([])
  const queryParams = ref({
    desc: true,
    limit: 20,
    offset: 0
  })

  const { data, refresh } = await useFetch<ApiResponse<VideoComment>>('/api/comments', {
    method: 'GET',
    immediate: true,
    query: queryParams.value
  })
  
  if (isDefined(data)) {
    comments.value = data.value.results
  }

  const pinnedComments = computed(() => {
    if (comments.value) {
      return comments.value.filter(x => x.pinned === true)
    } else {
      return []
    }
  })

  const unpinnedComments = computed(() => {
    if (comments.value) {
      return comments.value.filter(x => x.pinned === false)
    } else {
      return []
    }
  })

  /**
   * Sorting
   */

  async function sortCommentsBy(method: SortActions) {
    if (method === 'Newest') {
      queryParams.value.desc = true
    }

    if (method === 'Oldest') {
      queryParams.value.desc = false
    }
  }

  watchDebounced(queryParams, () => {
    refresh()
  }, {
    immediate: false,
    debounce: 300
  })

  return {
    /**
     * All comments
     */
    comments,
    /**
     * Pinned comments
     */
    pinnedComments,
    /**
     * Unpinned comments
     */
    unpinnedComments,
    /**
     * Method to sort comments by
     */
    sortCommentsBy
  }
}

/**
 * Composable to handle comment creation
 * and replying to comments
 */
export function useCreateCommentComposable() {
  const newComment = ref('')

  async function create() {
    if (isDefined(newComment)) {
      $fetch('/api/comments', {
        method: 'POST',
        body: {
          content: newComment.value
        }
      })
    }
  }

  async function reply() {
    if (isDefined(newComment)) {
      $fetch('/api/comments', {
        method: 'POST',
        body: {
          content: newComment.value
        }
      })
    }
  }
  
  return {
    newComment,
    create,
    /**
     * Specific case where a user replies to a
     * specific given comment
     */
    reply
  }
}
