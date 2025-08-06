<template>
  <section id="site">
    <div class="px-5 grid grid-cols-12 grid-rows-1 h-screen w-full">
      <aside id="navigation" class="border-r-2 border-r-gray-100 p-5 col-span-3">
        <ul>
          <li v-for="(feed, idx) in feeds" :key="idx" class="bg-slate-50 cursor-pointer hover:bg-gray-100 p-2 rounded" @click="feedsStore.setCurrentFeed(feed)">
            {{ feed.name }}
          </li>
        </ul>

        <div class="mt-10">
          Current: {{ currentFeed }}
        </div>
      </aside>

      <main id="content" class="p-5 overflow-y-scroll col-span-6">
        <slot />
      </main>

      <aside id="previewer" class="border-l-2 border-l-gray-100 bg-gray-100 p-5 col-span-3">
        <div v-if="items.length > 0" class="overflow-y-scroll h-[550px] w-full px-2">
          <div ref="infiniteEl">
            <VoltCard v-for="(item, i) in items" :key="item.id" :data-index="i" class="mb-1">
              <template #content>
                <h4 class="font-bold text-1xl">
                  {{ item.title }}
                </h4>

                <p class="tex-light text-gray-500 text-sm mb-3" >
                  {{ item.created_on }}
                </p>

                <p class="font-light">
                  {{ item.description }}
                </p>
              </template> 
            </VoltCard>
          </div>
        </div>

        <div v-else class="text-center text-gray-500 mt-10">
          Feed does not have any items yet.
        </div>
      </aside>
    </div>
  </section>
</template>

<script setup lang="ts">
const store = useVideoStore()
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

const feedsStore = useFeedsStore()
const { currentFeed, feeds } = storeToRefs(feedsStore)
</script>

<style lang="scss" scoped>
#previewer {
  div::-webkit-scrollbar {
    display: none;
  }
}
</style>
