<template>
  <!-- <div class="video-container" @click="playPause"> -->
  <div class="video-container">
    <!-- Spinner -->
    <div v-if="isLoading" class="load-wrapp opacity-50">
      <div class="load-2">
        <span class="visually-hidden">Loading 2</span>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
      </div>
    </div>

    <!-- Player -->
    <video ref="videoPlayer" class="video-player" controlist="nodownload" oncontextmenu="return false;" @loadmetadata="getVideoDetails" @timeupdate="getVideoDetails" @waiting="isLoading = true" @canplay="isLoading = false">
      <source :src="videoSource" type="video/mp4" />
    </video>

    <!-- Controls -->
    <div class="video-controls">
      <div class="video-control-progress-container">
        <div ref="videoProgress" class="progress" @click.stop.prevent="progressClick($event)">
          <div :style="{ width: `${progress}%` }" class="current">
            <!-- <div :style="{ left: `${progress}%` }" class="ball"></div> -->
          </div>
        </div>
      </div>

      <div class="video-control-actions">
        <div class="d-flex justify-content-left align-items-center">
          <button type="button" class="btn btn-light shadow-none" @click.stop="playPause">
            <font-awesome-icon v-if="!isPlaying" icon="fa-solid fa-play" />
            <font-awesome-icon v-else icon="fa-solid fa-pause" />
          </button>

          <div class="video-control-duration mx-3">
            <span>{{ currentTimeFormatted }}</span>
            <span>{{ durationFormatted }}</span>
          </div>
        </div>

        <div class="video-control-configuration-center d-flex justify-content-end">
          <div class="video-control-settings">
            <button type="button" class="btn btn-light" @click="showVideoSettings = !showVideoSettings">
              <font-awesome-icon icon="fa-solid fa-cog" />
            </button>

            <transition name="opacity">
              <div v-if="showVideoSettings" class="picker">
                <div class="row p-1">
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

                <div v-if="!showSpeedSettings && !showQualitySettings" :key="0" class="list-group">
                  <a href class="list-group-item list-group-item-action d-flex justify-content-between align-items-center bg-transparent text-light border-0" @click.prevent="showSpeedSettings = true">
                    <span>
                      <font-awesome-icon icon="fa-solid fa-gauge" class="me-2" />
                      Speed
                    </span>
                    <span>
                      {{ speed }}
                      <font-awesome-icon icon="fa-solid fa-arrow-right" class="ms-2" />
                    </span>
                  </a>

                  <a href class="list-group-item list-group-item-action d-flex justify-content-between align-items-center bg-transparent text-light border-0" @click.prevent="showQualitySettings = true">
                    <span>
                      <font-awesome-icon icon="fa-solid fa-gauge" class="me-2" />
                      Quality
                    </span>

                    <span>
                      {{ quality }}
                      <font-awesome-icon icon="fa-solid fa-arrow-right" class="ms-2" />
                    </span>
                  </a>
                </div>

                <div v-if="showSpeedSettings" :key="1" class="list-group">
                  <a v-for="speed in speeds" :key="speed" href class="list-group-item list-group-item-action bg-transparent text-light" @click.prevent="speedClick(speed)">
                    {{ `${speed}x` }}
                  </a>
                </div>

                <div v-if="showQualitySettings" :key="3" class="list-group">
                  <a href type="button" class="list-group-item">1080p</a>
                </div>
                <!-- <transition-group name="opacity" mode="out-in">
                </transition-group> -->
              </div>
            </transition>
          </div>

          <div class="video-control-volume ms-2">
            <button ref="volume" type="button" class="btn btn-light">
              <font-awesome-icon v-if="volume < 0.1" icon="fa-solid fa-volume-low" />
              <font-awesome-icon v-else-if="volume >= 0.1 && volume <= 0.8" icon="fa-solid fa-volume-up" />
              <font-awesome-icon v-else-if="volume > 0.8" icon="fa-solid fa-volume-high" />
            </button>

            <div class="picker">
              <div class="tracker">
                <div :style="{ height: `30%` }" class="track"></div>
                <div :style="{ bottom: `calc(30%) - 0.5rem` }" class="ball"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { onKeyStroke } from '@vueuse/core'

export default {
  name: 'BaseVideoPlayer',
  props: {
    videoUrl: {
      type: String,
      required: true,
    },
  },
  emits: {
    play: () => true,
    pause: () => true,
    'time-update': () => true
  },
  data () {
    return {
      videoSource: null,
      isPlaying: false,
      isLoading: true,
      duration: 0,
      currentTime: 0,
      speed: '1x',
      quality: '1080p',
      volume: 0.3,
      speeds: [2, 1.75, 1.5, 1, 0.75, 0.5],

      showVideoSettings: false,
      showSpeedSettings: false,
      showQualitySettings: false
    }
  },
  computed: {
    currentTimeFormatted () {
      return this.formatTime(this.currentTime)
    },
    durationFormatted () {
      return this.formatTime(this.duration)
    },
    progress () {
      return (this.currentTime / this.duration) * 100
    }
  },
  mounted () {
    this.getVideoDetails()
    this.videoSource = this.videoUrl

    const self = this
    onKeyStroke(['p', ' ', 'k'], function (e) {
      e.preventDefault()
      self.playPause()
    })
    onKeyStroke('ArrowUp', function (e) {
      e.preventDefault()
      let volume = self.volume += 0.1
      if (volume >= 1) {
        volume = 1
      }
      self.volume = volume
      self.$refs.videoPlayer.volume = volume
    })
    onKeyStroke('ArrowDown', function (e) {
      e.preventDefault()
      let volume = self.volume -= 0.1
      if (volume <= 0) {
        volume = 0
      }
      self.volume = volume
      self.$refs.videoPlayer.volume = volume
    })
    onKeyStroke(['ArrowLeft', 'j'], function (e) {
      e.preventDefault()
    })
    onKeyStroke(['ArrowRight', 'l'], function (e) {
      e.preventDefault()
    })
  },
  methods: {
    playPause () {
      if (this.$refs?.videoPlayer.paused) {
        this.isPlaying = true
        this.$refs.videoPlayer.play()
        this.$emit('play')
      } else {
        this.isPlaying = true
        this.$refs.videoPlayer.pause()
        this.$emit('pause', [this.progress, this.formatTime(this.currentTime)])
      }
    },
    progressClick (event) {
      const currentTime = (this.duration * event.offsetX) / this.$refs.videoProgress.offsetWidth
      this.currentTime = currentTime
      this.$refs.videoPlayer.currentTime = currentTime
      this.$emit('time-update', currentTime)
    },
    speedClick (speed) {
      this.speed = `${speed}x`
      this.$refs.videoPlayer.playbackRate = speed
      this.showSpeedSettings = false
    },
    getVideoDetails () {
      if (this.$refs?.videoPlayer) {
        const player = this.$refs.videoPlayer

        if (!Number.isNaN(player.duration)) {
          this.duration = player.duration
        }

        this.currentTime = player.currentTime

        if (player.paused) {
          this.isPlaying = false
          player.pause()
        } else {
          this.isPlaying = true
          player.play()
        }
      }
    },
    formatTime (value) {
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
}
</script>

<style scoped>

.video-container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  cursor: pointer;
  background: rgb(38, 38, 38);
  margin: 0 auto;
}

.video-player {
  width: 100%;
  height: 100%;
  touch-action: manipulation;
}

.video-player source {
  height: 100%;
}

.video-controls {
  position: absolute;
  bottom: 5%;
  background: black;
  padding: 1rem;
  z-index: 10;
  width: 80%;
  align-items: center;
  color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 4px 10px 0 rgb(0 0 0 / 20%), 0 4px 20px 0 rgb(0 0 0 / 10%);
  z-index: 1055;
}

.video-control-actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
}

.video-control-configuration .video-control-volume {
  position: relative;
}

/* .video-control-duration span {
  margin: 0 3px;
} */

.video-control-duration span:first-child::after {
  content: ":";
  margin: 0 3px;
}

.video-control-speed {
  position: relative;
  /* min-width: 60px; */
  top: 0;
}

.video-control-speed .picker {
  position: absolute;
  left: -25%;
  /* top: -740%; */
  bottom: 180%;
  background: rgb(38, 38, 38);
  padding: .5rem;
  border-radius: 0.5rem;
}

.video-control-progress-container {
  display: flex;
  width: 100%;
}

.video-control-progress-container .progress {
  position: relative;
  display: flex;
  flex: 1;
  align-items: center;
  background: rgb(38, 38, 38);
  margin: 0 0 1rem;
  height: .25rem;
  width: 100%;
}

.video-control-progress-container .current {
  display: flex;
  background: #dc3545;
  /* transition: width 0.2ms; */
  transition: width ease-in-out .5s;
  height: .25rem;
  /* border-radius: 6px; */
  /* background: royalblue; */
}

.video-control-progress-container .ball {
  position: absolute;
  z-index: 99;
  left: 0;
  bottom: -0.5rem;
  height: 1rem;
  width: 1rem;
  border-radius: 1rem;
  background: #fff;
  /* border: 1px solid #000; */
}

.video-control-configuration-center {
}

.video-control-settings {
  position: relative;
}

.video-control-settings .picker {
  position: absolute;
  transition: height .5s ease;
  bottom: 80px;
  right: -30%;
  width: 300px;
  background: rgb(38, 38, 38);
  border-radius: .5rem;
  padding: .5rem;
  z-index: 100;
}

.video-control-volume {
  position: relative;
}

.video-control-volume .picker {
  position: absolute;
  height: 100px;
  padding: 1rem;
  left: 20%;
  top: -350%;
  background: rgb(38, 38, 38);
  border-radius: 0.5rem;
}

.video-control-volume .picker .tracker {
  position: relative;
  height: 100%;
  width: 4px;
  border-radius: 4px;
  background-color: #dc3545;
}

.video-control-volume .picker .current {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 4px;
  background-color: #fff;
}

.video-control-volume .picker .ball {
  position: absolute;
  background-color: #fff;
  left: -8px;
  width: 20px;
  height: 10px;
  border-radius: 13px;
}

.load-wrapp {
  position: absolute;
  z-index: 3;
}
</style>
