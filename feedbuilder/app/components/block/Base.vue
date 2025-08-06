<template>
  <BaseCard>
    <template #header>
      <div class="flex justify-between">
        <BaseButton variant="text" draggable="true">
          <Icon name="fa-solid:grip-vertical" />
        </BaseButton>

        <BaseButton variant="tonal" @click="handleDeleteBlock">
          <Icon name="fa-solid:trash" />
        </BaseButton>
      </div>

      <h5 class="mb-2 text-1xl font-bold tracking-tight text-gray-900 dark:text-white">
        {{ title }}
      </h5>
    </template>

    <template #default>
      <div class="card-body">
        <div class="row">
          <slot />
        </div>
      </div>
    </template>
  </BaseCard>
</template>

<script setup lang="ts">
const emit = defineEmits({
  'delete-block' () {
    return true
  }
})

defineProps({
  title: {
    type: String
  }
})

function handleDeleteBlock () {
  emit('delete-block')
}
</script>
