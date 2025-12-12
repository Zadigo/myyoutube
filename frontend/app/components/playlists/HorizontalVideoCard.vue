<template>
  <article class="shadow-sm mb-2">
    <volt-card>
      <template #content>
        <div class="p-2">
          <div class="flex justify-left gap-2 items-center">
            <nuxt-link :to="`/videos/${video.node.videoId}`">
              <div class="video">
                <volt-avatar src="/avatars/avatar1.png" shape="circle" size="large" />
              </div>
            </nuxt-link>

            <div class="information">
              <nuxt-link :to="`/videos/${video.node.videoId}`">
                <h3 class="text-2xl font-bold">
                  {{ video.node.title }}
                </h3>
              </nuxt-link>

              <nuxt-link :to="`/channels/${video.node.userChannel.reference}`">
                <p class="font-semibold">
                  {{ video.node.userChannel.name }}
                </p>
              </nuxt-link>

              <p v-if="video.node.description" class="text-sm font-light">
                {{ video.node.description }}
              </p>
            </div>
          </div>
        </div>
      </template>
    </volt-card>
  </article>
</template>


<script setup lang="ts">
import type { PlaylistVideoNode } from '~/types'

defineProps<{ video: PlaylistVideoNode }>()
</script>
