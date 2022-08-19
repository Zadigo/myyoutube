<template>
  <transition-group id="recommendations" name="opacity" tag="div" mode="out-in">
    <div v-for="recommendation in recommendations" :key="recommendation.id" class="card mb-2">
      <router-link :to="{ name: 'home_view', query: { video: recommendation.id } }">
        <div class="row g-0">
          <div class="col-md-4">
            <img src="http://via.placeholder.com/400x400" class="img-fluid rounded-start" alt="Image 7">
          </div>

          <div class="col-md-8">
            <div class="card-body p-2">
              <h5 class="card-title fs-6">Golden State warriors vs Celtics Game 6 on the way</h5>
              <p class="text-muted m-0 fs-7">Vikapower</p>
              <p class="text-muted m-0 fs-7">911K views - 15 hours ago</p>
            </div>
          </div>
        </div>
      </router-link>
    </div>
  </transition-group>
</template>

<script>
export default {
  name: 'ListRecommendations',
  props: {
    recommendations: {
      type: Array,
      required: true
    }
  }
}
</script>
