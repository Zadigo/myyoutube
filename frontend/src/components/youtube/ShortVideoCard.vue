<template>
  <div class="col-sm-12 col-md-8 offset-md-2">
    <div class="card">
      <div class="card-header border-0">
        <!-- TODO: Make this a reusable component -->
        <div class="row">
          <div class="col-2">
            <a href>
              <img src="https://via.placeholder.com/400x400" class="img-fluid z-depth-1 rounded-circle" alt="">
            </a>
          </div>

          <div class="col-10 position-relative">
            <div class="d-flex justify-content-left" @mouseenter="showUserInfo = true" @mouseleave="showUserInfo = false">
              <a href class="me-2">
                <span class="fw-bold">
                  camillembaye
                </span>
              </a>
              <p class="fw-light m-0">Camille Mbaye</p>
            </div>

            <p class="fs-light" v-html="detectHashtags('the bloody AUDACITY of some people 🙄😂 #something #another #google #dosomething')"></p>

            <!-- TODO: Make this a reusable component -->
            <div v-if="showUserInfo" class="card position-absolute w-50 z-index-modal">
              <div class="card-header d-flex justify-content-between">
                <div class="col-2">
                  <img src="https://via.placeholder.com/100x100" class="img-fluid rounded-circle" alt="">
                </div>

                <div class="col-auto">
                  <button type="button" class="btn btn-outline-primary">
                    Subscribe
                  </button>
                </div>
              </div>

              <div class="card-body">
                <p class="fw-bold m-0">camillembaye</p>
                <p class="fs-light fs-7">Camille Mbaye</p>
                <p class="m-0"><span class="fw-bold">317K</span>Abonnés <span class="fw-bold">12.2M</span> J'aime</p>
              </div>

              <div class="card-footer py-4">
                Le mannequin curvy de Tik Tok
              </div>
            </div>

            <button type="button" class="btn btn-outline-primary">
              Subscribe
            </button>
          </div>
        </div>
      </div>

      <div class="card-body">
        <div class="row">
          <div class="col-12">
            <div class="row">
              <div class="col-auto">
                <img src="https://via.placeholder.com/300x500" class="rounded" alt="">
              </div>
              <div class="col-auto d-flex flex-column justify-content-left">
                <button type="button" class="btn btn-floating btn-light shadow-none mb-2 btn-lg">
                  <font-awesome-icon :class="[true ? 'text-danger' : null]" icon="fa-solid fa-heart" />
                </button>

                <div class="fw-bold fs-7 text-center mb-3 text-muted">37.4K</div>

                <button type="button" class="btn btn-floating btn-light shadow-none mb-2 btn-lg">
                  <font-awesome-icon icon="fa-solid fa-message" />
                </button>

                <div class="fw-bold fs-7 text-center mb-3 text-muted">17.4K</div>

                <button type="button" class="btn btn-floating btn-light shadow-none mb-2 btn-lg">
                  <font-awesome-icon icon="fa-solid fa-share" />
                </button>
                <div class="fw-bold fs-7 text-center mb-3 text-muted">567</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'ShortVideoCard',
  data () {
    return {
      showUserInfo: false
    }
  },
  // mounted () {
  //   const links = document.querySelectorAll('a#hashtag')
  //   Array.from(links).forEach((link) => {
  //     const parent = this
  //     const instance = new vue.component('RouterLink')({ to: 'home_view',  parent})
  //     instance.$el.innerHTML = link.innerHTML
  //     instance.$mount(link)
  //   })
  // },
  methods: {
    detectHashtags (text) {
      // const link = new RouterLink()
      const items = []
      const tokens = text.split(' ')
      tokens.forEach((token) => {
        if (token.startsWith('#')) {
          items.push(`<a id="hashtag" href class="fw-bold">${token}</a>`)
        } else {
          items.push(token)
        }
      })
      const newText = items.join(' ')
      return newText
    }
  }
}
</script>
