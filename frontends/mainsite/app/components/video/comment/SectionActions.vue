<template>
  <volt-card class="shadow-none">
    <template #content>
      <div class="flex justify-start items-start gap-4">
        <volt-avatar image="/avatars/avatar3.png" shape="circle" size="large" alt="" />

        <div class="w-full space-y-3">
          <volt-textarea v-model="requestData.content" class="w-full" auto-resize label="" :style="{ resize: 'none' }" />
          
          <div class="flex gap-2 w-full">
            <volt-button variant="info" size="small" rounded>
              Cancel
            </volt-button>

            <!-- <EmojisPicker @emoji-click="hanlePickEmoji" /> -->

            <volt-button variant="info" size="small" rounded @click="handleCreateComment ">
              <icon name="i-fa7-solid:comment" />
              Comment
            </volt-button>
          </div>
        </div>
      </div>
    </template>
  </volt-card>
</template>

<script lang="ts" setup>
import type { VideoComment } from '~/types'

const emit = defineEmits<{ 'new-comment': [comment: VideoComment] }>()

const { $client } = useNuxtApp()
const route = useRoute()
const requestData = ref({ content: '' })

// Creates a new comment for the video that
// the user is currently viewing
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

// Adds an emoji selected by the user to the text of the 
// text area field
function hanlePickEmoji (emoji: string) {
  requestData.value.content = requestData.value.content + emoji
}
</script>
