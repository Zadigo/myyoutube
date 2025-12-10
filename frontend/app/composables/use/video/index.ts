import type { MenuItem } from 'primevue/menuitem'
import type { SubscriptionModes } from '~/data'
import type { BaseVideo, Nullable, Refeable, Undefineable } from '~/types'

export * from './modals'

/**
 * Composable for managing video rating state
 * @param video Reactive reference to the video information
 */
export function useVideoRating(video: Refeable<Undefineable<BaseVideo>>) {
  const [liked, like] = useToggle(false)
  const [unliked, dislike] = useToggle(false)
  
  // $fetch(`/v1/fake-endpoint/${video.value?.video_id}`, {
  //   baseURL: useRuntimeConfig().public.djangoProdUrl,
  //   watch: [liked, unliked],
  //   body: {
  //     liked: liked.value,
  //     unliked: unliked.value
  //   },
  //   onRequestError({ response }) {
  //     if (response && response.status === 401) {
  //       refreshAccessTokenClient()
  //     }
  //   }
  // })

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
export function useVideoSubscription(video: Refeable<Undefineable<BaseVideo>>) {
  const [active, subscribe] = useToggle()
  const mode = ref<Nullable<SubscriptionModes>>(null)

  watch(active, (newValue) => {
    if (!newValue) {
      mode.value = null
    }
  })

  const subscribeMenuItems: MenuItem[] = [
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

  // useFetch(`/v1/fake-endpoint/${video.value?.video_id}`, {
  //   baseURL: useRuntimeConfig().public.djangoProdUrl,
  //   watch: [active, mode],
  //   body: {
  //     subscribe: active.value,
  //     mode: mode.value
  //   },
  //   onRequestError({ response }) {
  //     if (response && response.status === 401) {
  //       refreshAccessTokenClient()
  //     }
  //   }
  // })

  return {
    active,
    mode,
    subscribeMenuItems,
    subscribe
  }
}
