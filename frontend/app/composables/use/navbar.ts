/**
 * Composables for managing the sidebar state in the application.
 * Provides functionality to toggle the visibility of the sidebar.
 */
export function useSidebar() {
  const showSidebar = ref<boolean>(true)
  const toggle = useToggle(showSidebar)

  return {
    /**
     * Reactive reference to the sidebar visibility state.
     */
    showSidebar,
    /**
     * Function to toggle the sidebar visibility.
     * When called, it will switch the sidebar's visibility state between true and false.
     */
    toggle
  }
}
