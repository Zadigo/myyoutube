<template>
  <div class="space-y-2">
    <StudioSettingBlock>
      <template #title>
        Monetization
      </template>

      <template #description>
        If you want to monetize your video, you can do so by enabling the
        monetization feature. This will allow you to earn money from your video
        through ads and other monetization methods. Note that you can enable these
        features globally in your channel settings.
      </template>

      <template #actions>
        <div class="space-y-2">
          <VoltLabel>
            <VoltToggleSwitch v-model="newVideo.monetization.ads" />
            <label>Enable monetization through Ads</label>
          </VoltLabel>

          <VoltLabel>
            <VoltToggleSwitch v-model="newVideo.monetization.gifts" />
            <label>Enable monetization through gifts</label>
          </VoltLabel>
        </div>
      </template>
    </StudioSettingBlock>

    <StudioSettingBlock>
      <template #title>
        Participants
      </template>

      <template #description>
        If your video contains users that need to be tagged,
        you can do so by indicating either their socials or
        their YouTube handle
      </template>

      <div class="my-5 space-y-2">
        <div v-for="(participant, idx) in newVideo.participants" :key="idx" class="flex justify-start gap-1">
          <VoltInputText v-model="participant.fullname" placeholder="Full name" />
          <VoltInputText v-model="participant.url" type="url" placeholder="Social url" />
          <VoltSelect v-model="participant.handle" :options="socials" placeholder="User handle" />
          <VoltButton variant="outlined" color="danger" @click="() => handleRemoveParticipant(idx)">
            <Icon name="i-fa7-solid:trash" />
          </VoltButton>
        </div>

        <VoltButton class="mt-5" rounded @click="handleAddParticipant">
          <Icon name="i-fa7-solid:plus" class="me-2" />
          Add participant
        </VoltButton>
      </div>
    </StudioSettingBlock>

    <StudioSettingBlock>
      <template #title>
        LLM Generation and Text transcription
      </template>

      <template #description>
        If you want to generate an accurate transcript of your video
        or generate a summary, you can do so by enabling the
        LLM generation feature. This will use the video content
        to generate text.
      </template>

      <input type="file" label="Upload a text transcription of your video" />
    </StudioSettingBlock>
  </div>
</template>

<script lang="ts" setup>
const socials = [
  'Facebook',
  'X',
  'Instagram',
  'YouTube'
]

const studioStore = useStudioStore()
const { newVideo } = storeToRefs(studioStore)

/**
 * This function adds a new participant to the
 * video being created. The participant is initialized
 */
function handleAddParticipant () {
  newVideo.value.participants.push({
    fullname: '',
    url: null,
    handle: 'Instagram'
  })
}

/**
 * This function removes a participant from the
 * video being created. The participant is removed
 */
function handleRemoveParticipant(index: number) {
  newVideo.value.participants.splice(index, 1)
}
</script>
