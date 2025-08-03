<template>
  <div class="flex items-center justify-left">
    <VoltButton size="large" color="primary" class="me-1" rounded @click="like">
      <Icon v-if="liked" name="i-fa7-solid:thumbs-up" class="mr-2" />
      <Icon v-else name="i-fa7-regular:thumbs-up" class="mr-2" />
      Like <span class="font-bold">145.3k</span>
    </VoltButton>

    <VoltButton size="large" color="primary" class="me-3" rounded @click="dislike">
      <Icon v-if="unliked" name="i-fa7-solid:thumbs-down" class="mr-2" />
      <Icon v-else name="i-fa7-regular:thumbs-down" class="mr-2" />
      Dislike <span class="font-bold">15</span>
    </VoltButton>
    
    <!-- Extra Actions -->
    <VoltDropdownButton id="more-actions" :items="menuItems">
      <Icon name="i-fa7-solid:ellipsis-h" />
    </VoltDropdownButton>

    <VoltDropdownButton v-if="active" id="more-actions" :items="subscribeMenuItems" rounded>
      <Icon name="i-fa7-solid:bell-slash" />
    </VoltDropdownButton>

    <VoltButton v-else size="large" color="light" class="ml-5" @click="subscribe">
      Subscribe
    </VoltButton>
  </div>
</template>

<script lang="ts" setup>
import { useVideoRating, useVideoSubscription } from '~/composables/use'

import type { DefaultVideoMenuActions } from '~/data'
import type { VideoInfo, VideoMenuItem } from '~/types'

const emit = defineEmits<{ action: [method: DefaultVideoMenuActions] }>()

const { id } = useRoute().params as { id: string }
const router = useRouter()

const menuItems: VideoMenuItem[] = [
  {
    label: 'Store',
    icon: 'i-fa7-solid:store'
  },
  {
    label: 'Download',
    icon: 'i-fa7-solid:download',
    command: () => emit('action', 'Download')
  },
  {
    label: 'Save',
    icon: 'i-fa7-solid:save',
    command: () => emit('action', 'Save')
  },
  {
    label: 'Gift',
    icon: 'i-fa7-solid:gift',
    command: () => emit('action', 'Gift')
  },
  {
    label: 'Donate',
    icon: 'i-fa7-solid:dollar-sign',
    command: () => emit('action', 'Donate')
  },
  {
    label: 'Share',
    icon: 'i-fa7-solid:share',
    command: () => emit('action', 'Share')
  },
  {
    label: 'Recommendations',
    icon: 'i-fa7-solid:star',
    command: () => emit('action', 'Recommendations')
  },
  {
    label: 'Classify',
    icon: 'i-fa7-solid:clipboard-list',
    command: () => emit('action', 'Classify')
  },
  {
    label: 'Community note',
    icon: 'i-fa7-solid:note-sticky',
    command: () => emit('action', 'Community note')
  },
  {
    label: 'Fact check',
    icon: 'i-fa7-solid:building-shield',
    command: () => {
      router.push(`/fact-checking?v=${id}`)
    }
  },
  {
    label: 'Report',
    icon: 'i-fa7-solid:store',
    command: () => emit('action', 'Report')
  }
]

const currentVideo = inject<Ref<VideoInfo>>('currentVideo')
const { like, dislike, liked, unliked } = useVideoRating(currentVideo)
const { subscribe, active, mode, subscribeMenuItems } = useVideoSubscription(currentVideo)
</script>
