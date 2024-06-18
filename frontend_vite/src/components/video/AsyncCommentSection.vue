<template>
  <div class="card">
    <div class="card-body">
      <div class="d-flex align-items-center justify-content-between">
        <h2 class="h4 m-0">{{ comments.length }} comments</h2>

        <v-menu>
          <template #activator="{ props }">
            <v-btn v-bind="props" rounded="xl" color="primary" flat>
              <font-awesome-icon :icon="['fas', 'fa-sort']" class="me-3" />
              Sort
            </v-btn>
          </template>

          <v-list>
            <v-list-item v-for="sortAction in sortActions" :key="sortAction">
              <v-list-item-title>{{ sortAction }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    </div>

    <hr class="text-body-tertiary" />

    <!-- Actions -->
    <user-comment-actions @new-comment="handleNewComment" />

    <!-- Comments -->
    <transition-group id="comments" tag="div">
      <user-comment v-for="comment in comments" :key="comment.id" :comment="comment" />
    </transition-group>
  </div>
</template>

<script>
import _ from 'lodash'
import { computed, ref } from 'vue'
import { useRoute } from 'vue-router'
import { client } from 'src/plugins/axios'
import UserComment from './UserComment.vue'
import UserCommentActions from './UserCommentActions.vue'

const sortActions = [
  'Newest',
  'Oldest'
]


export default {
  name: 'AsyncCommentSection',
  components: {
    UserComment,
    UserCommentActions
  },
  async setup () {
    const route = useRoute()
    const comments = ref([])
    
    async function requestVideoComments () {
      // Get all the comments for the current video
      // in a delayed manner for performance optimization
      try {
        const videoID = route.params.id
        const response = await client.get(`/comments/${videoID}`)
        comments.value = response.data
      } catch (e) {
        console.log(e)
      }
    }
    await requestVideoComments()

    const pinnedComments = computed(() => {
      return _.filter(comments.value, { pinned: true })
    })

    const unpinnedComments = computed(() => {
      return _.filter(comments.value, { pinned: false })
    })

    return {
      comments,
      pinnedComments,
      unpinnedComments,
      sortActions
    }
  },
  methods: {
    async handleNewComment (comment) {
      // Append the newly created comment by implementing it
      // at the start of the current comment list
      this.comments.unshift(comment)
    }
  }
}
</script>
