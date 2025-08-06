<template>
  <VoltCard class="shadow-sm">
    <template #header>
      <div class="px-3 py-2">
        <div class="flex justify-between">
          <VoltButton variant="text" draggable="true">
            <Icon name="fa-solid:grip-vertical" />
          </VoltButton>

          <VoltButton @click="handleDeleteBlock">
            <Icon name="fa-solid:trash" />
          </VoltButton>
        </div>

        <VoltDivider />
      </div>
    </template>

    <template #content>
      <h5 class="font-bold tracking-tight text-gray-900 dark:text-white mb-3">
        {{ title }}
      </h5>

      <slot />
    </template>
  </VoltCard>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'delete-block': [] }>()
defineProps<{ title: string }>()

function handleDeleteBlock () {
  emit('delete-block')
}
</script>
