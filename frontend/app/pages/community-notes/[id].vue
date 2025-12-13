<template>
  <section id="community-note">
    <div v-if="communityNote" class="grid grid-cols-2 gap-2">
      <div class="col-span-2 mb-5">
        <nuxt-card>
          <template #content>
            <volt-button to="/community-notes">
              <icon name="i-lucide-arrow-left" />
              Back
            </volt-button>
          </template>
        </nuxt-card>
      </div>

      <!-- User Information -->
      <aside>
        <volt-card>
          <template #content>
            <h1 class="text-2xl font-bold mb-3">{{ communityNote.node.author.username }}</h1>
            <img src="/avatars/avatar1.png" :alt="communityNote.node.author.username" class="rounded-lg">
          </template>
        </volt-card>
      </aside>

      <!-- Note Details -->
      <div class="space-y-2">
        <volt-card>
          <template #content>
            <div class="flex items-center justify-start gap-2">
              <h2 class="font-bold text-xl">{{ communityNote.node.title }}</h2>
              <volt-tag>{{ communityNote.node.status }}</volt-tag>
            </div>

            <p class="text-sm text-gray-600">{{ communityNote.node.description }}</p>

            <div class="mt-4 space-x-2">
              <volt-button @click="() => { createVote('upvote') }">
                <icon name="lucide:thumbs-up" />
              </volt-button>

              <volt-button @click="() => { toggleShouldDemandReason() }">
                <icon name="lucide:thumbs-down" />
              </volt-button>

              <div v-if="shouldDemandReason" id="readon">
                <volt-fluid>
                  <volt-textarea v-model="reason" class="mt-2" :style="{ resize: 'none' }" />
                </volt-fluid>

                <volt-button class="mt-2" @click="() => { createVote('downvote') }">
                  Submit Reason
                </volt-button>
              </div>
            </div>
          </template> 
        </volt-card>

        <!-- Other Notes -->
        <volt-card>
          <template #content>
            <h2 class="font-bold text-xl mb-4">
              Other Notes on {{ communityNote.node.subjectCreatorId }} (36)
            </h2>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              <community-card v-if="communityNote" :note="communityNote" />
              <div v-else>Community note not found.</div>
            </div>
          </template>
        </volt-card>

        <!-- Note Sources -->
        <volt-card>
          <template #content>
            <h2 class="font-bold text-xl mb-4">Sources</h2>
            <ul>
              <li v-for="(source, index) in communityNote.node.noteSources" :key="index" class="rounded-lg bg-primary-50 p-5 flex items-center gap-2">
                <icon name="lucide:link" />
                <a :href="source.url" class="text-blue-500 hover:underline" target="_blank">
                  {{ source.url }}
                </a>
              </li>
            </ul>
          </template>
        </volt-card>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const { communityNotes } = await useCommunityNotesComposable()

const { id } = useRoute().params
const getCommunityNote = reactify(() => communityNotes.value.data.allnotes.edges.find(note => note.node.reference === id))
const communityNote = getCommunityNote()

/**
 * Voting
 */

const { createVote, shouldDemandReason, toggleShouldDemandReason, reason } = useCommunityNoteById(communityNote)
</script>
