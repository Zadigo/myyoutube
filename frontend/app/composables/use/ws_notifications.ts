/**
 * Composable used to manage user's notifications
 * It uses WebSocket to receive real-time notifications from the server
 * and provides methods to add and remove notifications.
 */
export const useNotificationsComposable = createSharedComposable(() => {
  const notifications = ref<Notification[]>([])

  function add(notification: Notification) {
    notifications.value.push(notification)
  }

  function remove(id: string) {
    notifications.value = notifications.value.filter(n => n.id !== id)
  }

  const wsObject = useWebSocket('ws://localhost:3000/notifications', {
    autoConnect: true,
    autoReconnect: true,
    onMessage: (event) => {
      // Do something
    },
    onError: (event) => {
      console.error('WebSocket error:', event)
    }
  })

  return {
    wsObject,
    notifications,
    add,
    remove
  }
})
