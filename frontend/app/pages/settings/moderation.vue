<template>
  <section class="moderation">
    <SettingsHeader>
      Moderate what you see on YouTube
    </SettingsHeader>

    <!-- Blocked channels -->
    <SettingsCard title="Blocked channels" subtitle="Channels that you blocked and do not want to see">
      <VoltList v-if="hasChannels" :items="channels">
        <template #default="{ item }">
          <div class="flex justify-start items-center gap-3">
            <VoltAvatar image="/avatars/avatar1.png" shape="circle" size="large" />
            <span>{{ item.channel.name }}</span>
          </div>

          <VoltButton color="danger" variant="text">
            <Icon name="i-fa7-solid:arrow-left" />"['fas', 'fa-trash']" />
          </VoltButton>
        </template> 
      </VoltList>
    </SettingsCard>

    <!-- Blocked Keywords -->
    <SettingsCard title="Blocked keywords" subtitle="Block videos containing certain specific keywords (title, description)">
      <template #default>
        <div class="flex justify-start gap-2">
          <VoltInputText v-model="newKeyword.word" variant="outlined" placeholder="Enter a keyword to block" @keypress.enter="create" />
          <VoltSelect v-model="newKeyword.duration" :options="Array.from(blockingDurations)" />
        </div>

        <VoltLabel class="my-5">
          <template #input>
            <VoltToggleSwitch v-model="excludeFollowedAccounts" />
          </template>

          <template #label>
            Exclude accounts that you follow
          </template> 
        </VoltLabel>

        <VoltList v-if="hasKeywords" :items="keywords" item-label="word">
          <template #default="{ item }">
            <div class="flex justify-between items-center gap-2">
              <div class="space-x-2">
                <p>
                  {{ item.word }}
                </p>

                <VoltBadge>
                  {{ item.duration }}
                </VoltBadge>
              </div>

              <VoltButton @click="() => remove(i)">
                <Icon name="i-fa7-solid:trash" />
              </VoltButton>
            </div>
          </template>
        </VoltList>
      </template>
    </SettingsCard>

    <!-- Moderation Lists -->
    <SettingsCard title="Block lists" subtitle="Create shareable block lists">
      <template #default>
        <VoltAlert>
          Blocklists are lists of accounts that other users have create of
          accounts that they have associated to be problematic
        </VoltAlert>
        
        <div class="flex justify-center">
          <VoltButton color="secondary" variant="tonal" rounded @click="() => { showBlockLists=true }">
            Use or create block lists
          </VoltButton>
        </div>
      </template>
    </SettingsCard>

    <!-- Modals -->
    <ModalsModerationBlockLists v-model="showBlockLists" />
    <ModalsModerationCreateList v-model="showCreateList" />
  </section>
</template>

<script setup lang="ts">
import { useBlockedKeywords, useBlockedChannels } from '~/composables/use'
import { blockingDurations } from '~/data'

definePageMeta({
  layout: 'settings'
})

const { keywords, hasKeywords, create, remove, newKeyword, excludeFollowedAccounts } = useBlockedKeywords()
const { channels, hasChannels, showCreateList, showBlockLists } = useBlockedChannels()
</script>
