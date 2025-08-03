<template>
  <VoltCard class="mt-4">
    <template #content>
      <div v-if="currentVideo" class="flex justify-around items-start gap-3">
        <NuxtLink :to="`/channels/${currentVideo.user_channel?.reference}`" class="mt-2" aria-label="">
          <VoltAvatar image="/avatars/avatar1.png" shape="circle" size="large" alt="" />
        </NuxtLink>

        <div class="information">
          <VoltButton :to="`/channels/${currentVideo.user_channel?.reference}`" variant="outlined" class="px-0">
            <span class="font-bold">{{ currentVideo.user_channel?.name }}</span>
            <Icon name="i-fa7-solid:circle-check" class="ms-2" />
          </VoltButton>
          
          <p class="text-muted my-2">
            345.6K subscribers
          </p>

          <!-- <v-sheet class="mx-auto" max-width="800px">
            <v-slide-group show-arrows>
              <v-slide-group-item v-for="n in 10" :key="n" v-slot="{ isSelected, toggle }">
                <VoltButton :color="isSelected ? 'success' : undefined" class="ma-2" rounded @click="toggle">
                  Options {{ n }}
                </VoltButton>
              </v-slide-group-item>
            </v-slide-group>
          </v-sheet> -->
          
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

          <VoltButton color="primary" variant="outlined">
            <Icon name="i-fa7-solid:caret-down" class="me-2" />
            More
          </VoltButton>
        </div>
      </div>
    </template>
  </VoltCard>
</template>

<script setup lang="ts">
import type { VideoInfo } from '~/types'

const currentVideo = inject<Ref<VideoInfo>>('currentVideo')
</script>
