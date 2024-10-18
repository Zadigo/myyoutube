import { useAuthentication } from '../store/authentication'
import { VueSessionInstance } from './vue-storages'

import axios from 'axios'

function getBaseURL () {
  if (import.meta.env.MODE === 'development') {
    return import.meta.env.VITE_DEVELOPMENT_URL
  } else {
    return import.meta.env.VITE_PRODUCTION_URL
  }
}

const client = axios.create({
  baseURL: getBaseURL(),
  withCredentials: true,
  headers: { 'Content-Type': 'application/json' },
  timeout: 10000
})

const authClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/auth/v1/',
  withCredentials: true,
  headers: { 'Content-Type': 'application/json' },
  timeout: 10000
})

client.interceptors.request.use(
  request => {
    const store = useAuthentication()
    if (store.accessToken) {
      request.headers.Authorization = `Token ${store.accessToken}`
    }
    return request
  }
)

client.interceptors.response.use(
  response => {
    console.log(response.status === 401)
    if (response.status === 401) {
      const store = useAuthentication()
      store.accessToken = null
      store.refreshToken = null
      VueSessionInstance.remove('authentication')
    }
    return response
  }
)

export {
  authClient,
  axios, client
}

