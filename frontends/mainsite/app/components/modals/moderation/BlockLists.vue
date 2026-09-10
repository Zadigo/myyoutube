<template>
  <u-modal v-model:open="show" modal>
    <template #header>
      <h3 class="text-lg font-semibold">Block lists</h3>
    </template>

    <template #body>
      <u-input class="w-full mb-10" placeholder="Search by list names..." />
      
      <div class="flex items-center gap-2 mb-3">
        <u-button :disabled="!showBlockedItems" rounded @click="showBlockedItems=false">
          <Icon name="i-fa7-solid:arrow-left" />
        </u-button>
  
        <u-button :disabled="!showBlockedItems" class="mb-3" rounded>
          Use this list
        </u-button>
        
        <u-button class="mb-3" rounded @click="show=true">
          Create my list
        </u-button>
      </div>
      
      <base-list-group :items="[{ label: 'Blocked Item 1' }, { label: 'Blocked Item 2' }]" v-if="showBlockedItems">
        <template #default>
          Something
        </template>
      </base-list-group>
  
      <base-list-group :items="[{ label: 'Hitchens' }, { label: 'Dawkins' }]" v-else item-label="label">
        <template #default="{ item }">
          <a :key="item.label" class="flex justify-between" @click.prevent="() => { showBlockedItems=true }">
            <span>Utilisateurs {{ item.label }}</span>
            
            <div class="popularity">
              <Icon v-for="x in 10" :key="x" name="i-fa7-solid:star" />
            </div>
          </a>
        </template>
      </base-list-group>
    </template>
  </u-modal>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })

const showBlockedItems = ref<boolean>(false)
</script>
