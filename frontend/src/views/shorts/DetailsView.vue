<template>
  <section id="fast" style="height:100vh;">
    <div class="row gx-0">
      <div class="col-7 bg-dark">
        <div class="h-100 w-50 z-index-1 mx-auto">
          <img :src="require('@/assets/avatar1.png')" class="img-fluid" alt="">
        </div>
      </div>

      <div class="col-5">
        <div class="user-info p-3 border-bottom">
          <!-- TODO: Use reusable user component info here -->
          <div class="row mb-4">
            <div class="col-2">
              <router-link :to="{ name: 'channel_view' }">
                <img :src="require('@/assets/avatar1.png')" class="img-fluid z-depth-1 rounded-circle" alt="">
              </router-link>
            </div>

            <div class="col-10 position-relative">
              <div class="d-flex justify-content-left" @mouseenter="showUserInfo = true" @mouseleave="showUserInfo = false">
                <router-link :to="{ name: 'channel_view' }" class="me-2">
                  <span class="fw-bold">
                    camillembaye
                  </span>
                </router-link>
                <p class="fw-light m-0">Camille Mbaye</p>
              </div>
              <button type="button" class="btn btn-outline-primary">
                Subscribe
              </button>
            </div>
          </div>

          <div class="row">
            <div class="col-8 align d-flex justify-content-left align-items-center">
              <button type="button" class="btn btn-floating btn-light shadow-none mb-2 btn-lg me-1">
                <font-awesome-icon :class="[true ? 'text-danger' : null]" icon="fa-solid fa-heart" />
              </button>
              <span class="fw-bold fs-small text-muted me-2">15.5.k</span>

              <button type="button" class="btn btn-floating btn-light shadow-none mb-2 btn-lg">
                <font-awesome-icon icon="fa-solid fa-message" />
              </button>
            </div>
          </div>
        </div>

        <div class="comments p-3 bg-light" style="overflow-y: scroll; height:300px;">
          <template v-for="i in 100" :key="i">
            <div :class="[i > 0 ? 'mb-1' : null]" class="card">
              <div class="card-body">
                <div class="d-flex justify-content-around">
                  <div class="col-2 me-3">
                    <img src="http://via.placeholder.com/100x100" class="img-fluid rounded-circle" alt="Image 1">
                  </div>

                  <div clas="col-11 ms-1">
                    <div class="d-flex justify-content-left">
                      <span class="fw-bold me-2">User</span>
                      <span class="text-muted">3 weeks ago</span>
                    </div>

                    <p class="card-text">
                      I can’t stop smiling. I once “borrowed “ my brother’s shoes and accidentally ran into him
                      and his friends. The whole time i was talking to them his eyes were laser focused on the shoes. I tried
                      cutting the conversation short but at some point he leaned closer and went “ is that my
                      shoes“. He roasted me but it was all lighthearted and fun. I can totally relate to the
                      sisters
                    </p>

                    <div class="btn-group shadow-none">
                      <button type="button" class="btn btn-primary btn-sm shadow-none">Report</button>
                      <button type="button" class="btn btn-info btn-sm shadow-none">Reply</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </div>

        <div class="actions p-3 border-top">
          <input type="text" class="form-control p-2">
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'DetailsView'
}
</script>
