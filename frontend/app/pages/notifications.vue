<template>
  <section id="notifications" class="container px-5">
    <div class="row">
      <div class="col-12">
        <div class="card shadow-none">
          <div class="card-body">
            <div class="d-flex justify-content-center gap-2">
              <v-btn to="/notifications" size="x-large" rounded="xl" color="primary" flat>
                <v-badge :content="48" inline>
                  All
                </v-badge>
              </v-btn>
    
              <v-btn to="/notifications/messages" size="x-large" rounded="xl" color="primary" flat>
                <v-badge :content="48" inline>
                  Messages
                </v-badge>
              </v-btn>
              
              <v-btn to="/notifications/updloads" size="x-large" rounded="xl" color="primary" flat>
                <v-badge :content="148" inline>
                  Uploads
                </v-badge>
              </v-btn>
            </div>
          </div>
        </div>
      </div>

      <div class="col-sm-12 col-md-8 offset-md-2 mt-4">
        <article v-for="i in 100" :key="i" class="card shadow-sm mb-1">
          <div class="card-body">
            Notification
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
