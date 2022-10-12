<template>
  <section id="algorithm">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12 col-md-6 offset-md-2">
          <!-- General -->
          <div class="card mb-1">
            <div class="card-body">
              <!-- Recommendation preference -->
              <p class="alert alert-info">{{ $t('No options selected', { platform: 'YouTube'}) }}</p>
              <base-checkbox-vue id="recommendation-preference" :label="$t('Recommendation preference')" />

              <div class="card shadow-none">
                <div class="card-body">
                  <label for="categories">Select the categories for which you will have the most interest</label>
                  <input type="text" class="form-control p-2" placeholder="Categories" name="categories">
                  <input type="text" class="form-control p-2 my-2" placeholder="Subcategories" name="subcategories" disabled>

                  <div class="list-group list-group-flush">
                    <div class="list-group-item ps-0">
                      <div class="form-check form-switch">
                        <input id="recommend-from-current" class="form-check-input" type="checkbox" role="switch" />
                        <label class="form-check-label" for="recommend-from-current">
                          Let YouTube recommend the most popular videos from what
                          users have also watched based on the video that you
                          are currently viewing
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="card-header">
              <h4>{{ $t('Blocked channels') }}</h4>
              <p class="text-muted">Channels that you blocked and do not want to see</p>
            </div>
            <div class="card-body">
              <div class="list-group">
                <div v-for="i in 5" :key="i" class="list-group-item list-group-item-action p-3 d-flex align-items-center justify-content-between">
                  <span>Channel {{ i }}</span>
                  <button type="button" class="btn btn-sm btn-danger">
                    <font-awesome-icon icon="fa-solid fa-eraser" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-12 col-md-3">
          <div class="card">
            <div class="card-header">
              <h3>{{ $t('Preferred categories') }}</h3>
            </div>

            <div class="card-body">
              <h4 class="fw-bold h5 mb-1">Sports</h4>
              <div class="list-group my-3">
                <a class="list-group-item list-group-item-action d-flex align-items-center justify-content-between">
                  <span>WNBA</span>
                  <button type="button" class="btn btn-sm btn-rounded btn-dark shadow-none">
                    <font-awesome-icon icon="fa-solid fa-trash" />
                  </button>
                </a>
              </div>
            </div>

            <div class="card-footer text-right">
              <button type="button" class="btn btn-danger">
                <font-awesome-icon icon="fa-solid fa-eraser" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import BaseCheckboxVue from '@/layouts/bootstrap/BaseCheckbox.vue'
// import SettingsBlock from '@/components/account/SettingsBlock.vue'

export default {
  name: 'AlgorithmPreferenceView',
  components: {
    BaseCheckboxVue
    // SettingsBlock
}
}
</script>
