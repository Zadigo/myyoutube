<template>
  <div v-if="isSaved" class="source p-5 rounded-lg bg-slate-50">
    <div class="flex-col">
      <div class="font-bold flex gap-2">
        <VoltBadge><time>{{ block.start_time }}</time></VoltBadge>
        <VoltBadge><time>{{ block.end_time }}</time></VoltBadge>
        <VoltBadge>4 sources</VoltBadge>
      </div>

      <p class="font-light my-2 p-2 rounded-lg">
        {{ block.explanation }}
      </p>

      <VoltButton @click="handleEdit">
        <Icon name="i-fa7-solid:pen" />
      </VoltButton>
    </div>
  </div>

  <div v-else class="space-y-3 p-5">
    <div class="flex justify-start gap-2">
      <VoltInputText v-model="sourceDetails.start_time" type="time" class="w-full" placeholder="Start time" />
      <VoltInputText v-model="sourceDetails.end_time" type="time" class="w-full" placeholder="End time" />
    </div>

    <VoltTextarea v-model="sourceDetails.explanation" class="w-full resize-none" placeholder="Explanation" rows="4" />

    <div class="mt-3">
      <VoltButton class="mb-2" variant="outlined" @click="handleAddSource">
        <Icon name="i-fa7-solid:book" />
        Add source
      </VoltButton>

      <div v-for="(articleSource, idx) in sourceDetails.article_sources" :key="idx" class="flex justify-between items-center gap-3">
        <VoltInputText v-model="sourceDetails.article_sources[idx]" type="url" placeholder="Source" class="w-full" />
        <VoltButton variant="outlined" @click="() => handleRemoveSource(idx)">
          <Icon name="i-fa7-solid:trash" />
        </VoltButton>
      </div>
    </div>

    <VoltDivider />

    <div class="flex justify-end">
      <VoltButton variant="outlined" @click="handleSave">
        <Icon name="i-fa7-solid:save" class="me-2" />
        Save source
      </VoltButton>
    </div>
  </div>
</template>

<script lang="ts" setup>
import type { SourceDetails } from '~/types'

const emit = defineEmits<{ 'update:blocks': [block: SourceDetails] }>()
const props = defineProps<{
  index: number;
  block: SourceDetails;
}>()

const sourceDetails = ref<SourceDetails>(props.block)

/**
 * Handles the addition of a new source
 */
function handleAddSource () {
  sourceDetails.value.article_sources.push('')
}

 const isSaved = ref<boolean>(false)

/**
 * Handles the edit action for a block
 */
function handleEdit () {
  isSaved.value = false
}

 /**
 * Handles the save action for a block
 */
function handleSave () {
  isSaved.value = !isSaved.value
  sourceDetails.value.id = props.index
  emit('update:blocks', sourceDetails.value)
}

/**
 * Handles the removal of a source from the list
 * @param index - The index of the source to remove
 */
function handleRemoveSource (index: number) {
  sourceDetails.value.article_sources.splice(index, 1)
}
</script>
