<template>
  <section id="algorithm">
    <volt-card class="shadow-sm">
      <template #content>
        <h1 class="font-bold text-3xl">
          Customize your viewing experience
        </h1>
      </template>
    </volt-card>

    <settings-card title="Algorithm constructor" subtitle="Build your own viewing algorithm">
      <template #default>
        <lazy-settings-algorithm-conditional-blocks hydrate-on-idle />
      </template>
    </settings-card>
  </section>
</template>

<script setup lang="ts">
import { useCategories } from '~/composables/use'

definePageMeta({
  layout: 'settings'
})

/**
 * Categories
 */

const { load, categories } = useCategories()
await load()
provide('categories', categories)


/**
 * Settings
 */

useAlgorithmSettingsComposable()
</script>
