<template>
  <v-menu>
    <!-- v-slot:activator="{ props }" -->
    <template #activator="{ props }">
      <v-btn v-bind="props" color="secondary" size="small" rounded="xl" flat>
        <font-awesome-icon icon="fas fa-face-smile" />
      </v-btn>
    </template>

    <v-card width="300">
      <div class="container">
        <article v-for="category in categories" :key="category" class="mt-4" :aria-label="category">
          <h5 class="text-body-secondary fw-light">
            {{ category }}
          </h5>
          
          <v-btn v-for="(emoji, index) in emojis[category]" :key="`emoji_${index}`" variant="text" @click.prevent="handleEmojiClick(emoji)">
            {{ emoji }}
          </v-btn>
        </article>
      </div>
    </v-card>
  </v-menu>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import emojis from './emojis-data.json'

export default defineComponent({
  emits: {
    'emoji-click' (_emoji: string) {
      return true
    }
  },
  setup () {
    return {
      emojis
    }
  },
  computed: {
    categories () {
      return Object.keys(this.emojis)
    }
  },
  methods: {
    handleEmojiClick (emoji: string) {
      this.$emit('emoji-click', emoji)
    }
  }
})
</script>
