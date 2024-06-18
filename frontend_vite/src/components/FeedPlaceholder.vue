<template>
  <div class="row">
    <div v-for="video in 30" :key="video" class="col-3 my-1">
      <article class="card shadow-sm">
        <div class="card-body">
          <v-skeleton-loader type="card-avatar"></v-skeleton-loader>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeedPlaceholder'
}
</script>
