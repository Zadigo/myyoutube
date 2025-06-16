<template>
  <div class="card-body">
    <div class="row">
      <div class="col-md-8">
        <p class="fw-bold">
          Tag users
        </p>

        <p class="fw-light">
          If your video contains users that need to be tagged,
          you can do so by indicating either their socials or
          their YouTube handle
        </p>

        <div v-for="(participant, i) in participants" :key="i" class="d-flex justify-content-between gap-1">
          <VoltInputText v-model="participant.url" type="url" placeholder="Social url"  flat />
          <v-select v-model="participant.handle" :items="socials" placeholder="User handle"  flat />
          <v-btn variant="text" color="danger" @click="handleRemoveParticipant(i)">
            <font-awesome icon="trash" />
          </v-btn>
        </div>

        <v-btn variant="tonal" color="secondary" rounded @click="handleAddParticipant">
          <font-awesome icon="plus" class="me-2" />
          Add participant
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

interface Participant {
  url: string | null
  handle: 'Facebook' | 'X' | 'Instagram' | 'YouTube'
}

const socials = [
  'Facebook',
  'X',
  'Instagram',
  'YouTube'
]

const participants = ref<Participant[]>([
  {
    url: null,
    handle: 'Instagram'
  }
])

function handleAddParticipant () {
  participants.value.push({
    url: null,
    handle: 'Instagram'
  })
}

function handleRemoveParticipant(index: number) {
  participants.value.splice(index, 1)
}
</script>
