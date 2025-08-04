<template>
  <VoltCard id="condition" class="shadow-none border border-slate-200">
    <template #content>
      <SettingsAlgorithmSavedConditionBlock v-if="isSaved" :condition="conditionProxy" />
      
      <div v-else>
        <div v-if="conditionProxy">
          <header class="flex justify-end">
            <VoltDropdownButton id="negation" :items="Array.from(negationOperators).map(x => ({ label: x }))">
              <span v-if="conditionProxy.negation">Not</span>
              <span v-else>Not negated</span>
            </VoltDropdownButton>

            <VoltButton class="ms-2" variant="outlined" rounded @click="() => emit('delete-block', index)">
              <Icon name="i-fa7-solid:trash" />
            </VoltButton>
          </header>

          {{ index }}
          
          <!-- Themes -->
          <div id="themes" class="w-full">
            <p class="font-bold mb-2">Show me videos when...</p>
            <VoltAutoComplete v-model="conditionProxy.theme" :suggestions="Array.from(defaultMainCategories)" placeholder="Choose a general theme..." />
          </div>

          <!-- Keywords -->
          <!-- TODO: Create template with this -->
          <div class="p-5 bg-slate-50 rounded-lg my-3">
            <p class="font-bold mb-2">Matches these keywords...</p>
            <div class="flex justify-between gap-2">            
              <VoltSelect v-model="conditionProxy.keyword_operator" :options="Array.from(keywordOperators)" class="w-3/8" />

              <div class="w-7/8">
                <VoltAutoComplete v-model="conditionProxy.keywords" :items="['NBA', 'WNBA']" placeholder="Select keywords..." />
              </div>
            </div>

            <!-- Subconditions -->
            <div v-if="conditionProxy.keywords_subconditions.length > 0" class="bg-slate-100 rounded-lg my-3 p-5 space-y-2 w-7/8">
              <!-- v-model="conditionProxy.video_sections" -->
              <VoltDropdownButton id="operator" :items="Array.from(joinOperators).map(x => ({ label: x }))">
                {{ conditionProxy.join_operator }}
              </VoltDropdownButton>
              
              <SettingsAlgorithmKeywordSubCondition v-for="(subCondition, i) in conditionProxy.keywords_subconditions" :key="i" :sub-condition="subCondition" /> 
              
              <div class="flex justify-end my-3">
                <VoltButton variant="tonal" @click="handleAddSubcondition">
                  <Icon name="i-fa7-solid:plus" class="me-2" />
                  Add
                </VoltButton>
              </div>
            </div>

          </div>

          <!-- Sections -->
          <div>
            <p class="font-bold mb-2">Which appear in these sections of the video...</p>
            <VoltSelect v-model="conditionProxy.video_sections" :options="['Title', 'Description', 'Theme', 'Classfication']" placeholder="Sections" />
          </div>
        </div>
      </div>
    </template>

    <template #footer>
      <div class="flex justify-end">
        <VoltButton variant="tonal" @click="handleSaveBlock">
          <span v-if="isSaved">Edit</span>
          <span v-else>Save</span>
        </VoltButton>
      </div>
    </template>
  </VoltCard>
</template>

<script setup lang="ts">
import { defaultMainCategories, joinOperators, keywordOperators, negationOperators, type JoinOperators, type NegationOperators } from '~/data';

const props = defineProps<{ index: number }>()
const emit = defineEmits<{ 'delete-block': [index: number] }>()

const isSaved = ref<boolean>(false)

async function handleSaveBlock() {
  isSaved.value = !isSaved.value
}

const algorithmStore = useAlgorithmSettingsStore()
const conditionProxy = algorithmStore.getCurrentBlock(props.index)
console.log('test', algorithmStore.getCurrentBlock(toRef(0)).value)

/**
 * 
 */
function handleJoinOperator(operator: JoinOperators) {
  if (conditionProxy.value) {
    if (operator === 'And') {
      conditionProxy.value.join_operator = 'And'
    } else if (operator === 'Or') {
      conditionProxy.value.join_operator = 'Or'
    }
  }
}

/**
 * 
 */
function handleNegation(operator: NegationOperators) {
  if (conditionProxy.value) {
    if (operator === 'Not') {
      conditionProxy.value.negation = true
    } else if (operator === 'Not negated') {
      conditionProxy.value.negation = false
    }
  }
}

/**
 * 
 */
function handleAddSubcondition() {
  if (conditionProxy.value) {
    conditionProxy.value.keywords_subconditions.push({
      operator: 'Exact match',
      keywords: []
    })
  }
}
</script>
