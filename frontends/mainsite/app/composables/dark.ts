/**
 * Composable to manage dark mode state
 */
export const useDarkModeComposable = createGlobalState(() => {
  if (import.meta.client) {
    const colorMode = useColorMode()
    const darkMode = useDark({ initialValue: 'auto', initOnMounted: true })
    const toggleDarkMode = useToggle(darkMode)

    return {
      darkMode,
      toggleDarkMode,
      colorMode,  
    }
  } else {
    return {
      darkMode: ref(undefined),
      toggleDarkMode: ref(undefined),
      colorMode: ref(undefined)
    }
  }
})
