import { defineStore } from 'pinia'

const useAuthentication = defineStore('authentication', {
  state: () => ({
    token: null
  })
})

export {
  useAuthentication
}
