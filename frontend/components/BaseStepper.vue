<template>
  <div id="stepperForm" class="bs-stepper linear">
    <div class="bs-stepper-header" role="tablist">
      <template v-for="(step, i) in steps" :key="i">
        <div :class="activeState(index, step)" class="step">
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

<script lang="ts">
import type { PropType } from 'vue'
import { onBeforeMount, ref } from 'vue';

interface Step {
  id: number
  title: string
}

export default defineNuxtComponent({
  name: 'BaseStepper',
  props: {
    steps: {
      type: Object as PropType<Step[]>,
      required: true
    },
    showState: {
      type: Boolean,
      default: false
    }
  },
  emits: {
    'update:step' (_step: number) {
      return true
    }
  },
  setup(props) {
    const numberOfSteps = ref(props.steps.length)
    const lastStep = ref<Step>(props.steps[props.steps.length - 1])
    const currentStep = ref<Step>()

    onBeforeMount(() => {
      currentStep.value = props.steps[0]
    })

    return {
      numberOfSteps,
      currentStep,
      isLastStep (step: Step) {
        return step.id === lastStep.value.id
      }
    }
  },
  computed: {
    completedSteps () {
      if (typeof this.currentStep === 'undefined') {
        return []
      } else {
        const currentStepIndex = this.steps.findIndex(x => x.title === this.currentStep.title)
        return this.steps.slice(0, currentStepIndex).map((x, i) => i)
      }
    }
  },
  methods: {
    handleCurrentStep (index: number, step: Step) {
      this.currentStep = step
      this.$emit('update:step', index)
    },
    activeState (index: number, step: Step): Record<string, boolean>[] {
      if (this.showState) {
        return [
          {
            active: this.completedSteps.includes(index)
          }
        ]
      } else {
        return [
          {
            active: step.title === this.currentStep.title
          }
        ]
      }
    }
  }
})
</script>
