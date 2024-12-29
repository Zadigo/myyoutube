<template>
  <li class="nav-item">
    <router-link :to="to" class="nav-link">
      {{ linkName }}
    </router-link>
  </li>
</template>

<script>
export default {
  name: 'NavItem',
  props: {
    to: {
      type: Object,
      required: true
    },
    linkName: {
      type: String,
      required: true
    }
  }
}
</script>
