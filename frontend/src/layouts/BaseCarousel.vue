<template>
  <div id="carouselBasicExample" class="carousel slide carousel-fade">
    <ol class="carousel-indicators">
      <li v-for="(image, i) in images" :key="image.id" :class="{ active: image.id === currentSlide.id }" :aria-current="[image.id === currentSlide.id ? 'true' : null]" :aria-label="`Slide ${i}`" @click="selectImage(image)"></li>
    </ol>

    <div class="carousel-inner">
      <div class="view">
        <div v-for="image in images" :key="image.id" :class="{ active: image.id === currentSlide.id }" class="carousel-item">
          <img :src="image.url" class="d-block w-100" alt="Sunset Over the City" />
          <div class="carousel-caption d-none d-md-block">
            <h5>{{ image.label }}</h5>
            <p>{{ image.description }}</p>
          </div>
        </div>
        <div class="mask rgba-black-strong"></div>
      </div>
    </div>

    <button class="carousel-control-prev" type="button" @click="previousImage">
      <span class="mdi mdi-arrow-left" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>

    <button class="carousel-control-next" type="button" @click="nextImage">
      <span class="mdi mdi-arrow-right" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script>
export default {
  name: 'BaseCarousel',
  props: {
    images: {
      type: Array,
      default: () => [
        {
          id: 2,
          url: 'https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(22).webp',
          label: 'Second slide label',
          description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        },
        {
          id: 1,
          url: 'https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(15).webp',
          label: 'First slide label',
          description: 'Nulla vitae elit libero, a pharetra augue mollis interdum.'
        },
        {
          id: 3,
          url: 'https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(23).webp',
          label: 'Third slide label',
          description: 'Praesent commodo cursus magna, vel scelerisque nisl consectetur.'
        }
      ]
    }
  },
  data () {
    return {
      currentId: 0,
      index: 0
    }
  },
  computed: {
    currentSlide () {
      const items = this.images.filter((image) => {
        return image.id === this.currentId
      })
      return items[0]
    }
  },
  created () {
    this.currentId = this.images[0].id
  },
  methods: {
    selectImage (image) {
      this.index = image.id
    },
    previousImage () {
      let index = this.index - 1
      if (index <= 0) {
        index = this.images.length - 1
      }
      this.index = index
      this.currentId = this.images[index].id
    },
    nextImage () {
      let index = this.index + 1
      if (index >= this.images.length) {
        index = 0
      }
      this.index = index
      this.currentId = this.images[index].id
    }
  }
}
</script>
