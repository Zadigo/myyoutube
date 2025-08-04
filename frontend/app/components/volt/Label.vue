<template>
  <div class="flex items-center gap-2">
    <slot>
      <slot name="input" />
      <label>
        <slot name="label" />
      </label>
    </slot>
  </div>
</template>
