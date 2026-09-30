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
        <u-switch v-model="newVideo.monetization.ads" label="Enable monetization through Ads" />
        <u-switch v-model="newVideo.monetization.gifts" label="Enable monetization through gifts" />
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
          <u-input v-model="participant.fullname" placeholder="Full name" />
          <u-input v-model="participant.url" type="url" placeholder="Social url" />
          
          <u-select v-model="participant.handle" :options="Array.from(SOCIALS)" placeholder="User handle" />

          <u-button @click="() => removeParticipant(idx)">
            <Icon name="i-fa7-solid:trash" />
          </u-button>
        </div>

        <u-button class="mt-5" rounded @click="addParticipant">
          <Icon name="i-fa7-solid:plus" class="me-2" />
          Add participant
        </u-button>
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
        to generate text. This will also allow your videos to be searchable
        with a higher level of accuracy by using in-video speech search functionality.
      </template>

      <u-file-upload type="file" label="Upload a text transcription of your video" />
    </StudioSettingBlock>
  </div>
</template>

<script lang="ts" setup>
const { newVideo, addParticipant, removeParticipant } = useNewVideoComposable()
</script>
