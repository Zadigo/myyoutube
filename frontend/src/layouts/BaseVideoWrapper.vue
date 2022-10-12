<template>
  <div class="video-wrapper">
    <slot></slot>

    <div v-if="showMoreVideos" class="more-videos">
      <div v-for="i in 6" :key="i" class="recommendation">
        {{ i }}
      </div>
    </div>

    <div v-if="showReference" class="reference">
      <router-link :to="{ name: 'home_view' }" type="button" class="btn btn-primary">
        Preclass
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseVideoWrapper',
  props: {
    showMoreVideos: {
      type: Boolean
    },
    showReference: {
      type: Boolean
    }
  },
  data () {
    return {
    }
  }
}
</script>

<style>
.video-wrapper {
  position: relative;
}

.more-videos {
  position: absolute;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, 1fr);
  grid-gap: 10px;
  top: 0;
  left: 10%;
  height: 80%;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  border-radius: .45em;
  padding: 1rem;
}

/* .c::before {
  content: "";
  position: absolute;
  height: 400px;
  width: 400px;
  top: 0;
  left: 0;
  filter: blur(1px);
  background: red;
  z-index: 1000;
} */

.more-videos .recommendation {
  height: auto;
  width: 100%;
  background-color: blue;
  border-radius: .45em;
  /* box-shadow: 0 .125rem .25rem rgba(0, 0, 0, .075) !important; */
  box-shadow: 0 .5rem 1rem rgba(0, 0, 0, .15) !important;
  cursor: pointer;
  transition: all .5s ease;
}

.more-videos .recommendation:hover {
  transform: scale(1.05);
}

.video-wrapper .reference {
  position: absolute;
  top: 0;
  right: 0;
  margin: .5rem;
  z-index: 1000;
}
</style>
