<template>
  <div class="card">
    <div class="card-body">
      <div class="d-flex align-items-center justify-content-between">
        <h2 v-if="comments" class="h4 m-0">
          {{ comments.length }} comments
        </h2>

        <v-menu>
          <template #activator="{ props }">
            <v-btn v-bind="props" rounded="xl" color="primary" flat>
              <font-awesome icon="sort" class="me-3" />
              Sort
            </v-btn>
          </template>

          <v-list>
            <v-list-item v-for="sortAction in sortActions" :key="sortAction" @click="() => handleSortComments(sortAction)">
              <v-list-item-title>
                {{ sortAction }}
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    </div>

    <hr class="text-body-tertiary">

    <!-- Actions -->
    <VideoUserCommentActions @new-comment="handleNewComment" />

    <!-- Comments -->
    <transition-group id="comments" tag="div">
      <VideoUserComment v-for="comment in comments" :key="comment.id" :comment="comment" />
    </transition-group>
  </div>
</template>

<script setup lang="ts">
import type { ExtendedRouteParamsGeneric, VideoComment } from '~/apps/types'

const sortActions = [
  'Newest',
  'Oldest'
] as const

type SortActions = (typeof sortActions)[number]

const { id: videoId } = useRoute().params as ExtendedRouteParamsGeneric

const queryParams = ref<{ desc: boolean }>({ desc: true })

/**
 * Get all the comments for the current video
 * in a delayed manner for performance optimization
 */
const { data: comments, refresh } = useAsyncData(async () => {
  return await $fetch<VideoComment[]>(`/api/v1/comments/${videoId}`, {
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    params: queryParams.value,
    onRequestError() {

    }
  })
})

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
 */
async function handleNewComment (comment: VideoComment) {
  if (comments.value) {
    comments.value.unshift(comment)
  }
}

/**
 * 
 */
async function handleSortComments (method: SortActions) {
  if (method === 'Newest') {
    queryParams.value.desc = true
  }
    
  if (method === 'Oldest') {
    queryParams.value.desc = false
  }

  refresh()
}
</script>
