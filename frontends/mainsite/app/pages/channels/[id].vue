<template>
  <section id="channel" class="relative text-primary-50 dark:text-primary-50">
    <header ref="headerEl" class="relative w-full h-[80vh] rounded-lg overflow-hidden">
      <div :class="{ 'scale-105': shouldAnimate }" class="bg-center bg-no-repeat h-full w-full z-20 transition-all ease-in-out duration-300" :style="{ backgroundImage: 'url(/banners/banner1.jpg)' }" />
      <div class="bg-linear-to-t from-black via-black/50 to-black-/10 blur-lg w-full h-full absolute top-0 left-0 z-30" />
      
      {{ mousePositionX }} {{ mousePositionY }}

      <div class="p-10 absolute top-4/12 left-0 z-40">
        <volt-avatar image="/avatars/avatar1.png" size="xlarge" shape="circle" class="mb-5" />
        <h1 class="font-bold text-6xl">
          {{ currentChannel.data.userChannel.name }}
        </h1>

        <p class="text-light font-light mb-10Ò">310 vidéos</p>

        <volt-button class="mt-8" rounded>
          <Icon name="i-fa7-solid:plus" />
          Subscribe
        </volt-button>
      </div>
    </header>
  </section>
</template>

<script setup lang="ts">
import { should } from 'vitest'

const { id } = useRoute().params
const currentChannel = await $fetch(`/api/channels/${id}`, { method: 'GET' })

/**
 * Header
 */

const headerEl = useTemplateRef<HTMLElement>('headerEl')

const shouldAnimate = ref(false)
const mousePositionX = ref(0)
const mousePositionY = ref(0)

if (import.meta.client) {
  const { x, y, isOutside } = useMouseInElement(headerEl)
  syncRef(mousePositionX, x, { direction: 'rtl' })
  syncRef(mousePositionY, y, { direction: 'rtl' })

  watch(isOutside, (newVal) => {
    if (!newVal) {
      shouldAnimate.value = true
    } else {
      shouldAnimate.value = false
    }
  })
}
</script>
