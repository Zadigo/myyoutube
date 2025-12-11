<template>
  <div class="relative">
    <slot :attrs="{ factCheck, generalAlert }" />

    <!-- Fact checking -->
    <div v-if="showFactCheck" id="fact-checking" class="absolute z-50 bottom-30 left-6/12 -translate-x-6/12 p-5 shadow-sm rounded-lg bg-primary-700 dark:bg-primary-900 text-primary-50">
      <h2 class="text-3xl flex items-center gap-2">
        Fact checking (0:15)
      </h2>

      <div class="flex gap-2">
        <volt-button disabled>
          <icon name="lucide:thumbs-up" />
          15.6K
        </volt-button>
        
        <volt-button disabled>
          <icon name="lucide:thumbs-down" />
          200
        </volt-button>
      </div>

      <p class="mt-2 font-light">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Facere doloribus 
        sapiente pariatur eligendi commodi cupiditate, quo consequatur ut, quae beatae 
        aspernatur reprehenderit, corrupti tempore cumque facilis officiis inventore 
        repellat ullam.
      </p>
    </div>

    <div v-if="showGeneralAlert" id="general-alert" class="absolute z-50 top-2 right-2 rounded-lg bg-primary-700 dark:bg-primary-900 text-primary-50 max-w-100 p-2">
      <div class="flex items-center justify-around gap-4">
        <div>
          <volt-avatar src="/avatars/avatar1.png" shape="circle"/>
        </div>
        <p class="">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ex tempore aperiam nostrum</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const showFactCheck = refAutoReset(false, 3000)
const showGeneralAlert = refAutoReset(false, 3000)

interface FactCheckData { name: string, time: string, content: string }
type GeneralAlertData = Omit<FactCheckData, 'time'> & { url: string }

const factCheckData = ref<FactCheckData>()
const generalAlertData = ref<GeneralAlertData>()

function factCheck(content: FactCheckData) {
  showFactCheck.value = true
  factCheckData.value = content
}

function generalAlert(content: GeneralAlertData) {
  showGeneralAlert.value = true
  generalAlertData.value = content
}
</script>
