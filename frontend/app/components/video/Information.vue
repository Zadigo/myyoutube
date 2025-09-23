<template>
  <volt-card class="mt-4">
    <template #content>
      <div v-if="currentVideo" class="grid grid-cols-12">
        <div class="col-span-1">
          <nuxt-link :to="`/channels/${currentVideo.user_channel?.reference}`" class="mt-2" aria-label="">
            <volt-avatar image="/avatars/avatar1.png" shape="circle" size="large" alt="" />
          </nuxt-link>
        </div>
        
        <div class="col-span-11">
          <volt-button :to="`/channels/${currentVideo.user_channel?.reference}`" variant="outlined" class="px-0">
            <span class="font-bold">{{ currentVideo.user_channel?.name }}</span>
            <Icon name="i-fa7-solid:circle-check" class="ms-2" />
          </volt-button>

          <p class="text-muted my-2">
            345.6K subscribers
          </p>
          
          <!-- Participants -->
          <video-participants class="py-5" />
          
          <div class="bg-slate-50 rounded-lg font-light my-4 p-4">
            <p class="font-light">
              Lorem, ipsum dolor sit amet consectetur adipisicing elit.
              Sequi porro iure repellat optio, ipsum ducimus veniam natus
              ipsam dolor, suscipit distinctio vero? Labore repellendus
              ipsum et cumque fuga? Ullam, nam! Lorem ipsum dolor sit amet
              consectetur adipisicing elit. Voluptates id pariatur
              fuga molestiae aperiam inventore repellendus, dolorum
              ducimus saepe fugiat minima quisquam. Deleniti, ratione?
              Quis et harum ullam ab nam.
            </p>
          </div>

          <volt-button color="primary" variant="outlined">
            <Icon name="i-fa7-solid:caret-down" class="me-2" />
            More
          </volt-button>
        </div>
      </div>
    </template>
  </volt-card>
</template>

<script setup lang="ts">
import type { VideoInfo } from '~/types'

const currentVideo = inject<Ref<VideoInfo>>('currentVideo')
</script>
