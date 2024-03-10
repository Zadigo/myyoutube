<template>
  <aside class="mt-3">
    <router-link :to="{ name: 'video_details', params: { id: 'vd_eneoifz' } }">
      <div v-for="i in 10" :key="i" class="card mt-1">
        <div class="card-body">
          Something
        </div>
      </div>
    </router-link>
  </aside>
</template>

<script>
export default {
  setup () {
    return {
      
    }
  }
}
</script>
