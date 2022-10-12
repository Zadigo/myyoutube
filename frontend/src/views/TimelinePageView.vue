<template>
  <base-site>
    <section id="for-you-page">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">
            <div class="card mb-4">
              <div class="card-body">
                <button type="button" class="btn btn-primary shadow-none me-2">
                  <font-awesome-icon icon="fa-solid fa-filter" class="me-2"></font-awesome-icon>
                  {{ $t('Filter') }}
                </button>

                <div class="btn-group ms-auto shadow-none">
                  <button type="button" :class="[showLongVideosTimeline ? 'active' : null ]" class="btn btn-light" @click="showLongVideosTimeline = true">Long</button>
                  <button type="button" :class="[showLongVideosTimeline ? null : 'active' ]" class="btn btn-light" @click="showLongVideosTimeline = false">Shorts</button>
                </div>
              </div>

              <div class="card-footer">
                <input type="text" class="form-control mb-2" placeholder="Search categories" multiple>
                <div class="d-flex justify-content-around">
                  <select class="form-select" aria-label="Default select example">
                    <option selected>Date de mise en ligne</option>
                    <option value="1">Nombres de vues</option>
                    <option value="2">Avis</option>
                    <option value="3">Three</option>
                  </select>

                  <select class="form-select mx-2" aria-label="Default select example">
                    <option selected>{{ $t('Video') }}</option>
                    <option value="1">Chaînes</option>
                    <option value="2">Playlist</option>
                  </select>

                  <select class="form-select" aria-label="Default select example">
                    <option selected>{{ $t('Between X and Y minutes', { x: 4, y: 20 }) }}</option>
                    <option selected>Plus de 20 minutes</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>

        <section v-if="showLongVideosTimeline" class="row">
          <div class="col-12">
            <div class="row">
              <video-section />
            </div>

            <hr class="my-4">

            <div class="row">
              <video-section title="Some recommended section" />
            </div>
          </div>
        </section>
      </div>
    </section>
  </base-site>
</template>

<script>
import BaseSite from '@/layouts/BaseSite.vue'
import VideoSection from '@/components/timeline/VideoSection.vue'

export default {
  name: 'TimelinePageView',
  components: {
    BaseSite,
    VideoSection
  },
  data () {
    return {
      showLongVideosTimeline: true
    }
  }
}
</script>
