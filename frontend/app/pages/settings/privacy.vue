<template>
  <section id="algorithm">
    <SettingsHeader>
      Privacy
    </SettingsHeader>

    <SettingsCard class="shadow-sm" title="General" subtitle="Manage what you share on YouTube">
      <VoltList>
        <template #body="{ theme }">
          <div :class="theme">
            <VoltLabel>
              <VoltToggleSwitch inset hide-details />
              <label>Keep all my saved playlists private</label>
            </VoltLabel>
          </div>

          <div :class="theme">
            <VoltLabel>
              <VoltToggleSwitch />
              <label>Keep all my subscriptions private</label>
            </VoltLabel>
          </div>
        </template>
      </VoltList>
    </SettingsCard>

    <SettingsCard class="shadow-sm" title="Ad personalization" subtitle="Manage what you share on YouTube">
      <p>Google makes your ads more useful on Google services (such as Search or YouTube), and on websites & apps that partner with Google to show ads</p>
      
      <VoltList>
        <template #body="{ theme }">
          <div :class="theme">
            <VoltLabel>
              <VoltToggleSwitch />
              <label>Personalize ads</label>
            </VoltLabel>
          </div>
        </template>
      </VoltList>

      <h4 class="mt-5">
        How your ads are personalized
      </h4>

      <p>
        Ads are based on personal info you've added to your 
        Google Account, data from advertisers that partner with Google, 
        and Google's estimation of your interests. Choose any factor to learn 
        more or update your preferences. Learn how to control the ads you see
      </p>

      <VoltButton variant="text">
        Show categories
      </VoltButton>
    </SettingsCard>

    <VoltDivider class="my-5" />

    <h2>Sensitive ad categories on YouTube</h2>
    <p>Select the categories for which you want to see less of</p>

    <VoltList :items="Array.from(sensitiveCategories).map(x => ({ label: x }))">
      <template #item="{ item }">
        <VoltLabel>
          <VoltToggleSwitch />
          <label>{{ item.label }}</label>
        </VoltLabel>
      </template>
    </VoltList>
  </section>
</template>

<script setup lang="ts">
import { sensitiveCategories } from '~/data/constants'
definePageMeta({
  layout: 'settings'
})
</script>
