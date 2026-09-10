<template>
  <div class="conditional-blocks">
    <volt-alert>
      You can set up conditional blocks to filter content based on specific criteria.
      For example, you can create a block that only shows videos related to a specific theme or
      keywords. This allows you to customize your viewing experience and focus on the content that matters most to you.

      {{ conditions }}

      <div class="mt-5">
        <nuxt-link to="/">
          <icon name="i-fa7-solid:arrow-right" />
          Advanced algorithm builder
        </nuxt-link>
      </div>
    </volt-alert>

    <div class="space-y-2">
      <settings-algorithm-condition-block v-for="(condition, idx) in conditions" :key="condition.id" :index="idx" @delete-block="remove" />
    </div>

    <div class="flex justify-center mt-3">
      <u-button variant="subtle" @click="create">
        <icon name="i-fa7-solid:plus" class="me-2" />
        Create
      </u-button>
    </div>
  </div>
</template>

<script setup lang="ts">
const { conditions, create, remove } = useAlgorithmSettingsStore()
</script>
