<template>
  <!-- TODO: Transform to drawer -->
  <v-dialog id="classification-modal" v-model="show" location="right" :width="400" temporary>
    <v-card>
      <v-card-text>
        <div class="container">
          <div class="row">
            <div class="col-12">
              <h2 class="h5">
                Classification
              </h2>

              <div class="alert alert-warning">
                Use this tool to signal that this video was not properly
                categorized by the creator and therefore does not correspond to
                the result you were expecting
              </div>

              <v-list>
                <v-list-item>
                  <v-switch label="Mark as wrong category" inset />
                </v-list-item>

                <v-list-item>
                  <v-switch label="Block this channel" inset />
                </v-list-item>
              </v-list>

              <v-divider />
            </div>
          </div>
        </div>

        <div class="d-flex justify-content-end gap-2 mt-3 p-4">
          <v-btn variant="outlined" color="primary" rounded="xl" flat @click="show=false">
            Cancel
          </v-btn>

          <v-btn color="primary" rounded="xl" flat>
            <font-awesome :icon="['fas', 'fa-save']" class="me-2" />
            Save
          </v-btn>
        </div>
      </v-card-text>
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
