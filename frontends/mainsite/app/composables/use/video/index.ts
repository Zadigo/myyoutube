import type { DropdownMenuItem } from '@nuxt/ui'

export * from './modals'

/**
 * Composable for managing video rating state
 * @param video Reactive reference to the video information
 */
export function useVideoRatingComposable(_video: Undefineable<Refeable<Undefineable<VideoDetails>>>) {
  const [liked, like] = useToggle(false)
  const [unliked, dislike] = useToggle(false)

  return {
    /**
     * Reactive property indicating if the video is liked
     */
    liked,
    /**
     * Reactive property indicating if the video is liked
     */
    unliked,
    /**
     * Function to like the video
     */
    like,
    /**
     * Function to dislike the video
     */
    dislike
  }
}

/**
 * Composable for managing video subscription state
 * @param video Reactive reference to the video information
 */
export function useVideoSubscriptionComposable(_video: Undefineable<Refeable<Undefineable<VideoDetails>>>) {
  const [active, subscribe] = useToggle()
  const mode = ref<Nullable<SubscriptionModes>>(null)

  watch(active, (newValue) => {
    if (!newValue) {
      mode.value = null
    }
  })

  const subscribeMenuItems: DropdownMenuItem[] = [
    {
      label: 'All',
      icon: 'i-lucide-bullhorn',
      command: () => {
        mode.value = 'All'
      }
    },
    {
      label: 'None',
      icon: 'i-lucide-bell-slash',
      command: () => {
        mode.value = null
      }
    },
    {
      label: 'Unsubscribe',
      icon: 'i-lucide-user-minus',
      command: () => {
        mode.value = 'None'
        active.value = false
      }
    }
  ]
  
  return {
    active,
    mode,
    subscribeMenuItems,
    subscribe
  }
}
