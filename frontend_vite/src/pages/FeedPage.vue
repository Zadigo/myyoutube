<template>
  <section id="videos">
    <header class="card shadow-sm">
      <div class="card-body">
        Something
      </div>
    </header>

    <section id="content" class="mt-5">
      <div class="row">
        <div v-for="i in 100" :key="i" class="col-3 my-1">
          <router-link :to="{ name: 'video_details', params: { id: 'vd_eiZEze3EF' } }" aria-label="">
            <article class="card shadow-sm">
              <div class="card-body"></div>
            </article>
          </router-link>
        </div>
      </div>
    </section>
  </section>
</template>
