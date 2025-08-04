<template>
  <section id="algorithm">
    <VoltCard class="shadow-sm">
      <template #content>
        <h1 class="font-bold text-3xl">
          Customize your viewing experience
        </h1>
      </template>
    </VoltCard>

    <SettingsCard title="Algorithm constructor" subtitle="Build your own viewing algorithm">
      <template #default>
        <SettingsAlgorithmConditionalBlocks />
      </template>
    </SettingsCard>
  </section>
</template>

<script setup lang="ts">
import { useCategories } from '~/composables/use'

definePageMeta({
  layout: 'settings'
})


const { load, categories } = useCategories()

await load()

provide('categories', categories)


// const selectedCategory = ref(null)
// const selectedSubcategory = ref(null)

// const requestData = ref({
//   preferred_categories: [
//     {
//       "title": "Sports",
//       "subcategories": ["WNBA"]
//     },
//     {
//       "title": "Movies",
//       "subcategories": ["Trailers"]
//     }
//   ]
// })

// watch(selectedCategory, (n, o) => {
//   if (n !== o) {
//     selectedSubcategory.value = null
//   }
// })

// const { data } = useFetch('/accounts/base', {
//   baseURL: useRuntimeConfig().public.djangoProdUrl,
//   method: 'GET',
//   immediate: true,
//   lazy: true
// })
</script>
