<template>
  <div class="block w-full p-6 bg-white shadow-md rounded-lg hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
    <slot name="header" />
    
    <p class="font-normal text-gray-700 dark:text-gray-400">
      <slot />
    </p>
  </div>
</template>
