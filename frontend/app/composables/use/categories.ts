export function useCategories() {
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

  // whenever(hasSelectedCategory, () => {
  //   execute()
  //   getCategories()
  //   subCategories.value = response.data
  //   instance.create(selectedCategory.value, response.data)
  // })

  async function load() {

  }

  return {
    load,
    categories
  }
}

export function useSubcategories(categories) {
  const { categories: allCategories } = useCategories()
  const subCategories = ref([])

  const selectedCategory = ref('Sports')
  const hasSelectedCategory = computed(() => selectedCategory.value !== null)

  async function load() {
    const { data } = await useAsyncData(() => {
      return Promise.all([
        $fetch(`videos/categories/${selectedCategory.value.toLowerCase()}/sub-categories`, {
          method: 'GET',
          baseURL: useRuntimeConfig().public.djangoProdUrl
        })
      ])
    }, {
      immediate: false
    })

    if (data) {
      categories.value = data.value || []
    }
  }

  return {
    load,
    subCategories,
    selectedCategory,
    hasSelectedCategory
  }
}
