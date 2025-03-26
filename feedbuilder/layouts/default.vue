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
            <BaseCard v-for="(item, i) in items" :key="item.id" :data-index="i" class="mb-1">
              <h4 class="font-bold text-1xl">
                {{ item.title }}
              </h4>

              <p class="tex-light text-gray-500 text-sm mb-3" >
                {{ item.created_on }}
              </p>

              <p class="font-light">
                {{ item.description }}
              </p>
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
const { items } = storeToRefs(store) 

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
</script>

<style lang="scss" scoped>
#previewer {
  div::-webkit-scrollbar {
    display: none;
  }
}
</style>
