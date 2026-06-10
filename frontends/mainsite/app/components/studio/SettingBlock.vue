<template>
  <div class="p-10 bg-slate-50 dark:bg-primary rounded-lg">
    <h3 class="font-bold mb-2">
      <slot name="title" />
    </h3>

    <div class="font-light">
      <slot name="description" />
    </div>

    <slot>
      <div class="mt-5">
        <slot name="actions" />
      </div>
    </slot>
  </div>
</template>
