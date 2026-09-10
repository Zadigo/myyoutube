<template>
  <u-modal v-model:open="show" modal>
    <template #body>
      <form id="payment" class="space-y-2" @submit.prevent>
        <input type="text" autocomplete="" placeholder="Card Number" class="mb-4" />
  
        <u-input autocomplete="cc-number" class="w-full" placeholder="Card Number" />
  
        <div class="flex gap-2">
          <u-input autocomplete="cc-exp-month" placeholder="MM" />
          <u-input autocomplete="cc-exp-year" placeholder="YYYY" />
        </div>
  
        <u-input autocomplete="cc-csc" placeholder="CVC" class="w-full" />
        <u-input autocomplete="cc-name" placeholder="Cardholder Name" class="w-full" />
      </form>
    </template>

    <template #footer>
      <u-button @click="show = false">
        Disagree
      </u-button>

      <u-button @click="show = false">
        Agree
      </u-button>
    </template>
  </u-modal>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
