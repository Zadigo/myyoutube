<template>
  <nuxt-card class="shadow-sm">
    <template #header>
      <div class="px-3 py-2">
        <div class="flex justify-between">
          <nuxt-button draggable="true">
            <icon name="fa-solid:grip-vertical" />
          </nuxt-button>

          <nuxt-button @click="handleDeleteBlock">
            <icon name="fa-solid:trash" />
          </nuxt-button>
        </div>
      </div>
    </template>

    <h5 class="font-bold tracking-tight text-gray-900 dark:text-green-50 mb-3">
      {{ title }}
    </h5>

    <slot />
  </nuxt-card>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'delete-block': [] }>()
defineProps<{ title: string }>()

function handleDeleteBlock () {
  emit('delete-block')
}
</script>
