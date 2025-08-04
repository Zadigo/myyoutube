<template>
  <VoltCard class="mt-1 shadow-sm">
    <template #header>
      <div class="p-5">
        <h3 class="font-bold text-2xl">{{ title }}</h3>
        <p class="font-light">
          {{ subtitle }}
        </p>

        <VoltDivider />
      </div>
    </template>

    <template #content>
      <slot />
    </template>
  </VoltCard>
</template>

<script setup lang="ts">
defineProps<{ title : string; subtitle: string }>()
</script>
