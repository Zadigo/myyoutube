<template>
  <section id="site">
    <div class="px-20 grid grid-cols-3 grid-rows-1 h-screen w-full">
      <aside id="navigation" class="border-r-2 border-r-gray-100 p-5">
        Left
      </aside>

      <main id="content" class="p-5">
        <slot />
      </main>

      <aside id="previewer" class="border-l-2 border-l-gray-100 p-5">
        <div class="overflow-y-scroll h-[550px] w-full px-2">
          <BaseSpinner v-if="store.isLoading" />

          <div ref="infiniteEl">
            <BaseCard v-for="(item, index) in items" :key="item.id" class="mb-1">
              {{ item.id }} {{ index }}
            </BaseCard>
          </div>
        </div>
      </aside>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useInfiniteScroll } from '@vueuse/core'

const store = useFeed()

const items = ref(Array.from({ length: 10 }).map((a, b) => {
  return {
    id: b
  }
}))

const infiniteEl = useTemplateRef<HTMLElement>('infiniteEl')
const { reset } = useInfiniteScroll(
  infiniteEl, 
  () => {
    items.value.push({
      id: 598
    })
  }, 
  {
    distance: 10,
    canLoadMore() {
      return true
    }
  }
)

function resetData() {
  reset()
}
</script>

<style lang="scss" scoped>
#previewer {
  div::-webkit-scrollbar {
    display: none;
  }
}
</style>
