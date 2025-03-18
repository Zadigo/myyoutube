<template>
  <div v-if="isSaved" class="source card-body">
    <div class="d-flex justify-content-between align-items-center">
      <p class="fw-bold d-flex gap-3">
        <time>{{ block.start_time }}</time>
        <time>{{ block.end_time }}</time>
      </p>

      <p class="fw-light">
        {{ block.explanation }}
      </p>

      <v-btn variant="text" color="dark" @click="isSaved=false">
        <font-awesome icon="pen" />
      </v-btn>
    </div>
  </div>

  <div v-else class="source card-body">
    <div class="d-flex justify-content-between gap-2">
      <v-text-field v-model="sourceDetails.start_time" type="text" placeholder="Start time" variant="solo-filled" flat />
      <v-text-field v-model="sourceDetails.end_time" type="text" placeholder="End time" variant="solo-filled" flat />
    </div>

    <v-textarea v-model="sourceDetails.explanation" placeholder="Explanation" variant="solo-filled" flat no-resize />

    <div class="mt-3">
      <v-btn variant="tonal" color="dark" @click="handleAddSource">
        Add source
      </v-btn>

      <div class="d-flex justify-content-between align-items-center gap-3">
        <v-text-field v-for="(articleSource, i) in sourceDetails.article_sources" :key="i" v-model="sourceDetails.article_sources[i]" :rules="[rules.validateUrl]" type="url" placeholder="Source" variant="solo-filled" class="mt-1" flat />
        <v-btn variant="tonal" color="danger" rounded>
          <font-awesome icon="trash" />
        </v-btn>
      </div>
    </div>

    <v-divider />

    <div class="d-flex justify-content-end">
      <v-btn variant="tonal" color="secondary" rounded @click="handleSave">
        <font-awesome icon="save" class="me-2" />
        Save source
      </v-btn>
    </div>
  </div>
</template>

<script lang="ts" setup>
import type { SourceDetails } from '~/types';
import type { PropType } from 'vue';
import { ref } from 'vue';

const props = defineProps({
  index: {
    type: Number,
    required: true
  },
  block: {
    type: Object as PropType<SourceDetails>,
    required: true
  }
})

const rules = {
  validateUrl: (url: string) => !!url || !!url.startsWith('http://') || 'Url is not valid'
}

const emit = defineEmits({
  'update:blocks' (_block: SourceDetails) {
    return true
  }
})

const isSaved = ref(false)
const sourceDetails = ref(props.block)

function handleAddSource () {
  sourceDetails.value.article_sources.push('')
}

function handleSave () {
  isSaved.value = !isSaved.value
  sourceDetails.value.id = props.index
  emit('update:blocks', sourceDetails.value)
}
</script>
