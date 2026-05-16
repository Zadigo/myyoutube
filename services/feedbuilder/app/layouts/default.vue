<template>
  <section id="site">
    <div class="px-5 grid grid-cols-12 grid-rows-1 h-screen w-full">
      <!-- Aside -->
      <lazy-base-aside hydrate-on-idle />

      <!-- Content -->
      <main id="content" class="p-5 overflow-y-scroll col-span-6">
        <slot />
      </main>

      <!-- Videos -->
      <lazy-base-results hydrate-on-idle />
    </div>
  </section>
</template>

<script setup lang="ts">

const infiniteEl = useTemplateRef<HTMLElement>('infiniteEl')
const { reset } = useInfiniteScroll(
  infiniteEl, 
  () => {
    // items.value.push({
    //   id: 598
    // })
  }, 
  {
    distance: 10,
    canLoadMore() {
      return false
    }
  }
)

function resetData() {
  reset()
}

/**
 * Theme
 */

// const theme = ['bg-green-50', 'dark:bg-green-900', 'text-green-900', 'dark:text-green-50']

// onMounted(() => {
//   document.body.classList.add(...theme)
// })

// onUnmounted(() => {
//   document.body.classList.remove(...theme)
// })
</script>

<style lang="scss" scoped>
#previewer {
  div::-webkit-scrollbar {
    display: none;
  }
}
</style>
