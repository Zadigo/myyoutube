import { initializeApp } from 'firebase/app'
import { getDatabase } from 'firebase/database'
import { getFirestore } from 'firebase/firestore'

export default defineNuxtPlugin(_nuxtApp => {
    const config = useRuntimeConfig()

    const app = initializeApp({
        apiKey: config.public.firebaseApiKey,
        authDomain: config.public.firebaseAuthDomain,
        databaseURL: config.public.firebaseDbUrl,
        storageBucket: config.public.firebaseStorageBucket,
        appId: config.public.firebaseAppId,
        projectId: config.public.firebaseProjectId,
        measurementId: config.public.firebaseMeasurementId,
        messagingSenderId: config.public.firebaseMessageSenderId
    })

    const db = getDatabase(app)
    const fireStore = getFirestore()

    return {
        provide: {
            fireStore,
            firepApp: app,
            fireDb: db
        }
    }
})
