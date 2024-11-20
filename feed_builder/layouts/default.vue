<template>
  <section class="site bg-secondary">
    <!-- Navbar -->

    <div class="container-fluid">
      <aside class="navigation border-right">
        <div class="row">
          <div class="col-12">
            Left
          </div>
        </div>
      </aside>

      <main class="content">
        <div class="row">
          <div class="col-12">
            <slot />
          </div>
        </div>
      </main>

      <aside class="previewer border-left">
        <div class="row">
          <div class="col-12">
            <v-progress-circular v-if="store.isLoading" />

            <v-infinite-scroll ref="infinite" :height="550" :items="items" :on-load="handleLoad">
              <template v-for="(item, index) in items" :key="item">
                <div class="card mb-1">
                  <div class="card-body">
                    {{ item.id }} {{ index }}
                  </div>
                </div>
              </template>
            </v-infinite-scroll>
          </div>
        </div>
      </aside>
    </div>
    
    <!-- Footer -->
  </section>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const store = useFeed()

const items = ref(Array.from({ length: 200 }).map((a, b) => {
  return {
    id: b
  }
}))

const infinite = ref<HTMLElement>(null)

onMounted(() => {
  console.log(infinite.value)
})

async function handleLoadItems () {
  setTimeout(() => {
    items.value.push({
      id: 598
    })
  }, 500);
}

async function handleLoad({ done }) {
  store.isLoading = true
  await handleLoadItems()
  done('ok')
  store.isLoading = false
}
</script>

<style lang="scss" scoped>
%column {
  padding: 1rem;
}

%centered_column {
  text-align: center;
  @extend %column;
}

.site {
  .container-fluid {
    display: grid;
    grid-template-columns: 15% 50% 35%;
    grid-template-rows: 1fr;
    height: 100vh;
  }

  .navigation {
    @extend %centered_column;
  }

  .content {
    @extend %column;
    overflow-y: scroll;
  }

  .previewer {
    @extend %centered_column;
    overflow-y: scroll;
  }
}
</style>
