<template>
  <div class="video-controls">
    <div class="video-control-actions">
      <div class="d-flex justify-content-left align-items-center gap-3">
        <button type="button" class="btn btn-primary shadow-none" @click.stop="emit('play-pause')">
          <font-awesome v-if="!isPlaying" icon="play" />
          <font-awesome v-else icon="pause" />
        </button>

        <div class="video-control-duration mx-3">
          <span>{{ currentTime }}</span> /
          <span>{{ durationTime }}</span>
        </div>
      </div>

      <!-- Control configuration center -->
      <div class="video-control-configuration-center d-flex justify-content-end">
        <div class="video-control-settings">
          <button type="button" class="btn btn-primary" @click="showVideoSettings=!showVideoSettings">
            <font-awesome icon="cog" />
          </button>
        </div>

        <div class="video-control-volume ms-2">
          <button type="button" class="btn btn-primary" @click="showVolume=!showVolume">
            <font-awesome v-if="volume < 0.1" icon="volume-low" />
            <font-awesome v-else-if="volume >= 0.1 && volume <= 0.8" icon="volume-up" />
            <font-awesome v-else-if="volume > 0.8" icon="volume-high" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits({
  'play-pause'() {
    return true
  }
})

withDefaults(defineProps<{ volume?: number, currentTime?: string, durationTime?: string, isPlaying?: boolean }>(), {
  volume: 0.1,
  currentTime: '00:00',
  durationTime: '00:00',
  isPlaying: false
})

const showVolume = ref<boolean>(false)
const showSpeedSettings = ref<boolean>(false)
const showInteractiveMenu = ref<boolean>(false)
const showVideoSettings = ref<boolean>(true)
const showQualitySettings = ref<boolean>(true)
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
