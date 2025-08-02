<template>
  <div class="card mt-1">
    <div class="card-header">
      <h3>{{ title }}</h3>
      <p class="m-0 text-muted">
        {{ subtitle }}
      </p>
    </div>

    <div class="card-body">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  title: {
    type: String,
    required: true
  },
  subtitle: {
    type: String,
    required: true
  }
})
</script>
