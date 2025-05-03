<template>
  <div ref="videoContainerEl" class="video-container">
    <video ref="videoPlayerEl" class="video-player" preload="metadata" controlist="nodownload" oncontextmenu="return false;" @loadedmetadata="getVideoDetails" @timeupdate="getVideoDetails" @canplay="isLoading=false" @click.stop="handlePlayPause">
      <source :src="videoSource" type="video/mp4">
    </video>

    <!-- Controls -->
    <VideoPlayerControls />
  </div>
</template>

<script setup lang="ts">
interface PlayingDetails {
  currentTime: number
  formattedCurrentTime: string
  wasPlayed: boolean
  percentagePlayed: number
  playPauseCount: number
}

defineProps({
  videoSource: {
    type: String,
    required: true
  }
})

const emit = defineEmits({
  'loaded-meta-data' () {
    return true
  },
  play () {
    return true
  },
  pause (_data:  PlayingDetails) {
    return true
  }
})

const speeds = [2, 1.75, 1.5, 1, 0.75, 0.5] as const

type Speeds  = (typeof speeds)[number]

// Tracks the amount of the times the
// button play was pressed during a
// viewing session
const { count, inc } = useCounter()

const isLoading = ref<boolean>(true)
const isPlaying = ref<boolean>(false)
const wasPlayed = ref<boolean>(false)

const duration = ref<number>(0)
const currentTime = ref<number>(0)
const volume = ref<number>(0.5)

const speed = ref<string>('1x')
const quality = ref<string>('1080p')

const videoContainerEl = useTemplateRef('videoContainerEl')
const videoPlayerEl = useTemplateRef('videoPlayerEl')

/**
 * Calculates the current completion of the
 * video in percentage on the total duration
 */
const completionPercentage = computed(() => {
  return Math.floor((currentTime.value / duration.value) * 100)
})

/**
 * Loads the metadata for the current
 * loaded video: duration, size etc.
 */
function getVideoDetails () {
  if (videoPlayerEl.value) {
    if (!Number.isNaN(videoPlayerEl.value.duration)) {
      duration.value = videoPlayerEl.value.duration
    }

    currentTime.value = videoPlayerEl.value.currentTime
  }
}

/**
 * Formats the time to a human readable
 * format for the user to track the
 * time at which the video is currently at
 * 
 * @param value The time value to format
 */
function formatTime (value: number) {
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

const playingDetails = computed((): PlayingDetails => {
  return {
    currentTime: currentTime.value,
    formattedCurrentTime: formatTime(currentTime.value),
    percentagePlayed: completionPercentage.value,
    wasPlayed: wasPlayed.value,
    playPauseCount: count.value
  }
})

const currentTimeFormatted = computed(() => {
  return formatTime(currentTime.value)
})

const durationFormatted = computed(() => {
  return formatTime(duration.value)
})

/**
 * Indicates that the viddeo has ended, in other
 * words that the current time is equals the total
 * video duration time
 */
const isEnded = computed(() => {
  return currentTimeFormatted.value === durationFormatted.value
})

/**
 * Function that handles the playing
 * and paused states of the player
 */
function handlePlayPause () {
  if (videoPlayerEl.value) {
    if (videoPlayerEl.value.paused) {
      isPlaying.value = true
      videoPlayerEl.value.play()

      inc()
      emit('play')
    } else {
      isPlaying.value = false
      videoPlayerEl.value.pause()
      
      emit('pause', playingDetails.value)
    }
  }
}

onMounted(() => {
  emit('loaded-meta-data')
})

onBeforeUnmount(() => {
  if (videoPlayerEl.value) {
    const source = videoPlayerEl.value.querySelector('source')
    
    if (source) {
      URL.revokeObjectURL(source.src)
    }
  }
})
</script>

<style lang="scss" scoped>
.video-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background: rgba(38, 38, 38, 1);
  margin: 0 auto;
}

.video-player {
  width: 100%;
  height: 100%;
  touch-action: manipulation;
  z-index: 40;
}

.video-player source {
  height: 100%;
}
</style>
