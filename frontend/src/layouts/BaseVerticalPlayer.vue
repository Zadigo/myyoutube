<template>
  <div class="video-container">
    <div @click="playPause">
      <video ref="videoPlayer" class="video-player" controlist="nodownload" oncontextmenu="return false;" @loadmetadata="getVideoDetails" @timeupdate="getVideoDetails" @waiting="isLoading = true" @canplay="isLoading = false">
        <source :src="videoSource" type="video/mp4" />
      </video>
    </div>

    <div class="actions">
      <button type="button" class="btn btn-floating btn-light" @click="playPause">
        <font-awesome-icon v-if="isPlaying" icon="fa-solid fa-pause"></font-awesome-icon>
        <font-awesome-icon v-else icon="fa-solid fa-play"></font-awesome-icon>
      </button>

      <button type="button" class="btn btn-floating btn-light mx-2">
        <font-awesome-icon icon="fa-solid fa-volume-up"></font-awesome-icon>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseVerticalPlayer',
  props: {
    videoSource: {
      type: String,
      required: true,
    },
  },
  data () {
    return {
      isPlaying: false
    }
  },
  methods: {
    playPause () {
      if (this.$refs?.videoPlayer.paused) {
        this.isPlaying = true
        this.$refs.videoPlayer.play()
      } else {
        this.isPlaying = true
        this.$refs.videoPlayer.pause()
      }
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
  border-radius: .5rem;
  overflow: hidden;
}

.video-player {
  width: 100%;
  height: 100%;
  touch-action: manipulation;
}

.video-player source {
  height: 100%;
}

.actions {
  position: absolute;
  padding: .5rem;
  width: 100%;
  bottom: 1%;
}
</style>
