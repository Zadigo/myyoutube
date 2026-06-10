<template>
  <div id="participants" class="flex justify-around overflow-x-scroll gap-2">
    <div v-for="i in 10" id="participant" :key="i" class="bg-primary-50 dark:bg-primary-900 border-primary-500 dark:border-primary-900 border-2 rounded-lg p-3 flex items-center justify-start gap-2">
      <div class="w-auto">
        <volt-avatar image="/avatars/avatar1.png" shape="circle" size="large" />
      </div>

      <p class="text-wrap font-bold text-sm">
        Julie Marboute
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style lang="scss" scoped>
#participants::-webkit-scrollbar {
  display: none;
}
</style>
