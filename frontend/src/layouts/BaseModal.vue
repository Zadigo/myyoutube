<template>
  <div :id="id" ref="link" :class="modalClasses" class="modal" role="dialog" tabindex="-1">
    <div :class="modalDialogClasses" class="modal-dialog">
      <div :class="modalContentClasses" class="modal-content">
        <div class="modal-header">
          <h5 v-if="title" class="modal-title">
            {{ title }}
          </h5>
          <button type="button" class="btn-close" aria-label="Close" @click="$emit('close')"></button>
        </div>

        <div class="modal-body">
          <slot></slot>
        </div>

        <slot name="footer"></slot>
        <!-- <div class="modal-footer">
          <button type="button" class="btn btn-secondary">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
/*
 * Base bootstrap modal
 * size: modal-sm, modal-lg, modal-xl, modal-fullscreen
 **/ 
import { inject } from 'vue'

export default {
  name: 'BaseModal',
  props: {
    id: {
      type: String,
      required: true
    },
    title: {
      type: String
    },
    centered: {
      type: Boolean
    },
    scrollable: {
      type: Boolean
    },
    show: {
      type: Boolean
    },
    size: {
      type: String,
      default: 'lg'
    },
    staticBackdrop: {
      type: Boolean
    },
    position: {
      type: String,
      default: null
    }
  },
  emits: ['close'],
  setup () {
    var darkMode = inject('darkMode')
    return {
      darkMode
    }
  },
  computed: {
    modalClasses () {
      let position = this.position
      
      if (position === 'top-left' || position === 'bottom-left') {
        position = 'left'
      } else if (position === 'top-right' || position === 'bottom-right') {
        position = 'right'
      }  

      return [
        this.show ? 'show' : null,
        position
      ]
    },
    modalDialogClasses () {
      if (this.hasPositionX) {
        return [
          {
            [`modal-side modal-${this.position}`]: true
          }
        ]
      }

      if (this.hasPositionY) {
        return [
          {
            [`modal-frame modal-${this.position}`]: true
          }
        ]
      }

      return [
        {
          [`modal-${this.size}`]: true
        },
        this.centered ? 'modal-dialog-centered' : null,
        this.scrollable ? 'modal-dialog-scrollable' : null
      ]
    },
    modalContentClasses () {
      return [
        this.hasPositionY ? 'rounded-0' : null,
        this.darkMode ? 'bg-dark text-light' : 'bg-white text-dark',
      ]
    },
    hasPositionX () {
      const positions = ['right', 'left', 'top-right', 'top-left', 'bottom-left', 'bottom-right']
      return this.position && positions.includes(this.position)
    },
    hasPositionY () {
      return this.position && this.position === 'top' || this.position === 'bottom'
    }
  },
  watch: {
    show (newValue) {
      if (newValue) {
        this.$refs.link.classList.add('show')
        this.$refs.link.style.display = 'block'
        this.$refs.link.ariaModal = true
      } else {
        this.$refs.link.classList.remove('show')
        this.$refs.link.style.display = 'none'
        this.$refs.link.ariaModal = null
        this.$refs.link.ariaHidden = true
      }
      this.toggleBody()
    }
  },
  // updated() {
  //   var body = document.querySelector('body')
  //   if (!this.show && body.classList.contains('modal-open')) {
  //     this.toggleBody()
  //   } else {
  //     this.$refs.link.style.display = 'block'
  //   }
  // },
  mounted () {
    // if (this.show) {
    //   this.toggleBody()
    // }
    var body = this.getBody()
    body.addEventListener('click', this.windowListener, { passive: true })
  },
  unmounted () {
    var body = this.getBody()
    body.removeEventListener('click', this.windowListener, { passive: true })
  },  
  methods: {
    windowListener (e) {
      if (e.target.classList.contains('modal')) {
        if (this.staticBackdrop) {
          this.$refs.link.classList.add('modal-static')
          setTimeout(() => {
            this.$refs.link.classList.remove('modal-static')
          }, 300);
        } else {
          this.$emit('close')
        }
      }
    },
    toggleBody () {
      var body = document.querySelector('body')

      if (body.classList.contains('modal-open')) {
        body.style = null
        body.classList.remove('modal-open')
        body.classList.add('modal-close')
        setTimeout(() => {
          body.classList.remove('modal-close')
        }, 500)
      } else {
        body.classList.add('modal-open')
        body.style.overflow = 'hidden'
        // body.style.paddingRight = '17px'
      }
    },
    getBody () {
      return document.querySelector('body')
    }
  }
}
</script>
