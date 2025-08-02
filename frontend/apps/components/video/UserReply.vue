<template>
  <article class="card my-1 shadow-none" aria-label="">
    <div class="card-body">
      <div class="d-flex justify-content-around">
        <div class="me-3">
          <NuxtLink :to="`/channels/ch_noienozinfoz`" aria-label="">
            <v-img src="/avatar3.png" class="img-fluid rounded-circle" width="40px" alt="Image 3" />
          </NuxtLink>
        </div>

        <div clas="ms-1">
          <div class="d-flex justify-content-left">
            <NuxtLink :to="`/channels/ch_noienozinfoz`" aria-label="">
              <span class="fw-bold me-2">Cee Dee</span>
              <span class="text-body-tertiary">3 weeks ago</span>
            </NuxtLink>
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
import type { PropType } from 'vue';
import type { VideoComment } from '~/apps/types';

defineProps({
  reply: {
    type: Object as PropType<VideoComment>, 
    default: () => {},
    required: false
  }
})
</script>
