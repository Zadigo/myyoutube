<template>
  <aside class="mt-3 bg-primary-100 dark:bg-primary-800 rounded-lg h-200 overflow-y-scroll p-3">
    <nuxt-link :to="`/channels/ch_noienozinfoz`">
      <u-card v-for="i in 120" :key="i" class="mt-1">
        Something
      </u-card>
    </nuxt-link>
  </aside>
</template>

<script setup lang="ts">
</script>
