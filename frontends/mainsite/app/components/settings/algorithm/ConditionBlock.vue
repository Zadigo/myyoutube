<template>
  <u-card id="condition" class="shadow-none border border-slate-200">
    <settings-algorithm-saved-condition-block v-if="isSaved" :condition="conditionProxy" />
    
    <div v-else>
      <div v-if="conditionProxy">
        <header class="flex justify-end">
          <volt-dropdown-button id="negation" :items="negationOperatorsMenuItems">
            <span v-if="conditionProxy.negation">Not</span>
            <span v-else>Not negated</span>
          </volt-dropdown-button>

          <u-button class="ms-2 rounded-full" variant="outline" @click="() => emit('delete-block', index)">
            <icon name="i-fa7-solid:trash" />
          </u-button>
        </header>

        {{ index }}
        
        <!-- Themes -->
        <div id="themes" class="w-full">
          <p class="font-bold mb-2">Show me videos when...</p>
          <volt-auto-complete v-model="conditionProxy.theme" :suggestions="Array.from(defaultMainCategories)" placeholder="Choose a general theme..." />
        </div>

        <!-- Keywords -->
        <!-- TODO: Create template with this -->
        <div class="p-5 bg-slate-50 rounded-lg my-3">
          <p class="font-bold mb-2">Matches these keywords...</p>
          <div class="flex justify-between gap-2">            
            <volt-select v-model="conditionProxy.keyword_operator" :options="Array.from(keywordOperators)" class="w-3/8" />

            <div class="w-7/8">
              <volt-auto-complete v-model="conditionProxy.keywords" :items="['NBA', 'WNBA']" placeholder="Select keywords..." />
            </div>
          </div>

          <!-- Subconditions -->
          <div v-if="conditionProxy.keywords_subconditions.length > 0" class="bg-slate-100 rounded-lg my-3 p-5 space-y-2 w-7/8">
            <div class="flex justify-start">
              <volt-dropdown-button id="operator" :items="joinOperatorsMenuItems">
                {{ conditionProxy.join_operator }}
              </volt-dropdown-button>
            </div>
            
            <settings-algorithm-keyword-sub-condition v-for="(subCondition, i) in conditionProxy.keywords_subconditions" :key="i" :sub-condition="subCondition" />

            <div class="flex justify-end my-3">
              <u-button variant="subtle" @click="handleAddSubcondition">
                <icon name="lucide:plus" class="me-2" />
                New condition
              </u-button>
            </div>
          </div>
          
          <div class="flex justify-end my-3">
            <u-button variant="subtle" @click="handleAddSubcondition">
              <icon name="lucide:plus" class="me-2" />
              Add
            </u-button>
          </div>

        </div>

        <!-- Sections -->
        <div>
          <p class="font-bold mb-2">Which appear in these sections of the video...</p>
          <volt-select v-model="conditionProxy.video_sections" :options="videoSections" placeholder="Sections" />
        </div>
      </div>
    </div>

    <template #footer>
      <div class="flex justify-end">
        <u-button variant="subtle" @click="handleSaveBlock">
          <span v-if="isSaved">Edit</span>
          <span v-else>Save</span>
        </u-button>
      </div>
    </template>
  </u-card>
</template>

<script setup lang="ts">
import type { MenuItem } from 'primevue/menuitem'
import { useMenuItems } from '~/composables/use'
import { defaultMainCategories, keywordOperators, type JoinOperators } from '~/constants'

const negationOperators = [
  'Not negated',
  'Not'
] as const

type NegationOperators = (typeof negationOperators)[number]

interface NegationOperatorsMenuItems extends MenuItem {
  label: NegationOperators
}

interface JoinOperatorsMenuItems extends MenuItem {
  label: JoinOperators
}

const props = defineProps<{ index: number }>()
const emit = defineEmits<{ 'delete-block': [index: number] }>()

const isSaved = ref<boolean>(false)

async function handleSaveBlock() {
  isSaved.value = !isSaved.value
}

const algorithmStore = useAlgorithmSettingsStore()
const conditionProxy = algorithmStore.getCurrentBlock(props.index)

/**
 * Function that adds a new subcondition to the current condition block
 */
function handleAddSubcondition() {
  if (conditionProxy.value) {
    conditionProxy.value.keywords_subconditions.push({
      operator: 'Exact match',
      keywords: []
    })
  }
}

// Menu Items

const videoSections = ['Title', 'Description', 'Theme', 'Classfication']

const negationOperatorsMenuItems: NegationOperatorsMenuItems[] = [
  {
    label: 'Not negated',
    command: () => {
      if (conditionProxy.value) {
        conditionProxy.value.negation = false
      }
    }
  },
  {
    label: 'Not',
    command: () => {
      if (conditionProxy.value) {
        conditionProxy.value.negation = true
      }
    }
  }
]

const joinOperatorsMenuItems: JoinOperatorsMenuItems[] = [
  {
    label: 'And',
    command: () => {
      if (conditionProxy.value) {
        conditionProxy.value.join_operator = 'And'
      }
    }
  },
  {
    label: 'Or',
    command: () => {
      if (conditionProxy.value) {
        conditionProxy.value.join_operator = 'Or'
      }
    }
  }
]
</script>
