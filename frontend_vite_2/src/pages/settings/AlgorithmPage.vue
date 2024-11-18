<template>
  <section id="algorithm">
    <div class="row">
      <div class="col-8 offset-md-2">
        <div class="card mb-2">
          <div class="card-body">
            <h2>
              Customize your viewing experience
            </h2>
          </div>
        </div>

        <div class="row">
          <div class="col-8">
            <div class="card">
              <div class="card-body">
                <div class="alert alert-info">
                  If no options are selected, YouTube will use 
                  your viewing history to recommend the most 
                  relevant videos
                </div>

                <v-checkbox label="Let YouTube decide which are the most relevant videos for me" />

                <p>Select your preferred categories</p>
                <div class="actions">
                  <v-select v-model="selectedCategory" :items="categories" placeholder="Select the main category" variant="outlined" />
                  <v-select v-model="selectedSubcategory" :items="subCategories" placeholder="Select the sub category" variant="outlined" />
                  <v-btn color="primary" rounded="xl" flat @click="handleAddCategory">
                    <v-icon icon="mdi-plus" />
                    Add
                  </v-btn>
                </div>

                <div class="mt-5">
                  <v-switch label="Let YouTube recommend the most popular videos from what users have also watched based on the video that you are currently viewing" inset />
                </div>
              </div>
            </div>
          </div>
    
          <aside class="col-4">
            <div class="card">
              <div class="card-body">
                <div v-for="category in requestData.preferred_categories" :key="category.title" class="category mt-3">
                  <h2 class="h5">
                    {{ category.title }}
                  </h2>

                  <div class="list-group">
                    <div v-for="subcategory in category.subcategories" :key="subcategory" class="list-group-item d-flex justify-content-between align-items-center">
                      <span>{{ subcategory }}</span>
                      <v-btn color="danger" variant="text">
                        <font-awesome-icon :icon="['fas', 'fa-trash']" />
                      </v-btn>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </aside>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import _ from 'lodash'
import { computed, defineComponent, ref } from 'vue'
import { whenever } from '@vueuse/core'
import { useVueSession } from '@/plugins/vue-storages'
import { client } from '@/plugins/axios'
import { CustomUser } from '@/types/authentication'

import categories from '@/data/categories.json'
// import SettingsCard from '@/components/settings/SettingsCard.vue'

export default defineComponent({
  name: 'AlgorithmPage',
  components: {
    // SettingsCard
  },
  setup () {
    const { instance } = useVueSession()
    const selectedCategory = ref(null)
    const selectedSubcategory = ref(null)

    // const subcategories = computed(() => {
    //   const category = _.find(categories, { title: selectedCategory.value })
    //   return category?.subcategories || []
    // })

    const subCategories = ref([])

    const hasSelectedCategory = computed(() => {
      return selectedCategory.value !== null
    })

    async function getCategories () {
      const response = await client.get(`videos/categories/${selectedCategory.value.toLowerCase()}/sub-categories`)
      subCategories.value = response.data
      instance.create(selectedCategory.value, response.data)
    }

    whenever(hasSelectedCategory, () => {
      getCategories()
    })
    
    const requestData = ref({
      preferred_categories: [
        {
          "title": "Sports",
          "subcategories": ["WNBA"]
        },
        {
          "title": "Movies",
          "subcategories": ["Trailers"]
        }
      ]
    })
    return {
      requestData,
      categories,
      subCategories,
      selectedCategory,
      selectedSubcategory
    }
  },
  watch: {
    selectedCategory (n, o) {
      if (n !== o) {
        this.selectedSubcategory === null
      }
    }
  },
  methods: {
    /**
     * 
     */
    async handleAccountDetails () {
      try {
        const response = await this.$client.get<CustomUser>('/accounts/base')
        this.requestData = response.data
      } catch {
        // Handle error
      }
    },
    /**
     * 
     */
    handleAddCategory () {
      const category = _.find(this.requestData.preferred_categories, { title: this.selectedCategory })
      
      if (category) {
        category.subcategories.push(this.selectedSubcategory)
      } else {
        this.requestData.preferred_categories.push({
          title: this.selectedCategory,
          subcategories: [this.selectedSubcategory]
        })
      }
    }
  }
})
</script>
