<template>
  <div :id="id" ref="link" :class="offcanvasClasses" class="offcanvas" tabindex="-1" aria-labelledby="offcanvasLabel">
    <div class="offcanvas-header">
      <h5 v-if="title" id="offcanvasLabel" class="offcanvas-title">
        {{ title }}
      </h5>
      <button type="button" class="btn-close text-reset" aria-label="Close" @click="$emit('close')"></button>
    </div>

    <div class="offcanvas-body">
      <slot></slot>
    </div>

    <slot name="footer"></slot>
  </div>
</template>

<script>
import { inject } from 'vue'

export default {
  name: 'BaseOffcanvas',
  props: {
    id: {
      type: String
    },
    position: {
      type: String,
      default: 'start'
    },
    show: {
      type: Boolean
    },
    title: {
      type: String
    }
  },
  emits: {
    close: () => true
  },
  setup () {
    var darkMode = inject('darkMode')
    return {
      darkMode
    }
  },
  computed: {
    offcanvasClasses () {
      return [
        this.show ? 'show' : null,
        this.darkMode ? 'bg-dark text-light' : 'bg-white text-dark',
        {
          [`offcanvas-${this.position}`]: true
        }
      ]
    }
  },
  watch: {
    show (newValue) {
      var body = document.querySelector('body')
      if (newValue) {
        body.style.overflow = 'hidden'
        body.style.paddingRight = '17px'
        body.classList.add('modal-open')

        this.$refs.link.style.visibility = 'visible'
      } else {
        body.style = null
        body.classList.remove('modal-open')
        
        this.$refs.link.style.visibility = 'none'
      }
    }
  },
  mounted () {
    var body = this.getBody()
    body.addEventListener('click', this.windowListener, { passive: true })
  },
  unmounted () {
    var body = this.getBody()
    body.removeEventListener('click', this.windowListener, { passive: true })
  },
  methods: {
    getBody () {
      return document.querySelector('body')
    },
    windowListener (e) {
      // console.log(e.target)
      if (e.target.classList.contains('modal-open')) {
        this.$emit('close')
      }
    }
  }
}
</script>
