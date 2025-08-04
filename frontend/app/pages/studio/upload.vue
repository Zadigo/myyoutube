<template>
  <section id="uploads" class="container mx-auto px-5">
    <VoltCard class="shadow-sm">
      <template #content>
        <div class="card">
          <VoltStepper v-model:value="activeStep">
            <VoltStepItem value="1">
              <VoltStep>
                <h4 class="font-bold">
                  Upload video
                </h4>
              </VoltStep>
              <VoltStepPanel v-slot="{ activateCallback }">
                <StudioUpload :callback="() => activateCallback('2')" />
              </VoltStepPanel>
            </VoltStepItem>

            <VoltStepItem value="2">
              <VoltStep>
                <h4 class="font-bold">
                  Video Information
                </h4>
              </VoltStep>
              <VoltStepPanel v-slot="{ activateCallback }">
                <Suspense>
                  <StudioVideoInformation :callback="() => activateCallback('3')" />
                </Suspense>

                <div class="flex py-6 gap-2">
                  <VoltSecondaryButton label="Back" @click="() => activateCallback('1')" />
                  <VoltButton label="Next" @click="() => activateCallback('3')" />
                </div>
              </VoltStepPanel>
            </VoltStepItem>
            
            <VoltStepItem value="3">
              <VoltStep>
                <h4 class="font-bold">
                  Visibility
                </h4>
              </VoltStep>
              <VoltStepPanel v-slot="{ activateCallback }">
                <StudioVideoVisibility :callback="() => activateCallback('4')" />
              </VoltStepPanel>
            </VoltStepItem>

            <VoltStepItem value="4">
              <VoltStep>
                <h4 class="font-bold">
                  Finalize
                </h4>
              </VoltStep>
              <VoltStepPanel v-slot="{ activateCallback }">
                <StudioFinalize :callback="() => activateCallback('5')" />
              </VoltStepPanel>
            </VoltStepItem>
          </VoltStepper>
        </div>
      </template>

      <template #footer>
        {{ activeStep }}
        <VoltButton :disabled="!isFinalStep" @click="studioStore.submit">
          Complete
        </VoltButton>
      </template>
    </VoltCard>
  </section>
</template>

<script lang="ts" setup>
const studioStore = useStudioStore()
const { newVideo } = storeToRefs(studioStore)

const activeStep = ref<number>(1)
const isFinalStep = computed(() => activeStep.value === 4)
</script>
