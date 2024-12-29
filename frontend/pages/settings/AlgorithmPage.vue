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

        <settings-card title="Algorithm constructor" subtitle="Build your own viewing algorithm">
          <template #default>
            <ConditionalBlocks />
          </template>
        </settings-card>
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
import { useHead } from 'unhead'

import categories from '@/data/categories.json'
import SettingsCard from '@/components/settings/SettingsCard.vue'
import ConditionalBlocks from '@/components/settings/ConditionalBlocks.vue'

export default defineComponent({
  name: 'AlgorithmPage',
  components: {
    ConditionalBlocks,
    SettingsCard
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

    useHead({
      title: 'Algorithm builder',
      meta: [
        {
          name: 'description',
          content: 'Some description to use'
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
