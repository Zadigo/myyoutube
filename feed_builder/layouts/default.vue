<template>
  <section class="site bg-secondary">
    <!-- Navbar -->

    <div class="container-fluid">
      <aside class="navigation">
        <div class="row">
          <div class="col-12">
            Left
          </div>
        </div>
      </aside>

      <main class="content bg-white">
        <div class="row">
          <div class="col-12">
            <slot />
          </div>
        </div>
      </main>

      <aside class="previewer">
        <div class="row">
          <div class="col-12">
            Right
          </div>
        </div>
      </aside>
    </div>
    
    <!-- Footer -->
  </section>
</template>

<style lang="scss" scoped>
%column {
  padding: 1rem;
}

%centered_column {
  text-align: center;
  @extend %column;
}

.site {
  .container-fluid {
    display: grid;
    grid-template-columns: 15% 50% 35%;
    grid-template-rows: 1fr;
    height: 100vh;
  }

  .navigation {
    @extend %centered_column;
  }

  .content {
    @extend %column;
    overflow-y: scroll;
  }

  .previewer {
    @extend %centered_column;
  }
}
</style>
