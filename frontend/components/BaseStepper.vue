<template>
  <div id="stepperForm" class="bs-stepper linear">
    <div class="bs-stepper-header" role="tablist">
      <template v-for="(step, i) in steps" :key="i">
        <div :class="activeState(i, step)" class="step">
          <button :id="`stepperFormTrigger${i}`" type="button" class="step-trigger" role="tab" aria-selected="true" @click="handleCurrentStep(i, step)">
            <span class="bs-stepper-circle">{{ step.id }}</span>
            <span class="bs-stepper-label">{{ step.title }}</span>
          </button>
        </div>
        
        <div v-if="!isLastStep(step)" class="bs-stepper-line" />
      </template>
    </div>
  </div>
</template>

<script lang="ts" setup>
import type { PropType } from 'vue'
import { onBeforeMount, ref } from 'vue';

interface Step {
  id: number
  title: string
}

const emit = defineEmits({
  'update:step' (_step: number) {
    return true
  }
})

const props = defineProps({
  steps: {
    type: Object as PropType<Step[]>,
    required: true
  },
  showState: {
    type: Boolean,
    default: false
  }
})

const numberOfSteps = ref(props.steps.length)
const lastStep = ref<Step>(props.steps[props.steps.length - 1])
const currentStep = ref<Step>()

const completedSteps = computed(() => {
  if (typeof currentStep.value === 'undefined') {
    return []
  } else {
    const currentStepIndex = props.steps.findIndex(x => x.title === currentStep.value.title)
    return props.steps.slice(0, currentStepIndex).map((x, i) => i)
  }
})

onBeforeMount(() => {
  currentStep.value = props.steps[0]
})

function handleCurrentStep (index: number, step: Step) {
  currentStep.value = step
  emit('update:step', index)
}

function activeState (index: number, step: Step): Record<string, boolean>[] {
  if (props.showState) {
    return [
      {
        active: completedSteps.value.includes(index)
      }
    ]
  } else {
    return [
      {
        active: step.title === currentStep.value.title
      }
    ]
  }
}

function isLastStep (step: Step) {
  return step.id === lastStep.value.id
}
</script>
