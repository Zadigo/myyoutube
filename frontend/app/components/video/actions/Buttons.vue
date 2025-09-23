<template>
  <div class="flex items-center justify-left">
    <volt-button size="large" color="primary" class="me-1" rounded @click="() => { like() }">
      <icon v-if="liked" name="i-fa7-solid:thumbs-up" class="mr-2" />
      <icon v-else name="i-fa7-regular:thumbs-up" class="mr-2" />
      Like <span class="font-bold">145.3k</span>
    </volt-button>

    <volt-button size="large" color="primary" class="me-3" rounded @click="() => { dislike() }">
      <icon v-if="unliked" name="i-fa7-solid:thumbs-down" class="mr-2" />
      <icon v-else name="i-fa7-regular:thumbs-down" class="mr-2" />
      Dislike <span class="font-bold">15</span>
    </volt-button>
    
    <!-- Extra Actions -->
    <volt-dropdown-button id="more-actions" :items="menuItems">
      <icon name="i-lucide-ellipsis-vertical" />
    </volt-dropdown-button>

    <volt-dropdown-button v-if="active" id="more-actions" :items="subscribeMenuItems" rounded>
      <icon name="i-lucide-bell-off" />
    </volt-dropdown-button>

    <volt-button v-else size="large" color="light" class="ml-5" @click="() => { subscribe() }">
      <icon name="i-lucide-bell" />
    </volt-button>
  </div>
</template>

<script lang="ts" setup>
import { useVideoRating, useVideoSubscription } from '~/composables/use'

import type { DefaultVideoMenuActions } from '~/data'
import type { BaseVideo, VideoMenuItem } from '~/types'

const emit = defineEmits<{ action: [method: DefaultVideoMenuActions] }>()

const { id } = useRoute().params as { id: string }
const router = useRouter()

const menuItems: VideoMenuItem[] = [
  {
    label: 'Store',
    icon: 'i-lucide-store'
  },
  {
    label: 'Download',
    icon: 'i-lucide-download',
    command: () => emit('action', 'Download')
  },
  {
    label: 'Save',
    icon: 'i-lucide-save',
    command: () => emit('action', 'Save')
  },
  {
    label: 'Gift',
    icon: 'i-lucide-gift',
    command: () => emit('action', 'Gift')
  },
  {
    label: 'Donate',
    icon: 'i-lucide-dollar-sign',
    command: () => emit('action', 'Donate')
  },
  {
    label: 'Share',
    icon: 'i-lucide-share',
    command: () => emit('action', 'Share')
  },
  {
    label: 'Recommendations',
    icon: 'i-lucide-star',
    command: () => emit('action', 'Recommendations')
  },
  {
    label: 'Classify',
    icon: 'i-lucide-clipboard-list',
    command: () => emit('action', 'Classify')
  },
  {
    label: 'Community note',
    icon: 'i-lucide-note-sticky',
    command: () => emit('action', 'Community note')
  },
  {
    label: 'Fact check',
    icon: 'i-lucide-shield-alert',
    command: () => {
      router.push(`/fact-checking?v=${id}`)
    }
  },
  {
    label: 'Report',
    icon: 'i-lucide-store',
    command: () => emit('action', 'Report')
  }
]

const currentVideo = inject<Ref<BaseVideo>>('currentVideo')
const { like, dislike, liked, unliked } = useVideoRating(currentVideo)
const { subscribe, active, mode, subscribeMenuItems } = useVideoSubscription(currentVideo)
</script>
