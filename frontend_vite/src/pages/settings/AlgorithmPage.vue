<template>
  <section id="algorithm">
    <div class="row">
      <div class="col-8 offset-md-2">
        <div class="row">
          <div class="col-8">
            <div class="card">
              <div class="card-body">
                <div class="alert alert-info">
                  If no options are selected, YouTube will use 
                  your viewing history to recommend the most 
                  relevant videos
                </div>

                <v-checkbox label="Let YouTube decide which are the most relevant videos for me"></v-checkbox>

                <p>Select your preferred categories</p>
                <div class="actions">
                  <v-select v-model="selectedCategory" :items="categories" placeholder="Select the main category" variant="outlined"></v-select>
                  <v-select v-model="selectedSubcategory" :items="subcategories" placeholder="Select the sub category" variant="outlined"></v-select>
                  <v-btn color="primary" rounded="xl" flat @click="handleAddCategory">
                    <v-icon icon="mdi-plus"></v-icon>
                    Add
                  </v-btn>
                </div>

                <div class="mt-5">
                  <v-switch label="Let YouTube recommend the most popular videos from what users have also watched based on the video that you are currently viewing" inset></v-switch>
                </div>
              </div>
            </div>
          </div>
    
          <aside class="col-4">
            <div class="card">
              <div class="card-body">
                <div v-for="category in requestData.preferred_categories" :key="category.title" class="category mt-3">
                  <h2 class="h5">{{ category.title }}</h2>

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
    
    <div class="col-8 offset-md-2">
      <settings-card title="Blocked channels" subtitle="Channels that you blocked and do not want to see">
        <template #default>
          <div class="list-group">
            <div v-for="i in 5" :key="i" class="list-group-item d-flex justify-content-between align-items-center">
              <div class="d-flex justify-content-start align-items-center gap-3">
                <v-avatar image="/avatar1.png" size="20"></v-avatar>
                <span>Something</span>
              </div>
              <v-btn color="danger" variant="text">
                <font-awesome-icon :icon="['fas', 'fa-trash']" />
              </v-btn>
            </div>
          </div>
        </template>
      </settings-card>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'
import { computed, ref } from 'vue'
import categories from '../../data/categories.json'
import SettingsCard from '../../components/settings/SettingsCard.vue'

export default {
  components: {
    SettingsCard
  },
  setup () {
    const selectedCategory = ref(null)
    const selectedSubcategory = ref(null)

    const subcategories = computed(() => {
      const category = _.find(categories, { title: selectedCategory.value })
      return category?.subcategories || []
    })
    
    // watch(selectedCategory, (n, o) => {
    //   if (n !== o) {
    //     selectedSubcategory.value === null
    //   }
    // })
    
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
      subcategories,
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
}
</script>
