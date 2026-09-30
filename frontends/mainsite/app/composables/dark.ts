/**
 * Composable to manage dark mode state
 */
export const useDarkModeComposable = createGlobalState(() => {
  const colorMode = useColorMode()
  const darkMode = useDark({ initialValue: 'auto', initOnMounted: true })

  let toggleDarkMode = () => {}

  if (import.meta.client) {
    toggleDarkMode = useToggle(darkMode)
  }

  return {
    darkMode,
    colorMode,
    toggleDarkMode
  }

})
