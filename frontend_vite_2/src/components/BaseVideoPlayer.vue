<template>
  <div ref="videoContainer" class="video-container">
    <!-- Source -->
    <!-- @waiting="isLoading=true" -->
    <video ref="videoPlayer" class="video-player" preload="metadata" controlist="nodownload" oncontextmenu="return false;" @loadedmetadata="getVideoDetails" @timeupdate="getVideoDetails" @canplay="isLoading = false" @click.stop="handlePlayPause">
      <source :src="videoSource" type="video/mp4">
    </video>

    <!-- Controls -->
    <div class="video-controls">
      <!-- <transition id="actions" tag="div" class="p-1 bg-dark" name="opacity">
        <div v-if="showVideoSettings" class="row p-1 mb-3" style="position: absolute; left: calc(100% - 300px); bottom: 100%;height: auto;width: 300px;margin-bottom: .5rem;border-radius: .5rem;" @mouseleave="showVideoSettings = false">
          <div class="col-6 justify-content-start">
            <button v-if="showSpeedSettings || showQualitySettings" type="button" class="btn btn-light btn-sm" @click="showSpeedSettings = false, showQualitySettings = false">
              <font-awesome-icon icon="fa-solid fa-arrow-left" />
            </button>
          </div>

          <div class="col-6 d-flex justify-content-end" @click="showVideoSettings = false">
            <button type="button" class="btn btn-light btn-sm">
              <font-awesome-icon icon="fa-solid fa-close" />
            </button>
          </div>
        </div>
      </transition> -->

      <div class="video-control-actions">
        <div class="d-flex justify-content-left align-items-center gap-3">
          <button type="button" class="btn btn-primary shadow-none" @click.stop="handlePlayPause">
            <font-awesome-icon v-if="!isPlaying" :icon="[ 'fas', 'fa-play' ]" />
            <font-awesome-icon v-else :icon="[ 'fas', 'fa-pause' ]" />
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
              <font-awesome-icon icon="fa-solid fa-cog" />
            </button>
          </div>

          <div class="video-control-volume ms-2">
            <button type="button" class="btn btn-primary" @click="showVolume = !showVolume">
              <font-awesome-icon v-if="volume < 0.1" icon="fas fa-volume-low" />
              <font-awesome-icon v-else-if="volume >= 0.1 && volume <= 0.8" icon="fas fa-volume-up" />
              <font-awesome-icon v-else-if="volume > 0.8" icon="fas fa-volume-high" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, computed, defineComponent } from 'vue'
import { useCounter, watchOnce } from '@vueuse/core'

export default defineComponent({
  name: 'BaseVideoPlayer',
  props: {
    videoSource: {
      type: String,
      required: true
    }
  },
  emits: {
    'loaded-meta-data' () {
      return true
    },
    play () {
      return true
    },
    pause (_data: [ number, string ]) {
      return true
    }
  },
  setup () {
    // Tracks the amount of the times the
    // button play was pressed during a
    // viewing session
    const { count, inc } = useCounter()

    const isLoading = ref(true)
    const isPlaying = ref(false)
    const wasPlayed = ref(false)

    watchOnce(isPlaying, () => {
      // Indicates that the video was
      // played once by the user
      wasPlayed.value= true
    })
    
    const duration = ref<number>(0)
    const currentTime = ref<number>(0)
    const volume = ref<number>(0.5)

    const completionPercentage = computed(() => {
      return Math.floor((currentTime.value / duration.value) * 100)
    })

    const speed = ref<string>('1x')
    const quality = ref<string>('1080p')
    const speeds = [2, 1.75, 1.5, 1, 0.75, 0.5]

    const showVolume = ref(false)
    const showSpeedSettings = ref(false)
    const showInteractiveMenu = ref(false)
    const showVideoSettings = ref(true)
    const showQualitySettings = ref(true)

    return {
      playCount: count,
      incrementCounter: inc,
      quality,
      speed,
      speeds,
      volume,
      duration,
      completionPercentage,
      currentTime,
      isPlaying,
      isLoading,
      wasPlayed,
      showVolume,
      showSpeedSettings,
      showInteractiveMenu,
      showVideoSettings,
      showQualitySettings
    }
  },
  computed: {
    currentTimeFormatted () {
      return this.formatTime(this.currentTime)
    },
    durationFormatted () {
      return this.formatTime(this.duration)
    },
    isEnded () {
      // Indicates that the viddeo has ended, in other
      // words that the current time is equals the total
      // video duration time
      return this.currentTimeFormatted === this.durationFormatted
    }
  },
  mounted () {
    this.$emit('loaded-meta-data', this.$refs.videoPlayer)
  },
  beforeUnmount () {
    const source = this.$refs.videoPlayer.querySelector('source')
    URL.revokeObjectURL(source.src)
  },
  methods: {
    handlePlayPause () {
      // Allows the user to either play or pause
      // the current video
      if (this.$refs?.videoPlayer.paused) {
        this.isPlaying = true
        this.$refs.videoPlayer.play()
        this.incrementCounter()
        this.$emit('play')
      } else {
        this.isPlaying = false
        this.$refs.videoPlayer.pause()
        this.$emit('pause', [ this.progress, this.formatTime(this.currentTime) ])
      }
    },
    handleVolumeClick () {

    },
    getVideoDetails () {
      // Get the main details for the current video
      // such as the duration and set the current
      // time on the player
      if (this.$refs.videoPlayer) {
        const player = this.$refs.videoPlayer

        if (!Number.isNaN(player.duration)) {
          this.duration = player.duration
        }

        this.currentTime = player.currentTime
        this.getFrames()
      }
    },
    getFrames () {

    },
    formatTime (value: number) {
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
  }
})
</script>

<style scoped>
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
