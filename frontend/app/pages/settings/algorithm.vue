<template>
  <section id="algorithm">
    <div class="row">
      <div class="col-sm-12 col-md-8 offset-md-2">
        <div class="card mb-2">
          <div class="card-body">
            <h2>
              Customize your viewing experience
            </h2>
          </div>
        </div>

        <settings-card title="Algorithm constructor" subtitle="Build your own viewing algorithm">
          <template #default>
            <SettingsConditionalBlocks />
          </template>
        </settings-card>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import type { CustomUser } from '~/types'

definePageMeta({
  layout: 'settings'
})

const selectedCategory = ref(null)
const subCategories = ref([])
const selectedSubcategory = ref(null)

const hasSelectedCategory = computed(() => {
  return selectedCategory.value !== null
})

const { data } = await useAsyncData(() => {
  return Promise.all([
    $fetch(`videos/categories/${selectedCategory.value.toLowerCase()}/sub-categories`, {
      method: 'GET',
      baseURL: useRuntimeConfig().public.djangoProdUrl
    })
  ])
}, {
  immediate: false,
  watch: [selectedCategory]
})

console.log(data)


// whenever(hasSelectedCategory, () => {
//   execute()
//   getCategories()
//   subCategories.value = response.data
//   instance.create(selectedCategory.value, response.data)
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
