<template>
  <section id="algorithm">
    <u-card class="shadow-sm">
      <h1 class="font-bold text-3xl">
        Customize your viewing experience
      </h1>
    </u-card>

    <settings-card title="Algorithm constructor" subtitle="Build your own viewing algorithm">
      <template #default>
        <lazy-settings-algorithm-conditional-blocks hydrate-on-idle />
      </template>
    </settings-card>
  </section>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'settings'
})

/**
 * Categories
 */

const { load, categories } = useCategoriesComposable()
await load()

provide('categories', categories)

/**
 * Settings
 */

useAlgorithmSettingsComposable()
</script>
