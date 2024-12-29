<template>
  <div class="card shadow-none border">
    <div v-if="isSaved" class="card-body">
      <p>Show me videos when...</p>
      <span class="badge badge-success">{{ conditionProxy.theme }}</span>
      <span>Matches these keywords...</span>
      <span v-for="keyword in conditionProxy.keywords" :key="keyword" class="badge badge-warning">{{ keyword }}</span>
      <span>Which appear in these sections of the video...</span>
      <span v-for="section in conditionProxy.video_sections" :key="section" class="badge badge-warning">{{ section }}</span>
    </div>
    
    <div v-else class="card-body">
      <div class="d-flex justify-content-end">
        <v-btn variant="tonal" rounded>
          <span v-if="conditionProxy.negation">Not</span>
          <span v-else>Not negated</span>

          <v-menu activator="parent">
            <v-list>
              <v-list-item v-for="item in negationOperators" :key="item" @click="handleNegation(item)">
                {{ item }}
              </v-list-item>
            </v-list>
          </v-menu>
        </v-btn>

        <v-btn class="ms-2" variant="outlined" rounded @click="$emit('delete-block', index)">
          <font-awesome-icon icon="trash" />
        </v-btn>
      </div>
      
      <!-- Themes -->
      <label class="fw-bold mb-2">Show me videos when...</label>
      <v-combobox v-model="conditionProxy.theme" :items="['Sports', 'TV shows']" variant="solo-filled" placeholder="Choose a general theme..." flat />

      <!-- Keywords -->
      <label class="fw-bold mb-2">Matches these keywords...</label>
      <div class="d-flex justify-content-between gap-2">
        <div class="w-25">
          <v-select v-model="conditionProxy.keyword_operator" :items="conditionOperators" variant="solo-filled" flat />
        </div>
        
        <v-autocomplete v-model="conditionProxy.keywords" :items="['NBA', 'WNBA']" placeholder="Select keywords..." variant="solo-filled" hide-selected chips multiple clearable flat>
          <v-text-field placeholder="Select keywords" />
        </v-autocomplete>
      </div>

      <!-- Keywords Additional Conditions -->
      <div v-if="conditionProxy.keywords_subconditions.length > 0" class="d-flex justify-content-end flex-column border p-2 rounded-2">
        <KeywordSubCondition v-for="(subCondition, i) in conditionProxy.keywords_subconditions" :key="i" :sub-condition="subCondition" />
      </div>

      <div class="d-flex justify-content-end my-3">
        <v-btn variant="tonal" @click="handleAddSubcondition">
          <font-awesome-icon icon="plus" class="me-2" />
          Add
        </v-btn>
      </div>

      <!-- Sections -->
      <label class="fw-bold mb-2">Which appear in these sections of the video...</label>
      <v-combobox v-model="conditionProxy.video_sections" :items="['Title', 'Description', 'Theme', 'Classfication']" variant="solo-filled" placeholder="Choose a general theme..." multiple hide-selected clearable flat chips />
      
      <v-btn variant="tonal" rounded>
        {{ conditionProxy.join_operator }}

        <v-menu activator="parent">
          <v-list>
            <v-list-item v-for="item in booleanOperators" :key="item" @click="handleJoinOperator(item)">
              {{ item }}
            </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
    </div>

    <div class="card-footer d-flex justify-content-end">
      <v-btn variant="tonal" @click="handleSaveBlock">
        <span v-if="isSaved">Edit</span>
        <span v-else>Save</span>
      </v-btn>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, PropType, provide } from 'vue';
import { AlgorithmConditionBlock, BooleanOperator, NegationOperators } from '@/types/user_settings';

import KeywordSubCondition from './KeywordSubCondition.vue';

const conditionOperators = [
  'Exact match',
  'Include related',
  'Approximate match',
  'Expression',
  'Exclude'
]

const booleanOperators = ['And', 'Or']

const negationOperators = ['Not negated', 'Not']

export default defineComponent({
  name: 'ConditionBlock',
  components: {
    KeywordSubCondition
  },
  props: {
    condition: {
      type: Object as PropType<AlgorithmConditionBlock>,
      required: true
    },
    index: {
      type: Number,
      required: true
    }
  },
  emits: {
    'delete-block' (_index: number) {
      return true
    }
  },
  setup(props) {
    const conditionProxy = ref(props.condition)
    const isSaved = ref(false)
    provide('conditionOperators', conditionOperators)
    return {
      isSaved,
      negationOperators,
      booleanOperators,
      conditionOperators,
      conditionProxy
    }
  },
  methods: {
    async handleSaveBlock() {
      this.isSaved = !this.isSaved
    },
    /**
     * 
     */
    handleJoinOperator(operator: BooleanOperator) {
      if (operator === 'And') {
        this.conditionProxy.join_operator = 'And'
      } else if (operator === 'Or') {
        this.conditionProxy.join_operator = 'Or'
      }
    },
    /**
     * 
     */
    handleNegation(operator: NegationOperators) {
      if (operator === 'Not') {
        this.conditionProxy.negation = true
      } else if (operator === 'Not negated') {
        this.conditionProxy.negation = false
      }
    },
    /**
     * 
     */
    handleAddSubcondition () {
      this.conditionProxy.keywords_subconditions.push({
        operator: 'Exact match',
        keywords: []
      })
    }
  }
})
</script>
