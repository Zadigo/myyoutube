<template>
  <div class="card shadow-none">
    <div class="card-body">
      <div class="d-flex justify-content-start align-items-start gap-4">
        <img src="/avatar3.png" width="60" height="60" class="img-fluid rounded-circle" alt="">
        <div class="actions" style="width: 100%;">
          <v-textarea v-model="requestData.content" label="" variant="solo-filled" clearable flat />
          
          <div class="d-flex gap-2">
            <v-btn color="secondary" size="small" rounded="xl" flat>
              Cancel
            </v-btn>

            <emoji-picker @emoji-click="hanlePickEmoji" />

            <v-btn color="secondary" size="small" rounded="xl" flat @click="handleCreateComment ">
              <font-awesome-icon icon="fas fa-comment" class="me-2" />
              Comment
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { VideoComment } from '@/types/comments'

import EmojiPicker from '@/components/emojis/EmojiPicker.vue'

export default defineComponent({
  name: 'UserCommentActions',
  components: {
    EmojiPicker
  },
  emits: {
    'new-comment' (_comment: VideoComment) {
      return true
    }
  },
  setup () {
    const requestData = ref({ content: '' })
    return { requestData }
  },
  methods: {
    /**
     * Creates a new comment for the video that
     * the user is currently viewing
     */
    async handleCreateComment  () {
      try {
        const videoID = this.$route.params.id
        const response = await this.$client.post<VideoComment>(`/videos/${videoID}/comment`, this.requestData)
        this.requestData.content = ''
        this.$emit('new-comment', response.data)
      } catch {
        // Handle error
      }
    },
    /**
     * Adds an emoji selected by the user to the text of the 
     * text area field
     */
    hanlePickEmoji (emoji: string) {
      this.requestData.content = this.requestData.content + emoji
    }
  }
})
</script>
