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

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'SettingsCard',
  props: {
    title: {
      type: String,
      required: true
    },
    subtitle: {
      type: String,
      required: true
    }
  }
})
</script>
