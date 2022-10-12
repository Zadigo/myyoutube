<template>
  <section id="algorithm">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12 col-md-8 offset-md-2">
          <base-template-card class="mb-2">
            <div class="card-body">
              <h2>{{ $t('viewing_experience') }}</h2>
              <p class="text-muted">Playback settings apply to this browser only</p>
            </div>
          </base-template-card>
          
          <base-template-card>
            <div class="card-body">
              <!-- <base-checkbox :is-radio="true" :initial="true" label="Auto (recommended)" name="viewing-experience" />
              <base-checkbox :is-radio="true" label="1080p" name="viewing-experience" />
              <base-checkbox :is-radio="true" label="720p" name="viewing-experience" /> -->
              <base-list-group-item-radio id="performance" :items="items" />
            </div>
          </base-template-card>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import BaseTemplateCard from '@/layouts/bootstrap/cards/BaseTemplateCard.vue'
// import BaseCheckbox from '@/layouts/bootstrap/BaseCheckbox.vue'
import BaseListGroupItemRadio from '@/layouts/bootstrap/listgroups/BaseListGroupItemRadio.vue'

export default {
  name: 'PerformanceView',
  components: {
    BaseTemplateCard,
    // BaseCheckbox,
    BaseListGroupItemRadio
  },
  data () {
    return {
      items: [
        {
          name: 'Auto (recommended)'
        },
        {
          name: '1080p'
        },
        {
          name: '720p'
        }
      ]
    }
  }
}
</script>
