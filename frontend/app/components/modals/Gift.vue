<template>
  <VoltDialog id="gifts" v-model:visible="show" modal>
    <VoltAlert class="mb-4" variant="warning">
      You have purchased no gifts yet. You can buy gifts here before pursuing.
    </VoltAlert>

    <VoltButton class="my-2">
      Purchase
    </VoltButton>

    <div class="grid grid-cols-3 gap-2">
      <article v-for="i in 10" id="donation" :key="i" class="font-light">
        <VoltCard class="shadow-none border border-slate-50 text-center">
          <template #content>
            Gift 1
          </template>
        </VoltCard>
      </article>
    </div>
  </VoltDialog>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>

<style lang="scss" scoped>
#donation {
  cursor: pointer;
}

#donation:hover {
  opacity: .9;
}
</style>
