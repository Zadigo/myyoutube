<template>
  <article class="shadow-sm mb-2">
    <volt-card>
      <template #content>
        <div class="p-2">
          <div class="flex justify-left gap-2 items-center">
            <nuxt-link :to="`/videos/${video.video_id}`">
              <div class="video">
                <volt-avatar src="/avatars/avatar1.png" shape="circle" size="large" />
              </div>
            </nuxt-link>

            <div class="information">
              <nuxt-link :to="`/videos/${video.video_id}`">
                <h3 class="text-2xl font-bold">
                  {{ video.title }}
                </h3>
              </nuxt-link>

              <nuxt-link :to="`/channels/${video.user_channel.id}`">
                <p class="font-semibold">
                  {{ video.user_channel.name }}
                </p>
              </nuxt-link>

              <p v-if="video.description" class="text-sm font-light">
                {{ video.description }}
              </p>
            </div>
          </div>
        </div>
      </template>
    </volt-card>
  </article>
</template>


<script setup lang="ts">
import type { PlaylistVideo } from '~/types'

defineProps<{ video: PlaylistVideo }>()
</script>
