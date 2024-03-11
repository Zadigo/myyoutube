import { defineStore } from 'pinia'

const useAuthentication = defineStore('authentication', {
  state: () => ({
    token: 'e7fd852212dde1b0f34063e9b08acb588806dedf'
  })
})

export {
  useAuthentication
}
