<template>
  <div id="participants" class="flex justify-around overflow-x-scroll gap-2">
    <div v-for="i in 10" id="participant" :key="i" class="bg-primary-50 dark:bg-primary border-primary-500 dark:border-primary-900 border-2 rounded-lg p-3 flex items-center justify-start gap-1">
      <div>
        <VoltAvatar image="/avatars/avatar1.png" shape="circle" size="large" />
      </div>

      <div class="flex gap-1 items-center">
        <p class="font-bold text-sm">
          Julie Marboute
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { VideoInfo } from '~/types'

const currentVideo = inject<Ref<VideoInfo>>('currentVideo')
</script>

<style lang="scss" scoped>
#participants::-webkit-scrollbar {
  display: none;
}
</style>
