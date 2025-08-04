<template>
  <div :class="theme.list">
    <template v-for="item in items" :key="item[itemLabel]">
      <slot :item="item">
        <div :class="theme.listItem">
          <span>{{ item[itemLabel] }}</span>
        </div>
      </slot>
    </template>
  </div>
</template>

<script setup lang="ts" generic="T extends Record<string, unknown>">
const { itemLabel = 'id' } = defineProps<{ items: T[], itemLabel?: string }>()

const theme = ref({
  list: [
    `rounded-lg border border-slate-200 
      dark:border-slate-700 bg-white dark:bg-slate-800 p-4 shadow-sm`,
  ],
  listItem: [
    `flex items-center px-2 py-4 
    border-b border-slate-200 dark:border-slate-700`,
  ]
})
</script>
