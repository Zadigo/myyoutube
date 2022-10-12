<template>
  <section id="algorithm">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12 col-md-8 offset-md-2">
          <div class="card mb-2">
            <div class="card-body">
              <h2>{{ $t('Privacy') }}</h2>
            </div>
          </div>

          <div class="card mb-1">
            <div class="card-header">
              <h3>General</h3>
              <p class="m-0 text-muted">{{ $t('Manage what you share on X', { platform: 'YouTube'}) }}</p>
            </div>

            <div class="card-body">
              <settings-block :items="general"></settings-block>
            </div>
          </div>

          <div class="card">
            <div class="card-header">
              <h3>{{ $t('Ad personalization') }}</h3>
              <p class="m-0 text-muted">{{ $t('Manage what you share on X', { platform: 'YouTube'}) }}</p>
            </div>
          
            <div class="card-body">
              <div class="card-text">
                Google makes your ads more useful on Google services 
                (such as Search or YouTube), and on websites & apps 
                that partner with Google to show ads

                <div class="list-group my-2">
                  <div v-for="(item, i) in ads" :key="i" class="list-group-item">
                    <div class="form-check form-switch">
                      <input :id="item.name" v-model="item.selected" class="form-check-input" type="checkbox" role="switch">
                      <label :for="item.name" class="form-check-label">
                        {{ item.text }}
                      </label>
                    </div>
                  </div>
                </div>

                <h4 class="mt-4 fw-bold">
                  How your ads are personalized
                </h4>
                <p>
                  Ads are based on personal info you've added to your Google 
                  Account, data from advertisers that partner with Google, 
                  and Google's estimation of your interests. Choose any 
                  factor to learn more or update your preferences. Learn how to control the ads you see
                </p>
                <p class="text-center">
                  <button type="button" class="btn btn-light shadow-none" @click="showAdvanced = !showAdvanced">
                    {{ $t('Show categories') }}
                  </button>
                </p>
              </div>
            </div>

            <div v-if="showAdvanced" class="card-footer">
              <!-- https://adssettings.google.com/u/0/authenticated?hl=en -->
              <div class="wrapper">
                <ul class="d-flex flex-wrap justify-content-around list-unstyled">
                  <li v-for="i in 30" :key="i">Google</li>
                </ul>
              </div>
            </div>
          </div>

          <hr class="my-4">

          <h3 class="fw-bold">
            {{ $t('Sensitive ad categories on X', { platform: 'YouTube' }) }}
          </h3>
          <p class="text-muted">
            Select the categories for which you want to see less of
          </p>

          <settings-block :items="sensitiveCategories"></settings-block>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import SettingsBlock from '@/components/account/SettingsBlock.vue'

export default {
  name: 'PrivacyView',
  components: {
    SettingsBlock
  },
  data () {
    return {
      showAdvanced: false,
      general: [
        {
          name: 'playlists-privacy',
          text: "Keep all my saved playlists private",
          selected: false
        },
        {
          name: 'subscriptions-privacy',
          text: "Keep all my subscriptions private ",
          selected: false
        }
      ],
      ads: [
        {
          name: 'ads-privacy',
          text: "Personalize ads",
          selected: false
        }
      ],
      sensitiveCategories: [
        {
          name: 'alcohol',
          text: 'Alcohol'
        },
        {
          name: 'dating',
          text: 'Dating'
        },
        {
          name: 'gambling',
          text: 'Gambling'
        },
        {
          name: 'pregnancy and Parenting',
          text: 'Pregnancy and Parenting'
        },
        {
          name: 'Weight Loss',
          text: 'Weight Loss'
        }
      ]
    }
  }
}
</script>

<style scoped>
li {
    border: 1px solid black;
    padding: 1rem;
    border-radius: .3rem;
    width: 100%;
    font-size: 1rem;
    font-weight: 400;
    margin: .3rem;
    text-align: center;
    text-decoration: none;
    vertical-align: middle;
    cursor: pointer;
    user-select: none;
    border: 1px solid #f8f9fa;
    background-color: #f8f9fa;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
  }

  .wrapper {
    width: 100%;
    height: auto;
    overflow: hidden;
  }
</style>
