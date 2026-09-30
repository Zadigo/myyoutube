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
        <u-input v-model="newVideo.title" class="w-full" placeholder="Title" />
        <u-textarea v-model="newVideo.description" cols="4" class="my-1 w-full resize-none" placeholder="Description" />
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
        <u-input-menu v-model="newVideo.category" :items="categories" item-label="title" placeholder="Select a category" />
        <u-input-menu v-model="newVideo.subcategory" :items="subCategories" item-label="title" placeholder="Select a sub-category" />
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
          <nuxt-img :src="frame[1]" class="img-fluid" alt="" />
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

      <u-switch v-model="newVideo.has_paid_promotion" label="My video contains paid promotion like a product placement, sponsorship, or endorsement" />

      <div v-if="newVideo.has_paid_promotion" class="font-light italic my-3">
        By selecting this box, you confirm that the paid promotion 
        follows our ad policies and any applicable laws and regulations

        <u-button variant="subtle" class="mt-2" href="/help/video-paid-promotion">
          <Icon name="i-fa7-solid:external-link-alt" class="me-2" />
          Learn more
        </u-button>
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
        <u-input-menu :items="newVideo.tags" placeholder="Tags" class="w-full" />
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
          <u-select v-model="newVideo.publication.language" :items="languages" class="w-full" />
          <u-input-menu v-model="newVideo.publication.recording_location" :items="locations" class="w-full" placeholder="Location" />
        </div>
      </template>
    </StudioSettingBlock>
  </div>
</template>

<script lang="ts" setup>
const { newVideo } = useNewVideoComposable()

const { data: subCategories, execute: getSubcategories } = useAsyncData(
  `subCategories-${newVideo.value.category}`, 
  () => $fetch(`/api/completion/${newVideo.value.category}/sub-categories`),
  { method: 'GET', immediate: false, default: () => [] as Subcategories[]}
)

const { data: categories } = useAsyncData(
  'categories', 
  () => $fetch<Categories>('/api/completion/categories'), 
  { method: 'GET', default: () => [] as Categories[] }
)

const { data: languages } = useAsyncData(
  'languages',
  () => $fetch<string[]>('/api/completion/languages'),
  { method: 'GET', default: () => [] as string[] }
)

const { data: locations } = useAsyncData(
  'locations',
  () => $fetch<string[]>('/api/completion/locations'),
  { method: 'GET', default: () => [] as string[] }
)

const frames = ref<string | null>(null)
</script>
