<template>
  <section class="moderation">
    <div class="row">
      <div class="col-8 offset-md-2">
        <div class="card mb-2">
          <div class="card-body">
            <h2>
              Customize your viewing experience
            </h2>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <!-- Block channels -->
      <div class="col-8 offset-md-2">
        <settings-card title="Blocked channels" subtitle="Channels that you blocked and do not want to see">
          <template #default>
            <div class="list-group">
              <div v-for="blockedChannel in blockedChannels" :key="blockedChannel.channel.reference" class="list-group-item d-flex justify-content-between align-items-center">
                <div class="d-flex justify-content-start align-items-center gap-3">
                  <v-avatar image="/avatar1.png" size="20" />
                  <span>{{ blockedChannel.channel.name }}</span>
                </div>

                <v-btn color="danger" variant="text">
                  <font-awesome :icon="['fas', 'fa-trash']" />
                </v-btn>
              </div>
            </div>
          </template>
        </settings-card>
      </div>

      <!-- Blocked Keywords -->
      <div class="col-8 offset-md-2">
        <settings-card title="Blocked keywords" subtitle="Block videos containing certain specific keywords (title, description)">
          <template #default>
            <div class="d-flex justify-content-between gap-2">
              <v-text-field v-model="blockedKeyword.word" variant="outlined" placeholder="Enter a keyword to block" @keypress.enter="handleAddBlockedKeyWord" />
              
              <div class="w-50">
                <v-select v-model="blockedKeyword.duration" :items="blockingDurations" variant="outlined" :auto-select-first="true" />
              </div>
            </div>

            <v-switch v-model="excludeFollowedAccounts" label="Exclude accounts that you follow" inset />

            <div class="list-group">
              <div v-for="(item, i) in blockedKeywords" :key="i" class="list-group-item d-flex justify-content-between align-items-center">
                <div class="d-flex gap-2">
                  <span>
                    {{ item.word }}
                  </span>

                  <span class="badge badge-secondary">
                    {{ item.duration }}
                  </span>
                </div>

                <v-btn variant="text" rounded @click="handleRemoveBlockedKeyword(i)">
                  <font-awesome icon="trash" />
                </v-btn>
              </div>
            </div>
          </template>
        </settings-card>
      </div>

      <!-- Moderation Lists -->
      <div class="col-8 offset-md-2">
        <settings-card title="Block lists" subtitle="Create shareable block lists">
          <template #default>
            <p class="fw-light">
              Blocklists are lists of accounts that other users have create of
              accounts that they have associated to be problematic
            </p>
            
            <div class="d-flex justify-content-center">
              <v-btn color="secondary" variant="tonal" rounded @click="showBlockLists=true">
                Use or create block lists
              </v-btn>
            </div>
          </template>
        </settings-card>
      </div>
    </div>

    <!-- Modals -->
    <Teleport to="body">        
      <v-dialog v-model="showBlockLists" width="900" scrollable>
        <v-card>
          <v-card-item>
            <h2 class="h4">
              Block lists
            </h2>
          </v-card-item>
          
          <v-card-text>
            <v-text-field variant="solo-filled" placeholder="Search by list names..." flat />
            
            <div class="d-flex gap-2 mb-3">
              <v-btn :disabled="!showBlockedItems" color="dark" variant="tonal" rounded @click="showBlockedItems=false">
                <font-awesome icon="arrow-left" />
              </v-btn>

              <v-btn :disabled="!showBlockedItems" class="mb-3" color="dark" variant="tonal" rounded>
                Use this list
              </v-btn>
              
              <v-btn class="mb-3" color="dark" variant="tonal" rounded @click="showCreateList=true">
                Create my list
              </v-btn>
            </div>
            
            <div v-if="showBlockedItems" class="list-group">
              <div class="list-group-item">
                Something
              </div>
            </div>

            <div v-else class="list-group">
              <a v-for="i in 15" :key="i" href="#" class="list-group-item list-group-item-action p-3 d-flex justify-content-between align-items-center" @click.prevent="showBlockedItems=true">
                <span>Utilisateurs Hitchens</span>
                
                <div class="popularity">
                  <font-awesome v-for="x in 10" :key="x" icon="star" />
                </div>
              </a>
            </div>
          </v-card-text>
        </v-card>
      </v-dialog>
    </Teleport>

    <Teleport to="body">
      <v-dialog v-model="showCreateList" :persistent="true" width="400">
        <v-card>
          <v-card-item>
            <h2 class="h4">
              New list
            </h2>
          </v-card-item>

          <v-card-text>
            <v-text-field variant="solo-filled" placeholder="Name of your list" flat />
            <v-text-field variant="solo-filled" placeholder="Search for users..." flat />
          </v-card-text>
          
          <v-card-actions>
            <v-btn variant="tonal" @click="showCreateList=false">
              Cancel
            </v-btn>

            <v-btn variant="tonal" @click="showCreateList=false">
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </Teleport>>
  </section>
</template>

<script setup lang="ts">
import type { BlockedChannel } from '@/types';
import { useRefHistory } from '@vueuse/core';
import { ref } from 'vue';

import SettingsCard from '~/components/settings/Card.vue';

interface BlockedKeyword {
  word: string
  duration: 'Forever' | 'For 24 hours' | '7 days' | '30 days'
}

definePageMeta({
  layout: 'settings'
})

const { client } = useAxiosClient()

const blockingDurations = [
  'Forever',
  'For 24 hours',
  '7 days',
  '30 days'
]
const showBlockedItems = ref(false)
const showCreateList = ref(false)
const showBlockLists = ref(false)
const excludeFollowedAccounts = ref(false)
const blockedChannels = ref<BlockedChannel[]>([])
const blockedKeyword = ref<BlockedKeyword>({
  word: '',
  duration: 'Forever'
})
const blockedKeywords = ref<BlockedKeyword[]>([])
const { history, undo, redo } = useRefHistory(blockedKeywords)

/**
 * 
 */
async function requestBlockedChannels () {
  try {
    const response = await client.get<BlockedChannel[]>('/user-channels/blocked')
    blockedChannels.value = response.data
  } catch {
    // Handle error
  }
}

/**
 * 
 */
async function handleAddBlockedKeyWord () {
  blockedKeywords.value.push(blockedKeyword.value)
  blockedKeyword.value = { word: '', duration: 'Forever' }
}

/**
 * 
 */
async function handleRemoveBlockedKeyword (index: number) {
  blockedKeywords.value.splice(index, 1)
}

onBeforeMount(async () => {
  await requestBlockedChannels()
})
</script>>
