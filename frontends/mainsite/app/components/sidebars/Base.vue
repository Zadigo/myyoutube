<template>
  <nav class="fixed top-0 left-0 bottom-0 p-3 shadow-sm w-(--sidebar-width) z-50 bg-white dark:bg-primary dark:text-surface-50">
    <div :class="theme.base">
      <ul id="links" class="space-y-5">
        <li v-for="navLink in links" :key="navLink.to" class="transition-all ease-in-out duration-200 text-sm font-light bg-primary-50 has-[.router-link-exact-active]:bg-primary-100 has-[.router-link-exact-active]:text-primary-500 dark:bg-primary-800 dark:text-surface-50 hover:bg-primary-100 rounded-lg">
          <nuxt-link-locale :to="navLink.to" :aria-current="route.path === navLink.to" :class="theme.link" class="">
            <icon :name="navLink.icon" />
            {{ navLink.name }}
          </nuxt-link-locale>
        </li>
      </ul>

      <slot name="footer" />
    </div>
  </nav>
</template>

<script setup lang="ts">
defineProps<{ links: { name: string, to: string, icon: string }[] }>()

const route = useRoute()

const theme = ref({
  base: `mx-3 mt-[calc(55px+1rem)] flex-col justify-between`,
  link: `p-2 px-4 rounded-lg flex gap-3 items-center font-semibold`
})
</script>
