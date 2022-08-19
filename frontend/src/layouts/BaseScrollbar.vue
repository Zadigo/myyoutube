<template>
  <div ref="link" class="scrollbar">
    <router-link v-for="(item, i) in items" :key="i" :to="{ name: 'home_view', query: { s: item } }" :class="badgeSize" class="mx-1">
      <span :class="badgeClasses" class="badge fw-normal rounded-pill">
        {{ item }}
      </span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'BaseScrollbar',
  props: {
    items: {
      type: Array,
      required: true
    },
    color: {
      type: String,
      default: 'primary'
    },
    badges: {
      type: String,
      default: 'p-2'
    },
    badgeSize: {
      type: String,
      default: 'h5'
    }
  },
  computed: {
    badgeClasses () {
      return [
        this.badges,
        {
          [`badge-${this.color}`]: true
        }
      ]
    }
  }
}
</script>

<style scoped>
.scrollbar {
  /* transition: all .3s ease; */
  overflow: auto;
  white-space: nowrap;
  scroll-behavior: smooth;
  padding: .5rem;
  margin-top: .25rem;
  margin-bottom: .25rem;
}

.scrollbar h5 {
  display: inline-block;
}

.scrollbar::-webkit-scrollbar {
  display: none;
}
</style>
