<template>
  <div class="dropdown">
    <button id="dropdownMenuButton1" :class="buttonClasses" :aria-expanded="show" class="btn btn-lg dropdown-toggle" type="button" @click="toggle">
      <span v-if="icon" :class="{ [`mdi-${icon}`]: true }" class="mdi me-2"></span>
      {{ buttonName }}
    </button>

    <ul ref="link" :class="{ show }" aria-labelledby="dropdownMenuButton1" class="dropdown-menu">
      <li v-for="(item, i) in items" :key="item.name">
        <a class="dropdown-item" href @click.prevent="show = !show, $emit('dropdown-click', [i, item])">
          <span v-if="item.icon" :class="{ [`mdi-${item.icon}`]: true }" class="mdi me-2"></span>
          {{ item.name }}
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import { onClickOutside } from '@vueuse/core'
import { ref } from 'vue'

export default {
  name: 'BaseDropdownButton',
  props: {
    // animation: {
    //   type: String,
    //   default: 'scale'
    // },
    buttonName: {
      type: String
    },
    color: {
      type: String,
      default: 'primary'
    },
    icon: {
      type: String
    },
    items: {
      type: Array,
      required: true
    }
  },
  emits: ['click', 'dropdown-click'],
  setup () {
    const target = ref(null)
    const show = ref(false)
    onClickOutside(target, () => {
      show.value = false
    })
    return {
      show,
      target
    }
  },
  computed: {
    buttonClasses () {
      return [
        this.show ? 'show' : null,
        {
          [`btn-${this.color}`]: true
        }
      ]
    }
  },
  watch: {
    show (current) {
      if (current) {
        this.$refs.link.style.position = 'absolute'
        // this.$refs.link.style.inset = 'auto auto 0px 0px'
        // this.$refs.link.style.margin = '0px'
        // this.$refs.link.style.transform = 'translate(0px, -40px)'
      } else {
        if (this.$refs.link.classList.contains('show')) {
          this.$refs.link.style.animation = 'scaleReverse .3s ease-out'
          this.$refs.link.style = null
        }
      }
      this.show = current
    }
  },
  mounted () {
    this.target = this.$refs.link
    //   this.$refs.link.style.animation = `${this.animation} .3s ease`
    //   var body = document.querySelector('body')
    //   body.addEventListener('click', (e) => {
    //       // console.log(e)
    //       if (!e.target.classList.contains('dropdown')) {
    //           this.show = !this.show
    //       }
    //   })
  },
  methods: {
    toggle () {
      this.show = !this.show
      this.$emit('click')
    }
  } 
}  
</script>

<style scoped>
.dropdown-menu {
  animation: scale .3s ease;
}

@keyframes scale {
  0% {
    opacity: 0;
    transform: scale(0.9, 0.9);
  }

  99% {
    opacity: 1;
    transform: scale(1, 1);
  }
}

@keyframes scaleReverse {
  0% {
    opacity: 1;
    transform: scale(1, 1);
  }

  99% {
    opacity: 0;
    transform: scale(.9, .9);
  }
}
</style>
