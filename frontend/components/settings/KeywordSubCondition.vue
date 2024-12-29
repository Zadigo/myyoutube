<template>
  <div class="row gx-1 mb-1 d-flex justify-content-end align-items-center">
    <div class="col-3">
      <v-select v-model="conditionBlockProxy.operator" :items="conditionOperators" variant="solo-filled" hide-details flat />
    </div>

    <div class="col-5">
      <v-combobox v-model="conditionBlockProxy.keywords" :items="['NBA', 'WNBA']" variant="solo-filled" hide-details hide-selected flat chips multiple />
    </div>

    <div class="col-auto">
      <v-btn size="x-large" variant="text" color="dark">
        <font-awesome-icon icon="trash" />
      </v-btn>
    </div>
  </div>
</template>

<script lang="ts">
import { KeywordOperatorArray, KeywordSubcondition } from '@/types/user_settings';
import { computed, defineComponent, inject, PropType } from 'vue';

export default defineComponent({
  name: 'KeywordSubcondition',
  props: {
    subCondition: {
      type: Object as PropType<KeywordSubcondition>,
      required: true
    }
  },
  setup(props) {
    const conditionOperators = inject<KeywordOperatorArray>('conditionOperators')
    const conditionBlockProxy = computed({
      get: () => props.subCondition,
      set: (newValue) => console.log(newValue)
    })
    return {
      conditionOperators,
      conditionBlockProxy
    }
  }
})
</script>
