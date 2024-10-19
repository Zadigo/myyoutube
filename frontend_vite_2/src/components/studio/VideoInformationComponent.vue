<template>
  <div class="card-body">
    <div class="row">
      <div class="col-7">
        <v-text-field v-model="returnData.title" type=" text" placeholder="Title" variant="solo-filled" flat @keypress="handleChange" />

        <div class="alert alert-info fw-light">
          In order for you video to rank correctly, you should describe as much as possible and
          precisely what your video is about then select a category/sub-category that matches
          exactly the subject of the video you are uploading. Users may consider you video to
          be unfit if the category/sub-category don't match what they were expecting.
        </div>

        <v-textarea v-model="returnData.description" cols="30" rows="7" class="my-1" placeholder="Description" variant="solo-filled" flat @keypress="handleChange" />

        <v-autocomplete v-model="returnData.category" :items="categories" item-title="title" item-value="title" variant="solo-filled" placeholder="Select a category" flat auto-select-first>
          <v-text-field />
        </v-autocomplete>

        <v-autocomplete v-model="returnData.subcategory" :items="subCategories" item-title="title" item-value="title" variant="solo-filled" placeholder="Select a sub-category" flat auto-select-first>
          <v-text-field />
        </v-autocomplete>
      </div>

      <div class="col-5">
        <base-video-player :video-source="store.previewUrl" :revoke-url="true" @loaded-meta-data="handleFrameInformation" />

        <div class="mt-3">
          <h5>Thumbnail</h5>
          <p class="text-muted">
            Select or upload a picture that shows what's in your video.
            A good thumbnail stands out and draws viewers'
            attention. Learn more
          </p>
          
          <div class="row">
            <div v-for="(frame, i) in frames" :key="i" class="col-3">
              <img :src="frame[1]" class="img-fluid" alt="">
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      Something
    </div>
  </div>
</template>

<script lang="ts">
import { client } from '@/plugins/axios';
import { whenever } from '@vueuse/core';
import { computed, defineComponent, ref } from 'vue';

import BaseVideoPlayer from 'src/components/BaseVideoPlayer.vue';

export default defineComponent({
  name:'VideoInformationComponent',
  components: {
    BaseVideoPlayer
  },
  emits: {
    'update:data' () {
      return true
    }
  },
  setup () {
    const store = {}
    const frames = ref(null)

    const returnData = ref({
      title: null,
      description: null,
      category: null,
      subcategory: null
    })

    const categories = ref([])
    const subCategories = ref([])

    const hasCategory = computed(() => {
      return returnData.value.category !== null
    })

    async function getSubcategories () {
      try {
        const response = await client.get(`/videos/categories/${returnData.value.category}/sub-categories`)
        subCategories.value = response.data
      } catch (e) {
        console.error('getSubcategories', e)
      }
    }
    whenever(hasCategory, () => {
      getSubcategories()
    })

    return {
    hasCategory,
      categories,
      subCategories,
      store,
      returnData,
      frames
    }
  },
  beforeMount () {
    this.requestCategories()
  },
  methods: {
    async requestCategories () {
      try {
        const response = await this.$client.get('/videos/categories')
        this.categories = response.data
      } catch (e) {
        console.error('requestCategories', e)
      }
    },
    handleFrameInformation () {
      
    },
    handleChange () {
      this.$emit('update:data', this.returnData)
    }
  }
})
</script>
