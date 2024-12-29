<template>
  <div v-if="isSaved" class="source card-body">
    <div class="d-flex justify-content-between align-items-center">
      <p class="m-0">
        Source
      </p>

      <v-btn variant="text" color="dark" @click="isSaved=false">
        <font-awesome-icon icon="pen" />
      </v-btn>
    </div>
  </div>

  <div v-else class="source card-body">
    <div class="d-flex justify-content-between gap-2">
      <v-text-field v-model="sourceDetails.start_time" type="text" placeholder="Start time" variant="solo-filled" flat />
      <v-text-field v-model="sourceDetails.end_time" type="text" placeholder="End time" variant="solo-filled" flat />
    </div>

    <v-textarea v-model="sourceDetails.explanation" variant="solo-filled" flat no-resize />

    <div class="mt-3">
      <v-btn variant="tonal" color="dark" @click="handleAddSource">
        Add source
      </v-btn>
      <v-text-field v-for="(articleSource, i) in sourceDetails.article_sources" :key="i" type="url" placeholder="Source" variant="solo-filled" class="mt-1" flat />
    </div>

    <v-divider />

    <div class="d-flex justify-content-end">
      <v-btn variant="tonal" color="secondary" rounded @click="handleSave">
        <font-awesome-icon icon="save" class="me-2" />
        Save source
      </v-btn>
    </div>
  </div>
</template>

<script lang="ts">
import { SourceDetails } from '@/types/fact_checker';
import { defineComponent, PropType, ref } from 'vue';

export default defineComponent({
  name: 'SourceBlock',
  props: {
    index: {
      type: Number,
      required: true
    },
    block: {
      type: Object as PropType<SourceDetails>,
      required: true
    }
  },
  emits: {
    'update:blocks' (_block: SourceDetails) {
      return true
    }
  },
  setup(props) {
    const isSaved = ref(false)
    const sourceDetails = ref(props.block)
    return {
      sourceDetails,
      isSaved
    }
  },
  methods: {
    handleAddSource () {
      this.sourceDetails.article_sources.push('')
    },
    handleSave () {
      this.isSaved = !this.isSaved
      this.sourceDetails.id = this.index
      this.$emit('update:blocks', this.sourceDetails)
    }
  }
})
</script>
