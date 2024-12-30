<template>
  <div ref="videoContainerEl" class="video-container">
    <video ref="videoPlayerEl" class="video-player" preload="metadata" controlist="nodownload" oncontextmenu="return false;" @loadedmetadata="getVideoDetails" @timeupdate="getVideoDetails" @canplay="isLoading = false" @click.stop="handlePlayPause">
      <source :src="videoSource" type="video/mp4">
    </video>

    <div class="video-controls">
      <div class="video-control-actions">
        <div class="d-flex justify-content-left align-items-center gap-3">
          <button type="button" class="btn btn-primary shadow-none" @click.stop="handlePlayPause">
            <font-awesome v-if="!isPlaying" icon="play" />
            <font-awesome v-else icon="pause" />
          </button>

          <div class="video-control-duration mx-3">
            <span>{{ currentTimeFormatted }}</span> /
            <span>{{ durationFormatted }}</span>
          </div>
        </div>

        <!-- Control configuration center -->
        <div class="video-control-configuration-center d-flex justify-content-end">
          <div class="video-control-settings">
            <button type="button" class="btn btn-primary" @click="showVideoSettings = !showVideoSettings">
              <font-awesome icon="cog" />
            </button>
          </div>

          <div class="video-control-volume ms-2">
            <button type="button" class="btn btn-primary" @click="showVolume = !showVolume">
              <font-awesome v-if="volume < 0.1" icon="volume-low" />
              <font-awesome v-else-if="volume >= 0.1 && volume <= 0.8" icon="volume-up" />
              <font-awesome v-else-if="volume > 0.8" icon="volume-high" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue'
import { useCounter, watchOnce } from '@vueuse/core'

const props = defineProps({
  videoSource: {
    type: String,
    required: true
  }
})

const emit = defineEmits({
  'loaded-meta-data' (_el: HTMLVideoElement | undefined) {
    return true
  },
  play () {
    return true
  },
  pause (_data: [ number, string ]) {
    return true
  }
})

// Tracks the amount of the times the
// button play was pressed during a
// viewing session
const { count, inc } = useCounter()

const isLoading = ref(true)
const isPlaying = ref(false)
const wasPlayed = ref(false)

// Indicates that the video was
// played once by the user
watchOnce(isPlaying, () => {
  wasPlayed.value= true
})

const duration = ref(0)
const currentTime = ref(0)
const volume = ref(0.5)

const completionPercentage = computed(() => {
  return Math.floor((currentTime.value / duration.value) * 100)
})

const speed = ref('1x')
const quality = ref('1080p')
const speeds = [2, 1.75, 1.5, 1, 0.75, 0.5]

const showVolume = ref(false)
const showSpeedSettings = ref(false)
const showInteractiveMenu = ref(false)
const showVideoSettings = ref(true)
const showQualitySettings = ref(true)

const videoContainerEl = ref<HTMLElement>()
const videoPlayerEl = ref<HTMLVideoElement>()

function getFrames () {}

function getVideoDetails () {
  if (videoPlayerEl.value) {
    if (!Number.isNaN(videoPlayerEl.value.duration)) {
      duration.value = videoPlayerEl.value.duration
    }

    currentTime.value = videoPlayerEl.value.currentTime
    getFrames()
  }
}

function formatTime (value: number) {
  // Formats the time to a human readable
  // format for the user to track the
  // time at which the video is currently at
  let hours = Math.floor(value / 3600)
  let minutes = Math.floor((value % 3600) / 60)
  let seconds = Math.floor(value % 60)

  hours = hours < 10 ? '0' + hours : hours
  minutes = minutes < 10 ? '0' + minutes : minutes
  seconds = seconds < 10 ? '0' + seconds : seconds

  if (hours > 0) {
    return `${hours}:${minutes}:${seconds}`
  }

  return `${minutes}:${seconds}`
}

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
      emit('pause', [
        1,
        formatTime(currentTime.value)
      ])
    }
  }
}

const currentTimeFormatted = computed(() => {
  return formatTime(currentTime.value)
})

const durationFormatted = computed(() => {
  return formatTime(duration.value)
})

const isEnded = computed(() => {
  // Indicates that the viddeo has ended, in other
  // words that the current time is equals the total
  // video duration time
  return currentTimeFormatted.value === durationFormatted.value
})

onMounted(() => {
  emit('loaded-meta-data', videoPlayerEl.value)
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
