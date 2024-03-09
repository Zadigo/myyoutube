<template>
  Great
</template>

<script>
import { useFeed } from '../store/feed'
import { storeToRefs } from 'pinia'

export default {
  name: 'FeedPage',
  setup () {
    const store = useFeed()
    const { videos } = storeToRefs(store)

    return {
      store,
      videos
    }
  },
  methods: {
    something () {
    }
  }
}
</script>
