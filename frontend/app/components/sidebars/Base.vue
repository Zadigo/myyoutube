<template>
  <div :class="theme.base">
    <div id="links" class="space-y-5">
      <NuxtLink v-for="navLink in links" :key="navLink.to" :to="navLink.to" :aria-current="route.path === navLink.to" :class="theme.link">
        <Icon :name="navLink.icon" />
        {{ navLink.name }}
      </NuxtLink>
    </div>

    <slot name="footer" />
  </div>
</template>

<script setup lang="ts">
defineProps<{ links: { name: string, to: string, icon: string }[] }>()

const route = useRoute()

const theme = ref({
  base: `mx-3 mt-4 flex-col justify-between`,
  link: `p-2 px-4 rounded-lg flex gap-3 items-center font-semibold`
})
</script>

<style lang="scss" scoped>
$box_shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);

a {
  &.active {
    border-radius: 5px;
    box-shadow: var(--shadow-sm);
  }
  
  &[class*="-exact-active"] {
    z-index: 2;
    color: var(--p-surface-0);
    background-color: var(--p-primary-500);
    border-color: var(--p-primary-500);
    border-radius: 5px;
    box-shadow: var(--shadow-sm);
  }
}
</style>
