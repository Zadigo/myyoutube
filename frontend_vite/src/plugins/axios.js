import { useAuthentication } from '../store/authentication'

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
  timeout: 10000
})

client.interceptors.request.use(
  request => {
    const store = useAuthentication()
    if (store.token) {
      request.headers.Authorization = `Token ${store.token}`
    }
    return request
  },
  error => {
    return Promise.reject(error)
  }
)

client.interceptors.response.use(
  response => {
    const store = useAuthentication()
    store
    return response
  },
  error => {
    return Promise.reject(error)
  }
)

export {
  client,
  axios
}
