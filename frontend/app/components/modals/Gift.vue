<template>
  <v-dialog id="gifts" v-model="show" width="700" persistent>
    <v-card>
      <v-card-text>
        <div class="alert alert-danger">
          You have purchased no gifts yet. You can buy gifts here before pursuing.
        </div>

        <div class="container">
          <div class="row">
            <article v-for="i in 30" id="donation" :key="i" class="col-3 gx-1 gy-1 fw-light">
              <div class="card shadow-none border-sm text-center">
                <div class="card-body">
                  Gift 1
                </div>
              </div>
            </article>
          </div>
        </div>
      </v-card-text>

      <v-card-actions>
        <v-btn variant="tonal" color="dark" @click="show=false">
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
const emit = defineEmits({
  'update:modelValue' (_value: boolean) {
    return true
  }
})

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
})

const show = computed({
  get: () => props.modelValue,
  set: (value) => {
    emit('update:modelValue', value)
  }
})
</script>

<style lang="scss" scoped>
#donation {
  cursor: pointer;
}

#donation:hover {
  opacity: .9;
}
</style>
