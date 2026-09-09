<template>
  <u-card class="mt-4">
    <div v-if="currentVideo" class="grid grid-cols-1 md:grid-cols-12">        
      <div class="col-span-10 col-start-2">
        <u-button :to="`/channels/${currentVideo.userChannel.reference}`" variant="outline">
          <span class="font-bold">{{ currentVideo.userChannel.name }}</span>
          <icon name="i-fa7-solid:circle-check" class="ms-2" />
        </u-button>

        <!-- Subscribers -->
        <p class="text-muted my-2">
          345.6K subscribers
        </p>
        
        <!-- Participants -->
        <video-participants class="py-5" />
        
        <!-- Description -->
        <div class="bg-primary-50 dark:bg-primary-800/20 rounded-lg font-light my-4 p-4 cursor-pointer hover:bg-primary-100 dark:hover:bg-primary-800/40 transition duration-200">
          Lorem, ipsum dolor sit amet consectetur adipisicing elit.
          Sequi porro iure repellat optio, ipsum ducimus veniam natus
          ipsam dolor, suscipit distinctio vero? Labore repellendus
          ipsum et cumque fuga? Ullam, nam! Lorem ipsum dolor sit amet
          consectetur adipisicing elit. Voluptates id pariatur
          fuga molestiae aperiam inventore repellendus, dolorum
          ducimus saepe fugiat minima quisquam. Deleniti, ratione?
          Quis et harum ullam ab nam.
        </div>
      </div>
    </div>
  </u-card>
</template>

<script setup lang="ts">
const currentVideo = injectLocal<Ref<VideoDetails>>(CURRENT_VIDEO_SYMBOL)
</script>
