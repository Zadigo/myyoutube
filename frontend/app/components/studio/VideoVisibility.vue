<template>
  <div class="space-y-3">
    <StudioSettingBlock>
      <template #title>
        Age restriction
      </template>
      
      <template #description>
        <div class="flex-col my-5">
          <p class="font-bold">Do you want to restrict your video to an adult audience?</p>

          <p class="font-light">
            Age-restricted videos are not shown in certain areas of YouTube. 
            These videos may have limited or no ads monetization
          </p>
        </div>
      </template>

      <template #actions>
        <VoltLabel>
          <VoltToggleSwitch v-model="newVideo.visibility.age_restricted" />
          <label>{{ ageRestrictedLabel }}</label>
        </VoltLabel>
      </template>
    </StudioSettingBlock>
    
    <StudioSettingBlock>
      <template #title>
        Visibility
      </template>

      <template #actions>
        <StudioSubSettingBlock>
          <template #description>
            Choose when to publish
          </template>

          <!-- Publication Date -->
          <VoltDatePicker v-model="newVideo.publication.publication_date" :min="minDate" />
          <VoltInputText v-model="newVideo.publication.publication_time" type="time" />

          <!-- Public/Private -->
          <VoltLabel>
            <VoltToggleSwitch v-model="newVideo.visibility.public" />
            <label>
              {{ newVideo.visibility.public ? 'Public' : 'Private' }}
            </label>
          </VoltLabel>

          <!-- Subscribers -->
          <VoltLabel>
            <VoltToggleSwitch v-model="newVideo.visibility.subscribers_only" />
            <label>
              {{ newVideo.visibility.subscribers_only ? 'Subscribers only' : 'Everyone' }}
            </label>
          </VoltLabel>
        </StudioSubSettingBlock>

        <!-- Premiere -->
        <StudioSubSettingBlock callout>
          <template #description>
            Announcing a Premiere video shows the users that a video will be coming
            soon. You can set a date and time for the premiere to start and also
            create a teaser video for it
          </template>

          <VoltLabel>
            <VoltToggleSwitch v-model="newVideo.visibility.is_premiere" />
            <label>Announce première</label>
          </VoltLabel>

          <input v-if="newVideo.visibility.is_premiere" type="file" placeholder="Teaser" />
        </StudioSubSettingBlock>

        <StudioSubSettingBlock callout>
          <template #description>
            You can post your video to a panel of users that you selected
            to watch it before it goes public. This is useful for getting feedback
            and making changes before the video is released to the public. The panel
            does not count towards the view count of the video and can only watch
            within 5 minutes of the video being posted.
          </template>

          <VoltLabel>
            <VoltToggleSwitch v-model="newVideo.visibility.panelize" />
            <label>Limit to panel</label>
          </VoltLabel>
          
          <VoltInputText v-if="newVideo.visibility.panelize" class="w-full" placeholder="Enter user emails" />
        </StudioSubSettingBlock>
      </template>
    </StudioSettingBlock>
  </div>
</template>

<script lang="ts" setup>
const storeStudio = useStudioStore()
const { newVideo } = storeToRefs(storeStudio)

const ageRestrictedLabel = computed(() => {
  if (newVideo.value.visibility.age_restricted) {
    return 'Yes, restrict my video to viewers over 18'
  } else {
    return "No, don't restrict my video to viewers over 18 only"
  }
})

const { $dayjs } = useNuxtApp() 
const minDate = toRef($dayjs?.date())
</script>
