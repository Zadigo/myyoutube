<template>
  <div id="participants" class="flex justify-around overflow-x-scroll gap-2">
    <!-- <div v-for="i in 10" id="participant" :key="i" class="bg-primary-50 dark:bg-primary-900 border-primary-500 dark:border-primary-900 border-2 rounded-lg p-3 flex items-center justify-start gap-2">
      <div class="w-auto">
        <u-avatar src="/avatars/avatar1.png" size="lg" />
      </div>

      <p class="text-wrap font-bold text-sm">
        Julie Marboute
      </p>
    </div> -->
    <u-badge v-for="i in 15" id="participant" :key="i" :avatar="{ src: '/avatars/avatar1.png', size: 'lg' }" variant="subtle">
      <template #default>
        <nuxt-link :to="`/channels/${i}`" class="font-bold text-md ms-3">
          Julie Marboute
        </nuxt-link>
      </template>
    </u-badge>
  </div>
</template>

<script setup lang="ts">
</script>

<style lang="scss" scoped>
#participants::-webkit-scrollbar {
  display: none;
}
</style>
