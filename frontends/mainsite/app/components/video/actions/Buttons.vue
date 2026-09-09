<template>
  <div class="flex items-center justify-left">
    <u-button class="me-1" size="xl" @click="() => { like() }">
      <icon v-if="liked" name="i-fa7-solid:thumbs-up" class="mr-2" />
      <icon v-else name="i-fa7-regular:thumbs-up" class="mr-2" />
      Like <span class="font-bold">145.3k</span>
    </u-button>

    <u-button class="me-3" size="xl" @click="() => { dislike() }">
      <icon v-if="unliked" name="i-fa7-solid:thumbs-down" class="mr-2" />
      <icon v-else name="i-fa7-regular:thumbs-down" class="mr-2" />
      Dislike <span class="font-bold">15</span>
    </u-button>
    
    <!-- Extra Actions -->
    <volt-dropdown id="more-actions" :items="menuItems">
      <template #default="{ attrs }">
        <u-button size="xl" @click="attrs.toggle">
          <icon name="i-lucide-ellipsis-vertical" />
        </u-button>
      </template>
    </volt-dropdown>

    <volt-dropdown v-if="active" id="more-actions" size="xl" :items="subscribeMenuItems" rounded>
      <template #default="{ attrs }">
        <u-button size="xl" @click="attrs.toggle">
          <icon name="i-lucide-bell-off" />
        </u-button>
      </template>
    </volt-dropdown>

    <u-button v-else size="xl" color="neutral" class="ml-5" @click="() => { subscribe() }">
      <icon name="i-lucide-bell" />
    </u-button>
  </div>
</template>

<script lang="ts" setup>

import type { VideoMenuItem } from '~/types'

const emit = defineEmits<{ 'action:modal': [method: DefaultVideoMenuActions] }>()

const { id } = useRoute().params as { id: string }
const router = useRouter()

const menuItems: VideoMenuItem[] = [
  {
    label: 'Store',
    icon: 'i-lucide-store'
  },
  {
    label: 'Download',
    icon: 'i-lucide:download',
    command: () => emit('action:modal', 'Download')
  },
  {
    label: 'Save',
    icon: 'i-lucide-save',
    command: () => emit('action:modal', 'Save')
  },
  {
    label: 'Gift',
    icon: 'i-lucide-gift',
    command: () => emit('action:modal', 'Gift')
  },
  {
    label: 'Donate',
    icon: 'i-lucide-dollar-sign',
    command: () => emit('action:modal', 'Donate')
  },
  {
    label: 'Share',
    icon: 'i-lucide-share',
    command: () => emit('action:modal', 'Share')
  },
  {
    label: 'Recommendations',
    icon: 'i-lucide-star',
    command: () => emit('action:modal', 'Recommendations')
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
    command: () => emit('action:modal', 'Report')
  }
]

const currentVideo = injectLocal<Ref<VideoDetails>>(CURRENT_VIDEO_SYMBOL)

/**
 * Rating
 */

const { like, dislike, liked, unliked } = useVideoRating(currentVideo)

/**
 * Subscription
 */
const { subscribe, active, mode, subscribeMenuItems } = useVideoSubscription(currentVideo)
</script>
