<template>
  <VoltDialog v-model:visible="show" modal>
    <form id="payment" class="space-y-2" @submit.prevent>
      <input type="text" autocomplete="" placeholder="Card Number" class="mb-4" />

      <VoltInputText autocomplete="cc-number" class="w-full" placeholder="Card Number" />

      <div class="flex gap-2">
        <VoltInputText autocomplete="cc-exp-month" placeholder="MM" />
        <VoltInputText autocomplete="cc-exp-year" placeholder="YYYY" />
      </div>

      <VoltInputText autocomplete="cc-csc" placeholder="CVC" class="w-full" />
      <VoltInputText autocomplete="cc-name" placeholder="Cardholder Name" class="w-full" />
    </form>

    <template #footer>
      <VoltButton @click="show = false">
        Disagree
      </VoltButton>

      <VoltButton @click="show = false">
        Agree
      </VoltButton>
    </template>
  </VoltDialog>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
