<template>
  <VoltCard class="shadow-none">
    <template #content>
      <div class="flex justify-start items-start gap-4">
        <VoltAvatar image="/avatars/avatar3.png" shape="circle" size="large" alt="" />

        <div class="actions" style="width: 100%;">
          <textarea v-model="requestData.content" label="" />
          
          <div class="flex gap-2">
            <VoltButton variant="info" size="small" rounded>
              Cancel
            </VoltButton>

            <!-- <EmojisPicker @emoji-click="hanlePickEmoji" /> -->

            <VoltButton variant="info" size="small" rounded @click="handleCreateComment ">
              <Icon name="i-fa7-solid:comment" />
              Comment
            </VoltButton>
          </div>
        </div>
      </div>
    </template>
  </VoltCard>
</template>

<script lang="ts" setup>
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
