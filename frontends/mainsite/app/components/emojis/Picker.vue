<template>
  <v-menu>
    <!-- v-slot:activator="{ props }" -->
    <template #activator="{ props }">
      <u-button v-bind="props" rounded="xl" icon="i-fa7-solid:face-smile" />
    </template>

    <v-card width="300">
      <div class="container">
        <article v-for="category in categories" :key="category" class="mt-4" :aria-label="category">
          <h5 class="text-body-secondary fw-light">
            {{ category }}
          </h5>
          
          <u-button v-for="(emoji, index) in emojis[category]" :key="`emoji_${index}`" variant="text" @click.prevent="handleEmojiClick(emoji)">
            {{ emoji }}
          </u-button>
        </article>
      </div>
    </v-card>
  </v-menu>
</template>

<script lang="ts" setup>
import emojis from './emojis-data.json'

const emit = defineEmits<{ 'emoji-click': [emoji: string] }>()

const categories = computed(() => Object.keys(emojis))

function handleEmojiClick (emoji: string) {
  emit('emoji-click', emoji)
}
</script>
