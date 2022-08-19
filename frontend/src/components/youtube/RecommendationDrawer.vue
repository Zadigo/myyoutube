<template>
  <section v-if="show" class="recommendations">
    <div class="conatainer-fluid">
      <div class="row">
        <!-- Filters -->

        <!-- Videos -->
        <div class="col-12">
          <list-recommendations-vue :recommendations="recommendations" />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import ListRecommendationsVue from './ListRecommendations.vue'

export default {
  name: 'ListRecommendations',
  components: {
    ListRecommendationsVue
  },
  props: {
    show: {
      type: Boolean
    },
    recommendations: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.recommendations {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: white;
  padding: 1rem;
}
</style>
