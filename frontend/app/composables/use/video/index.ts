import type { MenuItem } from 'primevue/menuitem'
import type { SubscriptionModes } from '~/data'
import type { VideoInfo } from '~/types'

/**
 * Composable for managing video rating state
 * @param video Reactive reference to the video information
 */
export function useVideoRating(video: Ref<VideoInfo> | undefined) {
  const liked = ref<boolean>(false)
  const unliked = ref<boolean>(false)

  useFetch(`/v1/fake-endpoint/${video.value.video_id}`, {
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    watch: [liked, unliked],
    onRequestError({ response }) {
      if (response && response.status === 401) {
        refreshAccessTokenClient()
      }
    }
  })

  /**
   * 
   */
  async function like () {
    liked.value = !liked.value
    // await handleLikeDislike()
  }

  /**
   * 
   */
  async function dislike () {
    unliked.value = !unliked.value
    // await handleLikeDislike()
  }

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
export function useVideoSubscription(video: Ref<VideoInfo> | undefined) {
  const active = ref<boolean>(false)
  const mode = ref<SubscriptionModes | null>(null)

  watch(active, (newValue) => {
    if (!newValue) {
      mode.value = null
    }
  })

  const subscribeMenuItems: MenuItem[] = [
    {
      label: 'All',
      icon: 'i-fa7-solid:i-fa7-solid:bullhorn',
      command: () => {
        mode.value = 'All'
      }
    },
    {
      label: 'None',
      icon: 'i-fa7-solid:i-fa7-solid:bell-slash',
      command: () => {
        mode.value = null
      }
    },
    {
      label: 'Unsubscribe',
      icon: 'i-fa7-solid:i-fa7-solid:user-minus',
      command: () => {
        mode.value = 'None'
      }
    }
  ]

  useFetch(`/v1/fake-endpoint/${video.value.video_id}`, {
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    watch: [active, mode],
    onRequestError({ response }) {
      if (response && response.status === 401) {
        refreshAccessTokenClient()
      }
    }
  })

  async function subscribe() {
    active.value = !active.value
  }

  return {
    active,
    mode,
    subscribeMenuItems,
    /**
     * Function to toggle subscription status
     */
    subscribe
  }
}
