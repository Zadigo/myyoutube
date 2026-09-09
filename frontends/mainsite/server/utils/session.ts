import type { H3Event } from 'h3'
import { useFirebaseAdmin } from '#shared/server_firebase'
import { SESSION_COOKIE_NAME } from '#shared/session_constants'
import type { SessionData } from '#shared/types/session'

const DEFAULT_SESSION_DATA: SessionData = {}

/**
 * Resolves the current session document, creating one and setting the
 * cookie if none exists. The cart lives as a field on this same document,
 * so cart and session always share the exact same id — no drift possible.
 * @param event The H3Event object from the request context
 */
export async function getOrCreateSession(event: H3Event) {
  const { db } = useFirebaseAdmin()
  const collectionRef = db.collection(SESSION_COOKIE_NAME)
  const existingId = getCookie(event, SESSION_COOKIE_NAME)

  if (existingId) {
    const docRef = collectionRef.doc(existingId)
    const snapshot = await docRef.get()

    if (snapshot.exists) {
      return { sessionId: existingId, docRef, data: snapshot.data() as SessionData }
    }
    // Cookie is stale (doc deleted/expired) → fall through and recreate below.
  }

  const docRef = collectionRef.doc()
  await docRef.set({ ...DEFAULT_SESSION_DATA, updatedAt: new Date(), createdAt: new Date() })

  const config = useRuntimeConfig(event)

  setCookie(event, SESSION_COOKIE_NAME, docRef.id, {
    httpOnly: false, // must stay readable client-side, useCookie() relies on it
    sameSite: 'strict',
    secure: process.env.NODE_ENV === 'production',
    domain: process.env.NODE_ENV === 'production' ? config.public.siteUrl.replace(/^https?:\/\//, '') : undefined
  })

  return { sessionId: docRef.id, docRef, data: DEFAULT_SESSION_DATA }
}
