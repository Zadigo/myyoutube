<template>
  <div class="card">
    <div class="card-body">
      <div class="d-flex align-items-center justify-content-between">
        <h2 class="h4 m-0">
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
            <v-list-item v-for="sortAction in sortActions" :key="sortAction" @click="handleSortComments(sortAction)">
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

<script lang="ts">
import { computed, defineComponent, ref } from 'vue'

import type { VideoComment } from '~/types'

import UserComment from './UserComment.vue'
import UserCommentActions from './UserCommentActions.vue'
import { VideoUserComment, VideoUserCommentActions } from '#build/components'

const sortActions: [ 'Newest', 'Oldest' ] = [
  'Newest',
  'Oldest'
]

export default defineComponent({
  name: 'AsyncCommentSection',
  components: {
    UserComment,
    UserCommentActions
  },
  async setup () {
    const { $client } = useNuxtApp()
    const route = useRoute()
    const comments = ref<VideoComment[]>([])
    const queryParams = ref({ desc: true })
    
    // Get all the comments for the current video
    // in a delayed manner for performance optimization
    async function requestVideoComments () {
      try {
        const videoID = route.params.id
        const response = await $client.get<VideoComment[]>(`/comments/${videoID}`, {
          params: queryParams.value
        })
        comments.value = response.data
      } catch (e) {
        console.log(e)
      }
    }
    await requestVideoComments()

    const pinnedComments = computed(() => {
      // return _.filter(comments.value, { pinned: true })
      return comments.value.filter(x => x.pinned === true)
    })

    const unpinnedComments = computed(() => {
      // return _.filter(comments.value, { pinned: false })
      return comments.value.filter(x => x.pinned === false)
    })

    return {
      comments,
      pinnedComments,
      unpinnedComments,
      queryParams,
      sortActions,
      requestVideoComments
    }
  },
  methods: {
    /**
     * Append the newly created comment by implementing it
     * at the start of the current comment list
     */
    async handleNewComment (comment: VideoComment) {
      this.comments.unshift(comment)
    },
    /**
     * 
     */
    async handleSortComments (method: 'Newest' | 'Oldest') {
      if (method === 'Newest') {
        this.queryParams.desc = true
      }
        
      if (method === 'Oldest') {
        this.queryParams.desc = false
      }

      await this.requestVideoComments()
    }
  }
})
</script>
