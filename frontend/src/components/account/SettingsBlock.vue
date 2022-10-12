<template>
  <div class="list-group">
    <div v-for="(item, i) in items" :key="i" class="list-group-item list-group-item-action p-3">
      <div class="form-check form-switch">
        <input :id="item.name" class="form-check-input" type="checkbox" role="switch" @click="selection(item)">
        <label :for="item.name" class="form-check-label">
          {{ item.text }}
        </label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SettingsBlock',
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  emits: {
    'setting-selection': () => true
  },
  data () {
    return {
      selections: {}
    }
  },
  created () {
    this.items.forEach((item) => {
      this.selections[item.name.toLowerCase()] = false
    })
  },
  methods: {
    selection (item) {
      this.selections[item.name.toLowerCase()] = !this.selections[item.name.toLowerCase()]
      this.$emit('setting-selection', this.selections)
    }
  }
}
</script>
