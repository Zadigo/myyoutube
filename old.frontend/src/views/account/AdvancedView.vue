<template>
  <section id="algorithm">
    <div class="container-fluid">
      <div class="row">
        <div v-if="!isAuthenticated" class="col-sm-12 col-md-8 offset-md-2">
          <base-template-card class="mb-1">
            <div v-if="!enterCode" class="card-body">
              <base-input id="email" placeholder="Email" />
              <base-input id="password" :placeholder="$t('Password')" class="my-1" />
            </div>
            <div v-else class="card-body">
              <div class="d-flex">
                <base-input id="validation-code" class="mx-1 text-center fw-bold fs-3" />
                <base-input id="validation-code" class="mx-1 text-center fw-bold fs-3" />
                <base-input id="validation-code" class="mx-1 text-center fw-bold fs-3" />
                <base-input id="validation-code" class="mx-1 text-center fw-bold fs-3" />
              </div>
            </div>
          
            <div class="card-footer">
              <button v-if="!enterCode" type="button" class="btn btn-primary" @click="validateCode">
                {{ $t('Receive validation code') }}
              </button>
              <button v-else type="button" class="btn btn-primary" @click="authenticate">
                {{ $t('Signin') }}
              </button>
            </div>
          </base-template-card>
        </div>

        <div v-else class="col-sm-12 col-md-8 offset-md-2">
          <base-template-card>
            <div class="card-body">
              <h2>{{ $t('Gifts') }}</h2>

              <base-list-group-checkbox id="gifts" :items="gifts" class="mb-2" />
            </div>

            <div class="card-footer">
              <button type="button" class="btn btn-primary">
                <font-awesome-icon icon="fa-solid fa-cart-shopping" class="me-2" />
                {{ $t('Buy gifts') }}
              </button>
            </div>
          </base-template-card>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import BaseListGroupCheckbox from '@/layouts/bootstrap/listgroups/BaseListGroupCheckbox.vue'
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'
import BaseTemplateCard from '@/layouts/bootstrap/cards/BaseTemplateCard.vue'
// import SettingsBlockVue from '@/components/account/SettingsBlock.vue'

export default {
  name: 'PerformanceView',
  components: {
    BaseInput,
    BaseListGroupCheckbox,
    BaseTemplateCard
    // SettingsBlockVue
  },
  data () {
    return {
      isAuthenticated: false,
      enterCode: false,
      general: [
        {
          name: 'playlists-privacy',
          text: "Keep all my saved playlists private",
        },
        {
          name: 'subscriptions-privacy',
          text: "Keep all my subscriptions private ",
        }
      ],
      gifts: [
        { name: 'Rose', subtitle: '500 - 0.99€' },
        { name: 'Voiture', subtitle: '1000 - 50€' }
      ]
    }
  },
  methods: {
    validateCode () {
      this.enterCode = true
    },
    authenticate () {
      this.isAuthenticated = true
    }
  }
}
</script>
