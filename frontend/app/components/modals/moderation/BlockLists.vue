<template>
  <VoltDialog v-model:visible="show" modal>
    <template #header>
      <h3 class="text-lg font-semibold">Block lists</h3>
    </template>

    <VoltInputText class="w-full mb-10" placeholder="Search by list names..." />
    
    <div class="flex gap-2 mb-3">
      <VoltButton :disabled="!showBlockedItems" rounded @click="showBlockedItems=false">
        <Icon name="i-fa7-solid:arrow-left" />
      </VoltButton>

      <VoltButton :disabled="!showBlockedItems" class="mb-3" rounded>
        Use this list
      </VoltButton>
      
      <VoltButton class="mb-3" rounded @click="show=true">
        Create my list
      </VoltButton>
    </div>
    
    <VoltList v-if="showBlockedItems">
      <template #default>
        Something
      </template>
    </VoltList>

    <VoltList v-else item-label="name">
      <template #body="{ theme }">
        <a v-for="item in [{ id: 1, name: 'Hitchens' }, { id: 2, name: 'Dawkins' }]" :key="item.id" :class="theme" class="flex justify-between" @click.prevent="() => { showBlockedItems=true }">
          <span>Utilisateurs {{ item.name }}</span>
          
          <div class="popularity">
            <Icon v-for="x in 10" :key="x" name="i-fa7-solid:star" />
          </div>
        </a>
      </template>
    </VoltList>
  </VoltDialog>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })

const showBlockedItems = ref<boolean>(false)
</script>
