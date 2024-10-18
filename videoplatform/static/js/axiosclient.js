axios.defaults.headers.common['Accept-Language'] = 'en'
axios.defaults.headers.common['Content-Type'] = 'application/json'

const axiosclient = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    responseType: 'json',
    withCredentials: true
})

axiosclient.interceptors.request.use(
    request => {
        if (request.method === "post") {
            request.headers['X-CSRFToken'] = PROJECT.init.getCSRF()
        }
        return request
    },

    error => {
        return Promise.reject(error)
    }
)

const createClient = () => {
    return {
        install: (app) => {
            app.config.globalProperties.$http = axiosclient 
        }
    }
}
