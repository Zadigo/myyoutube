<template>
  <VoltDialog v-model:visible="show" modal>
    <VoltInputText placeholder="Search by list names..." flat />
    
    <div class="flex gap-2 mb-3">
      <VoltButton :disabled="!showBlockedItems" rounded @click="showBlockedItems=false">
        <Icon icon="i-fa7-solid:arrow-left" />
      </VoltButton>

      <VoltButton :disabled="!showBlockedItems" class="mb-3" rounded>
        Use this list
      </VoltButton>
      
      <VoltButton class="mb-3" rounded @click="show=true">
        Create my list
      </VoltButton>
    </div>
    
    <div v-if="showBlockedItems" class="list-group">
      <div class="list-group-item">
        Something
      </div>
    </div>

    <div v-else class="list-group">
      <a v-for="i in 15" :key="i" href="#" class="list-group-item list-group-item-action p-3 d-flex justify-content-between align-items-center" @click.prevent="showBlockedItems=true">
        <span>Utilisateurs Hitchens</span>
        
        <div class="popularity">
          <Icon v-for="x in 10" :key="x" icon="i-fa7-solid:star" />
        </div>
      </a>
    </div>
  </VoltDialog>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })

const showBlockedItems = ref<boolean>(false)
</script>
