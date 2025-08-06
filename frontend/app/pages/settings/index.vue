<template>
  <section id="settings">
    <SettingsHeader>
      Choose how you appear on YouTube
    </SettingsHeader>

    <!-- Account Type -->
    <SettingsCard title="Account type" subtitle="Manage what you share on YouTube">
      <VoltAlert>
        You can choose to rank your account as a professional account. This will allow you to access 
        more features and tools on YouTube, such as advanced analytics and monetization options.
      </VoltAlert>

      <VoltLabel class="mt-5">
        <template #input>
          <VoltToggleSwitch v-model="userSettings.is_professional" />
        </template>

        <template #label>
          My account is professional or artistic
        </template>
      </VoltLabel>

      {{ userSettings }}

      <div v-if="userSettings.is_professional" class="p-5 rounded-lg bg-slate-100 mt-10 ms-10">
        <VoltLabel v-for="item in rankAs" :key="item">
          <VoltCheckbox v-model="userSettings.account_type" :value="item" />
          <label class="py-3 pe-5 font-semibold">
            {{ item }}
          </label>
        </VoltLabel>
        
        <SettingsIndexProAdditionalInfo />
        <SettingsIndexArtistAdditionalInfo />
      </div>
    </SettingsCard>

    <SettingsCard title="Vos chaînes YouTube" subtitle="Manage what you share on YouTube">
      <div class="my-2">
        <NuxtLink to="/" class="bg-slate-50 p-5 rounded-lg flex items-center w-full">
          <VoltAvatar image="/avatars/avatar1.png" shape="circle" size="large" alt="" />

          <p class="m-0">
            Channel name 1
          </p>
        </NuxtLink>
      </div>
    </SettingsCard>
  </section>
</template>

<script setup lang="ts">
import { rankAs } from '~/data'

definePageMeta({
  layout: 'settings'
})

const { data } = useFetch('/api/account/viewer-profile', {
  baseURL: useRuntimeConfig().public.djangoProdUrl,
  method: 'GET'
})

const settingsStore = useSettingsStore()
const { userSettings } = storeToRefs(settingsStore)

const store = useViewerProfile()
const { profileData } = storeToRefs(store)

if (data.value) {
  profileData.value = data.value
}
</script>
