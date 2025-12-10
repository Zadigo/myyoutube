import { addDoc, collection, doc, getDoc, updateDoc } from 'firebase/firestore'
import type { Nullable } from '~/types'


interface UserSession {
  createdAt: Date
  updatedAt: Date
  data: Record<string, unknown>
}

export const useSession = createGlobalState(<S extends UserSession>(collectionName = 'youtubeSessions') => {
  if (import.meta.server) {
    return {
      sessionId: ref(undefined),
      session: ref<S | undefined>(undefined),
      create: async () => {}
    }
  } else {
    const fireStore = useFirestore()
    const _collectionName = collectionName || 'youtubeSessions'
    const sessionId = useCookie<Nullable<string>>('sessionid', { sameSite: true, secure: true })
    
    async function _create() {
      if (!isDefined(sessionId)) {
        const sessionDefaults = {
          createdAt: new Date(),
          updatedAt: new Date(),
          data: {}
        }
        
        try {
          const collectionRef = collection(fireStore, _collectionName)
          const sessionDoc = await addDoc(collectionRef, sessionDefaults)
          sessionId.value = sessionDoc.id
        } catch (e) {
          console.error('Error creating session document:', e)
        }
      }
    }

    const create = useThrottleFn(_create, 5000)
  
    /**
     * Key in local storage but not on Firebase
     */

    if (isDefined(sessionId)) {
      const docRef = doc(fireStore, _collectionName, sessionId.value)

      getDoc<S>(docRef).then((docSnap) => {
        if (!docSnap.exists()) {
          sessionId.value = null
        }
      })
    } else {
      create()
    }

    if (!isDefined(sessionId)) {
      console.error('Session ID is not defined.')
      return {
        sessionId: ref(undefined),
        session: ref<S | undefined>(undefined),
        create: async () => { }
      }
    }
  
    const docRef = doc(fireStore, _collectionName, sessionId.value)
    const _session = useDocument<S>(docRef)
  
    const session = computed({
      get: () => _session.value,
      set: async (newValue) => {
        if (isDefined(newValue)) {
          await updateDoc(docRef, newValue, { merge: true })
        }
      }
    })
  
    return {
      sessionId,
      session,
      create
    }
  }
})
