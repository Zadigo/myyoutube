import type { Arrayable, Nullable, Undefineable, VideoTechnicalDetails} from '~/types'

export type VideoPlayerEl = Ref<Nullable<HTMLVideoElement>>

const [useVideoPlayer, _useVideoPlayerStore] = createInjectionState((el: VideoPlayerEl, videoSource: Undefineable<string>) => {
  const hasPlayer = computed(() => isDefined(el) && isDefined(el.value) && isDefined(videoSource))

  tryOnBeforeUnmount(() => {
    if (isDefined(el)) {
      const source = el.value.querySelector('source')

      if (source) {
        URL.revokeObjectURL(source.src)
      }
    }
  })

  return {
    /**
     * Reference to the HTMLVideoElement
     * @default undefined
     */
    el,
    /**
     * Indicates if the Video Player is Ready to be used
     * @default false
     */
    hasPlayer
  }
})

export { useVideoPlayer }

export function useVideoPlayerStore() {
  const store = _useVideoPlayerStore()
  if (!store) throw new Error('useVideoPlayerStore must be used after useVideoPlayer')
  return store
}

/**
 * Formats a time value in seconds to a string in the format HH:MM:SS or MM:SS
 * @param value - The time value in seconds
 */
function formatTime(value: number) {
  const hours = Math.floor(value / 3600)
  const minutes = Math.floor((value % 3600) / 60)
  const seconds = Math.floor(value % 60)

  const formattedHours = hours < 10 ? '0' + hours : hours
  const formattedMinutes = minutes < 10 ? '0' + minutes : minutes
  const formattedSeconds = seconds < 10 ? '0' + seconds : seconds

  if (hours > 0) {
    return `${formattedHours}:${formattedMinutes}:${formattedSeconds}`
  } else {
    return `${formattedMinutes}:${formattedSeconds}`
  }
}

/**
 * Composable that provides videolayer controls and statistics
 * @param videoPlayerEl - Reference to the HTMLVideoElement
 */
export const useVideoPlayerControls = createGlobalState((videoPlayerEl: VideoPlayerEl) => {
  const [isLoading, toggleLoading] = useToggle<boolean>(true)
  const [isPlaying, togglePlaying] = useToggle<boolean>(false)

  // Tracks the amount of the times the button play was 
  // pressed during a viewing session
  const { count: numberOfPlays, inc } = useCounter()

  async function handlePlayPause(_e: Event, callback?: (isPlaying: boolean) => void) {
    togglePlaying()
    
    if (isDefined(videoPlayerEl)) {
      if (videoPlayerEl.value.paused) {
        inc()
        togglePlaying(true)
        videoPlayerEl.value.play()
      } else {
        togglePlaying(false)
        videoPlayerEl.value.pause()
      }
    }

    if (callback) callback(isPlaying.value)
  }

  /**
   * Duration & Current Time
   */

  const duration = ref<number>(0)
  const currentTime = ref<number>(0)
  
  const currentTimeFormatted = computed(() => formatTime(currentTime.value))
  const durationFormatted = computed(() => formatTime(duration.value))
  
  // Indicates that the current time is equals the total video duration time
  const isEnded = computed(() => currentTimeFormatted.value === durationFormatted.value)
  
  watchOnce(isEnded, () => {
    isPlaying.value = false
    // emit('update:metadata', playingStatistics.value)
  })
  
  const wasPlayed = ref<boolean>(false)
  watchOnce(() => numberOfPlays.value === 1, () => {
    wasPlayed.value = true
  })

  // Calculates the current completion of the video in percentage of the total duration
  const completionPercentage = computed(() => Math.floor((currentTime.value / duration.value) * 100))

  const playingStatistics = computed((): VideoTechnicalDetails => {
    return {
      currentTime: currentTime.value,
      duration: duration.value,
      formattedCurrentTime: currentTimeFormatted.value,
      percentagePlayed: completionPercentage.value,
      wasPlayed: wasPlayed.value,
      playPauseCount: numberOfPlays.value
    }
  })

  function handleVideoMetadata(_e: Event, callback?: () => void) {
    if (isDefined(videoPlayerEl)) {
      if (!isPlaying.value && !Number.isNaN(videoPlayerEl.value.duration)) duration.value = videoPlayerEl.value.duration
      currentTime.value = videoPlayerEl.value.currentTime
      
      if (callback) callback()
      // emit('update:metadata', playingStatistics.value)
    }
  }

  function handleCanPlay(_e: Event) {
    toggleLoading(false)
  }

  /**
   * Keyboard Controls
   */

  // const { space } = useMagicKeys()

  // watch(space, (isPressed) => {
  //   if (isPressed) {
  //     handlePlayPause(new Event('keyboard'))
  //   }
  // })

  /**
   * Reset
   */
  tryOnUnmounted(() => {
    duration.value = 0
    currentTime.value = 0
    isPlaying.value = false
    isLoading.value = true
    wasPlayed.value = false
  })

  return {
    /**
     * Total Duration of the Video in Seconds
     * @default 0
     */
    duration,
    /**
     * Total Duration of the Video Formatted as HH:MM:SS or MM:SS
     * @default "00:00"
     */
    durationFormatted,
    /**
     * Current Time of the Video in Seconds
     * @default 0
     */
    currentTime,
    /**
     * Current Time of the Video Formatted as HH:MM:SS or MM:SS
     * @default "00:00"
     */
    currentTimeFormatted,
    /**
     * Indicates if the Video has Ended
     * @default false
     */
    isEnded,
    /**
     * Completion Percentage of the Video
     * @default 0
     */
    completionPercentage,
    /**
     * Indicates if the Video was Played at least once
     * @default false
     */
    wasPlayed,
    /**
     * Number of times the Play/Pause button was pressed
     * @default 0
     */
    numberOfPlays,
    /**
     * Indicates if the Video is Loading
     * @default true
     */
    isLoading,
    /**
     * Indicates if the Video is Playing
     * @default false
     */
    isPlaying,
    /**
     * Video Playing Statistics
     * @default {}
     */
    playingStatistics,
    /**
     * Handles the 'canplay' event of the video element
     */
    handleCanPlay,
    /**
     * Toggles the Loading State
     */
    toggleLoading,
    /**
     * Toggles the Playing State
     */
    togglePlaying,
    /**
     * Handles the Play/Pause functionality of the video
     */
    handlePlayPause,
    /**
     * Handles the 'loadedmetadata' and 'timeupdate' events of the video element
     */
    handleVideoMetadata
  }
})

type Speeds = 2 | 1.75 | 1.5 | 1 | 0.75 | 0.5

/**
 * Composable that provides video player options such as speed, quality, and volume
 * @param videoPlayerEl - Reference to the HTMLVideoElement
 */
export function useVideoPlayerOptions(videoPlayerEl: VideoPlayerEl) {
  const speeds: Arrayable<Speeds> = [2, 1.75, 1.5, 1, 0.75, 0.5]

  const speed = ref<string>('1x')
  const quality = ref<string>('1080p')
  const volume = ref<number>(0.5)

  watch(speed, (newSpeed) => {
    if (isDefined(videoPlayerEl)) {
      videoPlayerEl.value.playbackRate = parseFloat(newSpeed)
    }
  })

  watch(volume, (newVolume) => {
    if (isDefined(videoPlayerEl)) {
      videoPlayerEl.value.volume = newVolume
    }
  })

  watch(quality, (newQuality) => {
    if (isDefined(videoPlayerEl)) {
      // Implement quality change logic here
    }
  })

  /**
   * Modals
   */

  return {
    /**
     * Available Playback Speeds
     */
    speeds,
    /**
     * Selected Playback Speed
     * @default "1x"
     */
    speed,
    /**
     * Selected Video Quality
     * @default "1080p"
     */
    quality,
    /**
     * Selected Volume Level
     * @default 0.5
     */
    volume
  }

}
