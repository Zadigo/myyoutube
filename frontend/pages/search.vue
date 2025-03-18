<template>
  <section id="search">
    <div class="row">
      <div class="col-sm-12 col-md-8">
        <div class="card shadow-none border">
          <div class="card-body d-flex justify-content-start gap-3">
            <BaseSkeleton :loading="true" width="250px" height="250px" class="rounded-2" />

            <div class="mt-4">
              <h1 class="h4">
                Video name
              </h1>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
