<template>
  <div class="space-y-2">
    <!-- Title/Description -->
    <StudioSettingBlock>
      <template #description>
        Your title should be an accurate representation of your video and can influence user moderation
        if it is misleading or not. The title should be short and concise, ideally under 60 characters.
        Your description should explain as much as possible and precisely what your video is about
      </template>
      
      <template #actions>
        <VoltInputText v-model="newVideo.title" class="w-full" placeholder="Title" />
        <VoltTextarea v-model="newVideo.description" cols="4" class="my-1 w-full resize-none" placeholder="Description" />
      </template>
    </StudioSettingBlock>

    <!-- Ranking -->
    <StudioSettingBlock help="/help/video-ranking" callout>
      <template #title>
        Video ranking
      </template> 

      <template #description>
        In order for you video to rank correctly, you should select a category/sub-category that matches
        exactly the subject of the video you are uploading. Users may consider you video to
        be unfit if the category/sub-category don't match what they were expecting.
      </template>

      <template #actions>
        <VoltAutoComplete v-model="newVideo.category" :suggestions="categories" item-label="title" placeholder="Select a category">
          <VoltInputText />
        </VoltAutoComplete>

        <VoltAutoComplete v-model="newVideo.subcategory" :suggestions="subCategories" item-label="title" placeholder="Select a sub-category">
          <VoltInputText />
        </VoltAutoComplete>
      </template>
    </StudioSettingBlock>

    <!-- Thumbnail -->
    <StudioSettingBlock help="/help/video-thumbnail" callout>
      <template #title>
        Thumbnail
      </template>

      <template #description>
        Select or upload a picture that shows what's in your video.
        A good thumbnail stands out and draws viewers' attention
      </template>

      <template #actions>
        <div v-for="(frame, i) in frames" :key="i" class="col-3">
          <img :src="frame[1]" class="img-fluid" alt="">
        </div>
      </template>
    </StudioSettingBlock>

    <!-- Paid Promotion -->
    <StudioSettingBlock help="/help/video-thumbnail" callout>
      <template #title>
        Paid promotion
      </template>

      <template #description>
        If you accepted anything of value from a third party to make your video, 
        you must let us know. We'll show viewers a message that tells them your 
        video contains paid promotion.
      </template>

      <VoltLabel class="my-5">
        <VoltToggleSwitch v-model="newVideo.has_paid_promotion" />
        <label>My video contains paid promotion like a product placement, sponsorship, or endorsement</label>
      </VoltLabel>

      <div v-if="newVideo.has_paid_promotion" class="font-light italic my-3">
        By selecting this box, you confirm that the paid promotion 
        follows our ad policies and any applicable laws and regulations

        <VoltButton variant="text" color="primary" class="mt-2" href="/help/video-paid-promotion">
          <Icon name="i-fa7-solid:external-link-alt" class="me-2" />
          Learn more
        </VoltButton>
      </div>
    </StudioSettingBlock>
    
    <!-- Tags -->
    <StudioSettingBlock>
      <template #title>
        Tags
      </template>

      <template #description>
        Tags can be useful if content in your video is 
        commonly misspelled. Otherwise, tags play a minimal role in helping 
        viewers find your video. Learn more
      </template>

      <template #actions>
        <VoltAutoComplete :suggestions="newVideo.tags" placeholder="Tags" class="w-full" />
      </template>
    </StudioSettingBlock>

    <!-- Language/Location -->
    <StudioSettingBlock>
      <template #title>
        Language and location
      </template>

      <template #description>
        Select the language of your video and the location where it was recorded.
        This information can help viewers find your video and understand its context. Specifying
        the parameters can improve the discoverability of your video for your target audience
      </template>

      <template #actions>
        <div class="w-80 space-y-2">
          <VoltSelect v-model="newVideo.publication.language" class="w-full" />
          <VoltInputText v-model="newVideo.publication.recording_location" class="w-full" placeholder="Location" />
        </div>
      </template>
    </StudioSettingBlock>
  </div>
</template>

<script lang="ts" setup>
import type { Categories, Subcategories } from '~/types'

const studioStore = useStudioStore()
const { newVideo, hasCategory } = storeToRefs(studioStore)

/**
 * Fetch subcategories based on the selected category
 */
const { data: subCategories, execute: getSubcategories } = useFetch<Subcategories>(`/videos/categories/${newVideo.value.category}/sub-categories`, {
  baseURL: useRuntimeConfig().public.djangoProdUrl,
  method: 'GET',
  immediate: false
})

whenever(hasCategory, () => {
  getSubcategories()
})

const { execute, data: categories } = useFetch<Categories>('/videos/categories', {
  baseURL: useRuntimeConfig().public.djangoProdUrl,
  keepalive: true,
  lazy: true,
  method: 'GET'
})

await execute()

const frames = ref<string | null>(null)
</script>
