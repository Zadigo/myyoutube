<template>
  <div :class="[isSwitch ? 'form-switch' : null, inline ? 'form-check-inline' : null]" class="form-check">
    <input :id="id" v-model="value" :class="[darkMode ? 'dark' : null]" :checked="value" :type="checkboxType" :role="[ isSwitch ? 'switch' : null]" :name="name" class="form-check-input">
    <label :for="id" class="form-check-label">{{ label }}</label>
  </div>
</template>

<script>
import { inject } from 'vue'

export default {
  name: 'BaseCheckbox',
  props: {
    id: {
      type: String,
      required: true
    },
    inline: {
      type: Boolean
    },
    label: {
      type: String,
      required: true
    },
    name: {
      type: String
    },
    isSwitch: {
      type: Boolean,
      default: false
    },
    isRadio: {
      type: Boolean,
      default: false
    },
    initial: {
      type: Boolean,
      default: false
    }
  },
  emits: {
    'update:initial' () {
      return true
    }
  },
  setup () {
    const darkMode = inject('darkMode', () => false)
    return {
      darkMode
    }
  },
  computed: {
    value: {
      get () {
        return this.initial
      },
      set (value) {
        this.$emit('update:initial', value)
      }
    },
    checkboxType () {
      if (this.isSwitch && this.isRadio) {
        return 'checkbox'
      } else if (this.isSwitch) {
        return 'checkbox'
      } else if (this.isRadio) {
        return 'radio'
      } else {
        return 'checkbox'
      }
    }
  },
  mounted () {
    if (this.initial) {
      this.value = true
    }
  }
}
</script>
