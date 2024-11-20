<template>
  <section class="middle">
    <div class="row">
      <div class="col-sm-12 col-md-12">
        <h1 class="h5">Feed builder</h1>
      </div>

      <div class="col-sm-12 col-md-12">
        <v-text-field variant="solo-filled" placeholder="Feed name" flat />

        <v-chip-group>
          <v-chip v-for="block in blocks" :key="block" @click="handleAddBlock(block)">
            <font-awesome icon="plus" />
            {{ block }}
          </v-chip>
        </v-chip-group>
      </div>
      
      <div class="col-sm-12 col-md-12 mt-4">
        <TransitionGroup name="opacity" mode="out-in">
          <component :is="component.name" v-for="(component, i) in createdComponents" :key="i" :index="i" class="my-1" @delete-block="handleDeleteBlock" />
        </TransitionGroup>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import Source from '@/components/block/Source.vue'
import Regex from '@/components/block/Regex.vue'
import Sort from '~/components/block/Sort.vue'

type Blocks = 'Source' | 'Remove' | 'RegExp' | 'Replace' | 'Sort' | 'Limit'

interface CreatedComponent {
  position: number
  name: 'source' | 'remove' | 'regex' | 'replace' | 'sort' | 'limit'
}

const blocks: Blocks[] = [
  'Source',
  'Remove',
  'RegExp',
  'Replace',
  'Sort',
  'Limit'
]

export default defineNuxtComponent({
  name: 'Index',
  components: {
    Source,
    Sort,
    Regex
  },
  setup() {
    const createdComponents = ref<CreatedComponent[]>([
      {
        position: 1,
        name: 'source'
      },
      {
        position: 2,
        name: 'regex'
      },
      {
        position: 3,
        name: 'sort'
      }
    ])

    useHead({
      title: 'Feed creator'
    })

    return {
      createdComponents,
      blocks
    }
  },
  methods: {
    handleAddBlock (block: Blocks) {
      let blockName = block.toLowerCase()
      
      if (block === 'RegExp') {
        blockName = 'regex'
      }

      const lastItem = this.createdComponents[this.createdComponents.length - 1]

      this.createdComponents.push({
        position: lastItem.position + 1,
        name: blockName
      })
    },
    handleDeleteBlock (index: number) {
      this.createdComponents.splice(index, 1)
    }
  }
})
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
