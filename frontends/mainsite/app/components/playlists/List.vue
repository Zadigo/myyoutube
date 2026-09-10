<template>
  <u-card>
    <u-button class="me-2" size="sm" @click="emit('playlist:create', false)">
      <icon name="lucide:plus" class="me-2" />
      Playlist
    </u-button>

    <u-button size="sm" @click="emit('playlist:create', true)">
      <icon name="lucide:star" class="me-2" />
      Intelligent playlist
    </u-button>

    <u-separator class="my-3" />

    <div class="space-y-2">
      <a v-for="playlist in playlists" :key="playlist.node.id" href="#" class="bg-primary-50 hover:bg-primary-100 dark:bg-primary-900 dark:hover:bg-primary-800 block rounded-lg p-3" @click.prevent="emit('playlist:details', playlist)">
        <article :data-id="playlist.node.id">
          <p class="font-bold">{{ playlist.node.name }}</p>
          <p v-if="playlist.node.description" class="font-light m-0">
            {{ playlist.node.description }}
          </p>
        </article>
      </a>
    </div>
  </u-card>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'playlist:create': [intelligent: boolean], 'playlist:details': [playlist: RelayNode<SinglePlaylist>] }>()

const { playlists } = usePlaylistsComposable() 
</script>
