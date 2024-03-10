<template>
  <div ref="videoContainer" class="video-container">
    <!-- Source -->
    <!-- @loadedmetadata="getVideoDetails" @timeupdate="getVideoDetails" @waiting="isLoading=true" @canplay="isLoading=false" @click.stop="playPause" -->
    <video ref="videoPlayer" class="video-player" preload="metadata" controlist="nodownload" oncontextmenu="return false;">
      <source :src="videoSource" type="video/mp4">
    </video>

    <!-- Controls -->
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'BaseVideoPlayer',
  props: {
    videoSource: {
      type: String,
      required: true
    }
  },
  setup () {
    const isLoading = ref(true)
    return {
      isLoading
    }
  }
}
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
</style>
