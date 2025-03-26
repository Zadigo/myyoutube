<template>
  <section class="middle">
    <div class="">      
      <h1 class="font-bold text-1xl">
        Feed builder
      </h1>
      
      <div class="mt-5">
        <v-text-field variant="solo-filled" placeholder="Feed name" flat />

        <v-btn @click="handleUpdateData">Run</v-btn>

        <div class="flex flex-wrap gap-1 mt-5">
          <BaseChip v-for="block in blocks" :key="block" class="flex gap-1 items-center" @click="handleAddBlock(block)">
            <Icon name="fa-solid:plus" />
            {{ block }}
          </BaseChip>
        </div>

        <div>
          <div v-for="(component, i) in createdComponents" :key="i" class="my-3">
            <component v-model="component.data" :is="component.component" :index="i" @update-data="handleUpdateData" @delete-block="handleDeleteBlock" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import Source from '~/components/block/Source.vue'
// import Remove from '~/components/block/Remove.vue'
import Limit from '~/components/block/Limit.vue'
import Regex from '~/components/block/Regex.vue'
import Sort from '~/components/block/Sort.vue'

import { blocks } from '~/data'
import type { BlockNames, CreatedComponent, RequestData, VideoItem } from '~/types'

useHead({
  title: 'Feed creator'
})

const store = useFeed()
const { items } = storeToRefs(store)

const componentMapping: Record<string, Component> = {
  source: markRaw(Source),
  // remove: markRaw(Remove),
  regexp: markRaw(Regex),
  // replace: markRaw('BlockReplace'),
  sort: markRaw(Sort),
  limit: markRaw(Limit)
}


const createdComponents = ref<CreatedComponent[]>([
  {
    position: 1,
    component: componentMapping.source,
    data: {
      source: 'Entire network',
      duration: '7 days'
    }
  }
])


const requestData = ref<RequestData>({
  sources: [],
  regex: [],
  sorting: []
})

const { execute, data } = useFetch('/api/videos', {
  method: 'post',
  immediate: false,
  // params: requestData,
  onResponse() {

  },
  transform(data: VideoItem[]) {
    items.value = data
    return data
  }
})

function handleAddBlock (block: BlockNames) {
  let blockName = block.toLowerCase()

  let dataToWrite = {
    duration: '7 days',
    source: 'Entire network'
  }
  
  if (block === 'Source') {
    dataToWrite = {
      duration: '7 days',
      source: 'Entire network'
    }
  }

  const data: CreatedComponent = { 
    position: createdComponents.value.length + 1, 
    component: componentMapping[blockName],
    data: dataToWrite
  }

  createdComponents.value.push(data)
}

function handleDeleteBlock (index: number) {
  createdComponents.value.splice(index, 1)
}

function handleUpdateData () {
  execute()

  // if (data.value) {
  //   items.value = data.value
  // }
}
</script>

<style lang="scss">
.opacity-enter-active,
.opacity-leave-active {
  transition: all .3s ease-in-out
}
.opacity-enter-from,
.opacity-leave-to {
  opacity: 1;
  transform: translate(.95, .95);
}
.opacity-enter-to,
.opacity-leave-from {
  opacity: 1;
  transform: translate(1, 1);
}
</style>
