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
                  <label for="categories">Select your preferred categories</label>
                  <base-autocomplete :items="[{ text: 'Documentary' }]" @item-selected="(value) => { choices.category = value.text }">
                    <input type="text" class="form-control p-2" placeholder="Categories" name="categories">
                  </base-autocomplete>
                  
                  <base-autocomplete :items="[{ text: 'Animal' }]" class="my-2" @item-selected="(value) => { choices.subcategory = value.text }">
                    <input :disabled="choices.category === null || choices.category === ''" type="text" class="form-control p-2" placeholder="Subcategories" name="subcategories">
                  </base-autocomplete>

                  <button type="button" class="btn btn-primary" @click="updateCategory">
                    <font-awesome-icon icon="fa-solid fa-plus" class="me-2" />
                    {{ $t('Add') }}
                  </button>
                  
                  <div class="list-group list-group-flush mt-4">
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
              <template v-for="category in categories" :key="category">
                <h4 class="fw-bold h5 mb-1">{{ category }}</h4>
                <div class="list-group my-3">
                  <a v-for="subcategory in refactoredCategories[category]" :key="subcategory" class="list-group-item list-group-item-action d-flex align-items-center justify-content-between">
                    <span>{{ subcategory }}</span>
                    <button type="button" class="btn btn-sm btn-rounded btn-dark shadow-none">
                      <font-awesome-icon icon="fa-solid fa-trash" />
                    </button>
                  </a>
                </div>
              </template>
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
import _ from 'lodash'
import BaseAutocomplete from '@/layouts/bootstrap/BaseAutocomplete.vue'
import BaseCheckboxVue from '@/layouts/bootstrap/BaseCheckbox.vue'
// import SettingsBlock from '@/components/account/SettingsBlock.vue'

export default {
  name: 'AlgorithmPreferenceView',
  components: {
    BaseAutocomplete,
    BaseCheckboxVue
    // SettingsBlock
  },
  data () {
    return {
      choices: {
        category: null,
        subcategory: null
      },
      preferredCategories: [
        {
          id: 1,
          category: 'Sports',
          subcategory: 'WNBA'
        }
      ]
    }
  },
  computed: {
    categories () {
      return _.map(this.preferredCategories, (item) => {
        return item.category
      })
    },
    refactoredCategories () {
      const items = {}
      _.forEach(this.preferredCategories, (item) => {
        items[item.category] = []
      })
      _.forEach(this.preferredCategories, (item) => {
        items[item.category].push(item.subcategory)
      })
      return items
    }
  },
  methods: {
    async updateCategory () {
      this.preferredCategories.push({
        id: 3,
        ...this.choices
      })
      this.choices = {
        category: null,
        subcategory: null
      }
    }
  }
}
</script>
