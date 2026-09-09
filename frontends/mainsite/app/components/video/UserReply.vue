<template>
  <article class="my-1 shadow-none bg-primary-50 rounded-lg max-w-5xl ms-auto">
    <u-card>
      <div class="flex justify-around">
        <div class="me-3">
          <nuxt-link :to="`/channels/ch_noienozinfoz`" aria-label="">
            <u-avatar src="/avatars/avatar3.png" size="xl" alt="Image 3" />
          </nuxt-link>
        </div>

        <div class="ms-1">
          <div class="flex justify-start">
            <nuxt-link :to="`/channels/ch_noienozinfoz`" aria-label="">
              <span class="fw-bold me-2">Cee Dee</span>
              <span class="text-primary-400">3 weeks ago</span>
            </nuxt-link>
          </div>

          <p class="card-text">
            Gotta give Kendra points for not totally losing her professional
            "cool" when she realized she'd been called out on live TV.
          </p>

          <div class="my-3">
            <u-badge>
              @creator
            </u-badge>

            <u-badge color="neutral">
              Aimé par le createur
            </u-badge>
          </div>

          <u-button type="button" variant="subtle">
            <span class="mdi mdi-thumb-up me-2" />12.3k
          </u-button>
            
          <u-button type="button" variant="subtle">
            <span class="mdi mdi-thumb-down me-2" />26
          </u-button>
            
          <u-button type="button" variant="subtle">
            Repondre
          </u-button>
        </div>
      </div>
    </u-card>
  </article>
</template>

<script lang="ts" setup>
defineProps<{ reply: VideoReplyNode }>()
</script>
