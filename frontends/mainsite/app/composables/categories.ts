export function useCategoriesComposable() {
  const categories = ref([
    { id: 1, name: 'Sports', icon: 'i-fa7-solid:soccer-ball' },
    { id: 2, name: 'Music', icon: 'i-fa7-solid:music' },
    { id: 3, name: 'Gaming', icon: 'i-fa7-solid:gamepad' },
    { id: 4, name: 'News', icon: 'i-fa7-solid:newspaper' },
    { id: 5, name: 'Entertainment', icon: 'i-fa7-solid:film' },
    { id: 6, name: 'Education', icon: 'i-fa7-solid:graduation-cap' },
    { id: 7, name: 'Technology', icon: 'i-fa7-solid:laptop-code' },
    { id: 8, name: 'Lifestyle', icon: 'i-fa7-solid:user-friends' }
  ])

  async function load() {
    // Placeholder for loading categories if needed
  }

  return {
    categories,
    load
  }
}

export async function useSubcategoriesComposable() {
  const selectedCategory = ref('Sports')
  const hasSelectedCategory = computed(() => selectedCategory.value !== null)

  const { data } = await useAsyncData('sub-categories', () => {
    return $fetch(`/api/completion/${selectedCategory.value.toLowerCase()}/sub-categories`, {
      method: 'GET',
      baseURL: useRuntimeConfig().public.djangoProdUrl
    })
  }, {
    immediate: false
  })

  return {
    subCategories: data,
    selectedCategory,
    hasSelectedCategory
  }
}
