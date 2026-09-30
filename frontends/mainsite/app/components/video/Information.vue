<template>
  <u-card>
    <div v-if="currentVideo" class="grid grid-cols-1 md:grid-cols-12">        
      <div class="col-span-12">
        <u-button v-if="currentVideo.userChannel" :to="`/channels/${currentVideo.userChannel.reference}`" variant="outline">
          <span class="font-bold">{{ currentVideo.userChannel.name }}</span>
          <icon name="i-fa7-solid:circle-check" class="ms-2" />
        </u-button>
        <u-skeleton v-else class="h-10 w-40" />

        <!-- Subscribers -->
        <p class="my-2 text-slate-400 font-semibold">
          345.6K subscribers
        </p>
        
        <!-- Participants -->
        <lazy-video-participants class="py-5" hydrate-on-idle />
        
        <!-- Description -->
        <div class="bg-primary-50 dark:bg-primary-800/20 rounded-lg my-4 p-4 cursor-pointer hover:bg-primary-100 dark:hover:bg-primary-800/40 transition duration-200">
          <span class="font-light">
            {{ currentVideo.description }}
          </span>

          <div class="flex gap-2 my-5">
            <nuxt-link to="https://www.instagram.com/some-handler/">
              <u-badge icon="i-lucide-instagram" label="@some-handler" variant="soft" color="info" />
            </nuxt-link>

            <nuxt-link to="https://www.linkedin.com/in/some-handler/">
              <u-badge icon="i-lucide-linkedin" label="@some-handler" variant="soft" color="info" />
            </nuxt-link>
            
            <nuxt-link to="https://twitter.com/some-handler/">
              <u-badge icon="i-lucide-x" label="@some-handler" variant="soft" color="info" />
            </nuxt-link>
            
            <nuxt-link to="https://www.youtube.com/@some-handler/">
              <u-badge icon="i-lucide-youtube" label="@some-handler" variant="soft" color="info" />
            </nuxt-link>
          </div>
        </div>
      </div>
    </div>
  </u-card>
</template>

<script setup lang="ts">
const currentVideo = injectLocal<Ref<VideoDetails>>(CURRENT_VIDEO_SYMBOL)
</script>
