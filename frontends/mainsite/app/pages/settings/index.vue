<template>
  <section id="settings">
    <SettingsHeader>
      Choose how you appear on YouTube
    </SettingsHeader>

    <!-- Account Type -->
    <SettingsCard title="Account type" subtitle="Manage what you share on YouTube">
      <base-alert>
        You can choose to rank your account as a professional account. This will allow you to access 
        more features and tools on YouTube, such as advanced analytics and monetization options.
      </base-alert>

      <u-switch v-model="userSettings.is_professional" label="My account is professional or artistic" />

      {{ userSettings }}

      <div v-if="userSettings.is_professional" class="p-5 rounded-lg bg-slate-100 mt-10 ms-10">
        <template v-for="item in rankAs" :key="item">
          <u-checkbox v-model="userSettings.account_type" :value="item" />
        </template>
        
        <SettingsIndexProAdditionalInfo />
        <SettingsIndexArtistAdditionalInfo />
      </div>
    </SettingsCard>

    <SettingsCard title="Vos chaînes YouTube" subtitle="Manage what you share on YouTube">
      <div class="my-2">
        <nuxt-link to="/" class="bg-slate-50 p-5 rounded-lg flex items-center w-full">
          <u-avatar image="/avatars/avatar1.png" size="xl" alt="" />

          <p class="m-0">
            Channel name 1
          </p>
        </nuxt-link>
      </div>
    </SettingsCard>
  </section>
</template>

<script setup lang="ts">
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
