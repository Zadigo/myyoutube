<template>
  <article class="card my-1 shadow-none bg-primary-50 rounded-lg p-5 max-w-5xl ms-auto" aria-label="">
    <div class="card-body">
      <div class="d-flex justify-content-around">
        <div class="me-3">
          <nuxt-link :to="`/channels/ch_noienozinfoz`" aria-label="">
            <u-avatar src="/avatars/avatar3.png" size="xl" alt="Image 3" />
          </nuxt-link>
        </div>

        <div class="ms-1">
          <div class="d-flex justify-content-left">
            <nuxt-link :to="`/channels/ch_noienozinfoz`" aria-label="">
              <span class="fw-bold me-2">Cee Dee</span>
              <span class="text-body-tertiary">3 weeks ago</span>
            </nuxt-link>
          </div>

          <p class="card-text">
            Gotta give Kendra points for not totally losing her professional
            "cool" when she realized she'd been called out on live TV.
          </p>

          <div class="my-3">
            <div class="badge badge-danger me-1">
              @creator
            </div>

            <div class="badge badge-light">
              Aimé par le createur
            </div>
          </div>

          <div class="btn-group shadow-none">
            <button type="button" class="btn btn-primary btn-sm shadow-none">
              <span class="mdi mdi-thumb-up me-2" />12.3k
            </button>
              
            <button type="button" class="btn btn-primary btn-sm shadow-none">
              <span class="mdi mdi-thumb-down me-2" />26
            </button>
              
            <button type="button" class="btn btn-info btn-sm shadow-none">
              Repondre
            </button>
          </div>
        </div>
      </div>
    </div>
  </article>
</template>

<script lang="ts" setup>
defineProps<{ reply: VideoReplyNode }>()
</script>
