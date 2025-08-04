<template>
  <v-menu>
    <!-- v-slot:activator="{ props }" -->
    <template #activator="{ props }">
      <VoltButton v-bind="props" color="secondary" size="small" rounded="xl" flat>
        <font-awesome icon="face-smile" />
      </VoltButton>
    </template>

    <v-card width="300">
      <div class="container">
        <article v-for="category in categories" :key="category" class="mt-4" :aria-label="category">
          <h5 class="text-body-secondary fw-light">
            {{ category }}
          </h5>
          
          <VoltButton v-for="(emoji, index) in emojis[category]" :key="`emoji_${index}`" variant="text" @click.prevent="handleEmojiClick(emoji)">
            {{ emoji }}
          </VoltButton>
        </article>
      </div>
    </v-card>
  </v-menu>
</template>

<script lang="ts" setup>
import emojis from './emojis-data.json'

const emit = defineEmits({
  'emoji-click' (_emoji: string) {
    return true
  }
})

const categories = computed(() => {
  return Object.keys(emojis)
})

function handleEmojiClick (emoji: string) {
  emit('emoji-click', emoji)
}
</script>
