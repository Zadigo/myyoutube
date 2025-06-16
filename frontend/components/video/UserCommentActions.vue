<template>
  <div class="card shadow-none">
    <div class="card-body">
      <div class="d-flex justify-content-start align-items-start gap-4">
        <img src="/avatar3.png" width="60" height="60" class="img-fluid rounded-circle" alt="">
        <div class="actions" style="width: 100%;">
          <v-textarea v-model="requestData.content" label=""  clearable flat />
          
          <div class="d-flex gap-2">
            <v-btn color="secondary" size="small" rounded="xl" flat>
              Cancel
            </v-btn>

            <EmojisPicker @emoji-click="hanlePickEmoji" />

            <v-btn color="secondary" size="small" rounded="xl" flat @click="handleCreateComment ">
              <font-awesome icon="fas fa-comment" class="me-2" />
              Comment
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import type { VideoComment } from '~/types'

const emit = defineEmits({
  'new-comment' (_comment: VideoComment) {
    return true
  }
})

const { $client } = useNuxtApp()
const route = useRoute()
const requestData = ref({ content: '' })

/**
 * Creates a new comment for the video that
 * the user is currently viewing
 */
async function handleCreateComment () {
  try {
    const videoID = route.params.id
    const response = await $client.post<VideoComment>(`/videos/${videoID}/comment`, requestData.value)
    requestData.value.content = ''
    emit('new-comment', response.data)
  } catch {
    // Handle error
  }
}

/**
 * Adds an emoji selected by the user to the text of the 
 * text area field
 */
function hanlePickEmoji (emoji: string) {
  requestData.value.content = requestData.value.content + emoji
}
</script>
