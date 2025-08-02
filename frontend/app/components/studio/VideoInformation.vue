<template>
  <div class="card-body">
    <div class="row">
      <div v-if="requestData" class="col-7">
        <VoltInputText v-model="requestData.title" type=" text" placeholder="Title"  flat />

        <div class="alert alert-info fw-light">
          <p class="fw-bold">
            Video ranking
          </p>

          In order for you video to rank correctly, you should describe as much as possible and
          precisely what your video is about then select a category/sub-category that matches
          exactly the subject of the video you are uploading. Users may consider you video to
          be unfit if the category/sub-category don't match what they were expecting.
        </div>

        <v-textarea v-model="requestData.description" cols="30" rows="7" class="my-1" placeholder="Description"  flat no-resize />

        <v-autocomplete v-model="requestData.category" :items="categories" item-title="title" item-value="title"  placeholder="Select a category" flat auto-select-first>
          <VoltInputText />
        </v-autocomplete>

        <v-autocomplete v-model="requestData.subcategory" :items="subCategories" item-title="title" item-value="title"  placeholder="Select a sub-category" flat auto-select-first>
          <VoltInputText />
        </v-autocomplete>
      </div>

      <div class="col-5">
        <!-- TODO: Upload the video at first in order to edit it afterwards -->
        <!-- <base-video-player :video-source="store.previewUrl" :revoke-url="true" @loaded-meta-data="handleFrameInformation" /> -->

        <div class="mt-3">
          <h5>Thumbnail</h5>
          
          <p class="text-muted">
            Select or upload a picture that shows what's in your video.
            A good thumbnail stands out and draws viewers'
            attention. Learn more
          </p>
          
          <div class="row">
            <div v-for="(frame, i) in frames" :key="i" class="col-3">
              <img :src="frame[1]" class="img-fluid" alt="">
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <!-- Paid promotion -->
      <div class="col-12">
        <p class="fw-bold">
          Paid promotion
        </p>

        <p class="fw-light">
          If you accepted anything of value from a third party to make your video, 
          you must let us know. we'll show viewers a message that tells them your 
          video contains paid promotion.
        </p>
        
        <v-switch label="My video contains paid promotion like a product placement, sponsorship, or endorsement" inset />
        
        <p class="fw-light">
          By selecting this box, you confirm that the paid promotion 
          follows our ad policies and any applicable laws and regulations. Learn more
        </p>
      </div>

      <!-- Tags -->
      <div class="col-12">
        <p class="fw-bold">
          Tags
        </p>

        <p class="fw-light">
          Tags can be useful if content in your video is 
          commonly misspelled. Otherwise, tags play a minimal role in helping 
          viewers find your video. Learn more
        </p>

        <v-combobox  placeholder="Add tag" :items="tags" flat chips multiple />
      </div>

      <div class="col-12">
        <p class="fw-bold">
          Language
        </p>

        <p class="fw-light">
          Select your video's language
        </p>

        <v-select  flat />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import type { Categories, FileUploadRequestData, Subcategories, SessionCache } from '~/types';
import { useSessionStorage, whenever } from '@vueuse/core';
import { computed, inject, ref } from 'vue';

// import BaseVideoPlayer from 'src/components/BaseVideoPlayer.vue';

type StringOrNull = string | null

interface ReturnData {
  title: StringOrNull
  description: StringOrNull
  category: StringOrNull
  subcategory: StringOrNull
}

const emit = defineEmits({
  'update:data' (_data: ReturnData) {
    return true
  }
})

const { $client } = useNuxtApp()
const returnData = ref<ReturnData>({
  title: null,
  description: null,
  category: null,
  subcategory: null
})

const frames = ref(null)
const categories = ref<Categories[]>([])
const subCategories = ref<Subcategories[]>([])

const hasCategory = computed(() => {
  return returnData.value.category !== null
})

const requestData = inject<FileUploadRequestData>('requestData')
const tags = ref<string[]>([])

const sessionCache = useSessionStorage<SessionCache>('cache', null, {
  serializer: {
    read (raw) {
      return JSON.parse(raw)
    },
    write (value) {
      return JSON.stringify(value)
    }
  }
})

/**
 * 
 */
async function getSubcategories () {
  try {
    if (instance.keyExists('subcategories')) {
      subCategories.value = instance.retrieve('subcategories')
    } else {
      const response = await $client.get(`/videos/categories/${returnData.value.category}/sub-categories`)
      subCategories.value = response.data
      instance.create('subcategories', response.data)
    }
  } catch {
    // Handle error
  }
}

whenever(hasCategory, () => {
  getSubcategories()
})

async function requestCategories () {
  try {
    if (!('categories' in sessionCache.value)) {
      const response = await $client.get<Categories[]>('/videos/categories')
      sessionCache.value.categories = response.data
    }
  } catch {
    // Handle error
  }
}

/**
 * 
 */
function handleFrameInformation () {
  
}

/**
 * 
 */
function handleChange () {
  emit('update:data', returnData.value)
}

onBeforeMount(async () => {
  await requestCategories()
})
</script>
