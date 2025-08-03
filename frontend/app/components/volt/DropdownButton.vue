<template>
  <div class="card flex justify-center">
    <slot :attrs="{ toggle }" name="button">
      <VoltButton :aria-controls="id" type="button" aria-haspopup="true" @click="toggle($event)">
        <slot />
      </VoltButton>
    </slot>
    <VoltMenu :id="id" ref="menuEl" :model="items" :popup="true" />
  </div>
</template>

<script setup lang="ts">
import type { MenuItem } from 'primevue/menuitem'

const menuEl = useTemplateRef('menuEl')

defineProps<{ id: string, items: MenuItem[] }>()

function toggle(e: MouseEvent) {
  if (menuEl.value) {
    menuEl.value.toggle(e)
  }
}

defineExpose({
  toggle
})
</script>
