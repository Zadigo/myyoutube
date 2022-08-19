<template>
  <div class="col-3">
    <transition name="explode" mode="out-in">
      <div v-if="expandCard" :class="[{ show: expandCard }]" class="card shadow bg-dark text-light border border-primary" @mouseleave="expandCard = false">
        <div class="indicator">prime</div>
        <a href>
          <img src="https://via.placeholder.com/800x800" class="card-img-top">
        </a>
        
        <div class="gradient"></div>
        <div class="card-body">
          <div class="d-flex justify-content-between mt-3">
            <a href class="btn btn-sm btn-primary btn-floating">
              <span class="mdi mdi-play"></span>
            </a>

            <div class="btn-group">
              <button type="button" class="btn btn-sm btn-primary">
                <span class="mdi mdi-play"></span>
              </button>
              <button type="button" class="btn btn-sm btn-primary">
                <span class="mdi mdi-play"></span>
              </button>
              <button type="button" class="btn btn-sm btn-primary">
                <span class="mdi mdi-play"></span>
              </button>
            </div>
          </div>

          <p class="fw-bold m-0 mt-4">What does fashion mean</p>
          <p class="fw-light">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit...
          </p>
        </div>
      </div>

      <div v-else class="card" @mouseenter="expandCard = true">
        <img src="https://via.placeholder.com/800x800" class="card-img">
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'VideoCard',
  data () {
    return {
      expandCard: false
    }
  }
}
</script>

<style scoped>
.col-3 {
  position: relative;
}
.gradient::after {
  content: "";
  position: absolute;
  display: block;
  left: 0;
  right: 0;
  top: 53%;
  height: 10%;
  width: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(38, 38, 38, 1));
}

.indicator {
  position: absolute;
  padding: .3rem;
  top: 0;
  left: 40%;
  background-color: #0d6efd;
  color: rgba(38, 38, 38, 1);
  border-bottom: 2px solid rgba(38, 38, 38, 1);
  border-left: 2px solid rgba(38, 38, 38, 1);
  border-right: 2px solid rgba(38, 38, 38, 1);
  border-bottom-left-radius: .5rem;
  border-bottom-right-radius: .5rem;
  font-weight: bold;
  font-size: .8rem;
}

.card.border {
  border: 2px solid #0d6efd !important;
}

.explode-enter-active,
.explode-leave-active {
  transition: all .1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.explode-enter-from,
.explode-leave-to {
  opacity: 0;
  transform: scale(1, 1);
}

.explode-enter-to,
.explode-leave-from {
  opacity: 1;
}

.card.show {
  position: absolute;
  display: block;
  left: 0;
  z-index: 999;
  transform: scale(1.1, 1.1);
}
</style>
