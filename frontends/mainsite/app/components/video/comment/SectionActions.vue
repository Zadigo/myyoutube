<template>
  <u-card class="shadow-none">
    <div class="flex justify-start items-start gap-4">
      <u-avatar src="/avatars/avatar3.png" size="lg" alt="" />

      <div class="w-full space-y-3">
        <u-textarea v-model="requestData.content" class="w-full" auto-resize label="" :style="{ resize: 'none' }" />
        
        <div class="flex gap-2 w-full">
          <u-button variant="subtle" size="md" rounded>
            Cancel
          </u-button>

          <!-- <EmojisPicker @emoji-click="hanlePickEmoji" /> -->

          <u-button variant="subtle" size="md" rounded @click="handleCreateComment ">
            <icon name="i-fa7-solid:comment" />
            Comment
          </u-button>
        </div>
      </div>
    </div>
  </u-card>
</template>

<script lang="ts" setup>

const emit = defineEmits<{ 'new-comment': [comment: BaseComment] }>()

const route = useRoute()
const requestData = ref({ content: '' })

// Creates a new comment for the video that
// the user is currently viewing
async function handleCreateComment () {
  try {
    const videoID = route.params.id
    const response = await $fetch<BaseComment>(`/api/videos/${videoID}/comment`, {
      method: 'POST',
      body: requestData.value
    })
    
    requestData.value.content = ''

    emit('new-comment', response)
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
