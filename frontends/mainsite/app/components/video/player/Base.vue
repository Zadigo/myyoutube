<template>
  <div ref="videoContainerEl" class="relative minx-h-[300px] md:min-h-[500px] xl:min-h-[700px] z-20 flex items-center justify-center cursor-pointer bg-primary-900 dark:bg-primary-950 mx-auto overflow-hidden rounded-lg">
    <client-only>
      <template #default>
        <video ref="videoPlayerEl" class="w-full touch-manipulation has-[source]:h-full" preload="metadata" controlist="nodownload" oncontextmenu="return false;" @loadedmetadata="handleVideoMetadata" @timeupdate="handleVideoMetadata" @canplay="handleCanPlay" @click.stop="handlePlayPause">
          <source :src="videoSource" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </template>

      <template #placeholder>
        <div class="p-5 text-center text-primary-50 dark:text-primary">
          <p class="mb-3">Loading video player...</p>
          <p>Please wait while the video player is being initialized.</p>
        </div>
      </template>

      <template #fallback>
        <div class="p-5 text-center text-primary-50 dark:text-primary">
          <p class="mb-3">Video playback is not supported in SSR mode.</p>
          <p>Please enable client-side rendering to view the video player.</p>
        </div>
      </template>
    </client-only>

    <dev-only>
      <div class="p-5 rounded-md absolute top-1 left-1 max-w-xs z-40 bg-primary-50/50 dark:bg-primary-900/50 text-primary-900 dark:text-primary-50">
        {{ playingStatistics }}
      </div>
    </dev-only>

    <!-- Controls -->
    <video-player-controls />
  </div>
</template>

<script setup lang="ts">
import { useVideoPlayer, useVideoPlayerControls } from './utils'
import type { Undefineable, VideoTechnicalDetails } from '~/types' 

const { videoSource } = defineProps<{ videoSource: Undefineable<string> }>()

const emit = defineEmits<{ 
  'play': [], 
  'pause': [VideoTechnicalDetails], 
  'player:loaded': [], 
  'update:metadata': [data: VideoTechnicalDetails] 
}>()

const videoPlayerEl = useTemplateRef<HTMLVideoElement>('videoPlayerEl')
const videoContainerEl = useTemplateRef<HTMLDivElement>('videoContainerEl')

const { el } = useVideoPlayer(videoPlayerEl, videoSource)
const { handleCanPlay, handlePlayPause, handleVideoMetadata, playingStatistics, isPlaying } = useVideoPlayerControls(el)

onMounted(() => {
  emit('player:loaded')
  emit('update:metadata', playingStatistics.value)
})

/**
 * Watchers
 */

watch(isPlaying, (newVal) => {
  if (newVal) {
    emit('play')
  } else {
    emit('pause', playingStatistics.value)
  }
})
</script>
