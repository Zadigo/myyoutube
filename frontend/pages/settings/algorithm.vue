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

<script setup lang="ts">
import { whenever } from '@vueuse/core'
import { computed, ref } from 'vue'
import type { CustomUser } from '@/types'

import ConditionalBlocks from '@/components/settings/ConditionalBlocks.vue'
import SettingsCard from '~/components/settings/Card.vue'

definePageMeta({
  layout: 'settings'
})

const { client } = useAxiosClient()
// const { instance } = useVueSession()
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

watch(selectedCategory, (n, o) => {
  if (n !== o) {
    selectedSubcategory.value = null
  }
})

/**
 * 
 */
async function handleAccountDetails () {
  try {
    const response = await client.get<CustomUser>('/accounts/base')
    this.requestData = response.data
  } catch {
    // Handle error
  }
}

/**
 * 
 */
function handleAddCategory () {
  const category = requestData.value.preferred_categories.find( () => {
    return {
      title: selectedCategory.value
    }
  })
  
  if (category) {
    category.subcategories.push(this.selectedSubcategory)
  } else {
    requestData.value.preferred_categories.push({
      title: selectedCategory.value,
      subcategories: [selectedSubcategory.value]
    })
  }
}
</script>
