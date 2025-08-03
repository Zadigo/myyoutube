<template>
  <VoltCard>
    <template #content>
      <div class="flex items-center justify-between">
        <h2 v-if="comments" class="h4 m-0">
          {{ comments.length }} comments
        </h2>

        <VoltDropdownButton id="comment-sorting" :items="sortActionsMenuItem">
          Sort by
        </VoltDropdownButton>
      </div>

      <VoltDivider class="my-3" />

      <!-- Actions -->
      <VideoCommentSectionActions @new-comment="handleNewComment" />

      <VoltDivider class="my-5" />

      <!-- Comments -->
      <VideoCommentCardItem v-for="comment in pinnedComments" :key="comment.id" :comment="comment" />
      <VideoCommentCardItem v-for="comment in unpinnedComments" :key="comment.id" :comment="comment" />
    </template>
  </VoltCard>
</template>

<script setup lang="ts">
import { commentsFixture } from '~/data/fixtures'
import type { ExtendedRouteParamsGeneric, VideoComment } from '~/types'

const sortActions = [
  'Newest',
  'Oldest',
  'Most popular',
  'Least popular'
] as const

type SortActions = (typeof sortActions)[number]

type SortActionsMenuItem = {
  label: SortActions
}

const { id: videoId } = useRoute().params as ExtendedRouteParamsGeneric

const queryParams = ref<{ desc: boolean }>({ desc: true })

/**
 * Get all the comments for the current video
 * in a delayed manner for performance optimization
 * @todo - Reimplemnt
 */
// const { data: comments, refresh } = useAsyncData<VideoComment[]>(async () => {
//   return await $fetch<VideoComment[]>(`/v1/comments/${videoId}`, {
//     baseURL: useRuntimeConfig().public.djangoProdUrl,
//     params: queryParams.value
//   })
// })

const comments = ref<VideoComment[]>(commentsFixture)

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
 * Append the newly created comment by implementing it
 * at the start of the current comment list
 * @todo - Send to backend
 */
async function handleNewComment (comment: VideoComment) {
  if (comments.value) {
    comments.value.unshift(comment)
  }
}

/**
 * Handle sorting of comments
 * @todo - Reimplement
 */
async function handleSortComments (method: SortActions) {
  if (method === 'Newest') {
    queryParams.value.desc = true
  }
    
  if (method === 'Oldest') {
    queryParams.value.desc = false
  }

  // refresh()
}

const sortActionsMenuItem: SortActionsMenuItem[] = sortActions.map(action => ({ label: action, command: handleSortComments }))
</script>
