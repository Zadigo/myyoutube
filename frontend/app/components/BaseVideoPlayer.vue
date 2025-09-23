<template>
  <div ref="videoContainerEl" class="relative flex items-center justify-center cursor-pointer bg-primary-900 m-0 overflow-hidden rounded-lg">
    <video ref="videoPlayerEl" class="video-player" preload="metadata" controlist="nodownload" oncontextmenu="return<boolean> false;" @loadedmetadata="getVideoDetails" @timeupdate="getVideoDetails" @canplay="isLoading<boolean>=false" @click.stop="handlePlayPause">
      <source :src="videoSource" type="video/mp4">
    </video>

    <div class="video-controls">
      <div class="video-control-actions">
        <div class="d-flex justify-content-left align-items-center gap-3">
          <NuxtButton @click.stop="handlePlayPause">
            <Icon v-if="!isPlaying" name="i-fa7-solid:play" />
            <Icon v-else name="i-fa7-solid:pause" />
          </NuxtButton>

          <div class="video-control-duration mx-3">
            <span>{{ currentTimeFormatted }}</span> /
            <span>{{ durationFormatted }}</span>
          </div>
        </div>

        <!-- Control configuration center -->
        <div class="video-control-configuration-center d-flex justify-content-end">
          <div class="video-control-settings">
            <NuxtButton @click="() => { showVideoSettings=!showVideoSettings }">
              <Icon name="i-fa7-solid:cog" />
            </NuxtButton>
          </div>

          <div class="video-control-volume ms-2">
            <NuxtButton @click="() => { showVolume=!showVolume }">
              <Icon v-if="volume < 0.1" name="i-fa7-solid:volume-low" />
              <Icon v-else-if="volume >= 0.1 && volume <= 0.8" name="i-fa7-solid:volume-up" />
              <Icon v-else-if="volume > 0.8" name="i-fa7-solid:volume-high" />
            </NuxtButton>
          </div>
        </div>
      </div>
    </div>
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

// Tracks the amount of the times the
// NuxtButton play was pressed during a
// viewing session
const { count, inc } = useCounter()

const isLoading = ref(true)
const isPlaying = ref<boolean>(false)
const wasPlayed = ref<boolean>(false)

// Indicates that the video was
// played once by the user
watchOnce(isPlaying, () => {
  wasPlayed.value= true
})

const duration = ref<number>(0)
const currentTime = ref<number>(0)
const volume = ref<number>(0.5)

const speeds = [2, 1.75, 1.5, 1, 0.75, 0.5]

const speed = ref<string>('1x')
const quality = ref<string>('1080p')

const showVolume = ref<boolean>(false)
const showSpeedSettings = ref<boolean>(false)
const showInteractiveMenu = ref<boolean>(false)
const showVideoSettings = ref<boolean>(true)
const showQualitySettings = ref<boolean>(true)

const videoContainerEl = ref<HTMLElement>()
const videoPlayerEl = ref<HTMLVideoElement>()

// Calculates the current completion of the
// video in percentage on the total duration
const completionPercentage = computed(() => {
  return Math.floor((currentTime.value / duration.value) * 100)
})

// Loads some frames from the current
// loaded video - especially for previews
function getFrames () {}

// Loads the metadata for the current
// loaded video: duration, size etc.
function getVideoDetails () {
  if (videoPlayerEl.value) {
    if (!Number.isNaN(videoPlayerEl.value.duration)) {
      duration.value = videoPlayerEl.value.duration
    }

    currentTime.value = videoPlayerEl.value.currentTime

    getFrames()
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

// Indicates that the viddeo has ended, in other
// words that the current time is equals the total
// video duration time
const isEnded = computed(() => {
  return currentTimeFormatted.value === durationFormatted.value
})



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

.video-controls {
  position: absolute;
  bottom: 5%;
  background: rgba(38, 38, 38, .8);
  padding: 1rem;
  width: 80%;
  align-items: center;
  color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 4px 10px 0 rgb(0 0 0 / 20%), 0 4px 20px 0 rgb(0 0 0 / 10%);
  z-index: 50;
}

.video-control-actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
}
</style>
