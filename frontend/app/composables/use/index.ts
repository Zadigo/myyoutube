export * from './categories'
export * from './modals'
export * from './navbar'
export * from './playlists'
export * from './settings'
export * from './utils'
export * from './video'
export * from './viewing_profile'
export * from './feed'

/**
 * Composable used to manage the sidebar state
 */
// const [useProvideSidebar, useSidebar] = createInjectionState(() => {
//   if (import.meta.server) {
//     return {
//       showSidebar: true,
//       toggleSidebar: () => {}
//     }
//   }

//   const [showSidebar, toggleSidebar] = useToggle()

//   return {
//     showSidebar, 
//     toggleSidebar
//   }
// })

// export { useProvideSidebar, useSidebar }
