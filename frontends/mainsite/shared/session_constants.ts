/**
 * Name of the collection in Firestore that stores the session data.
 * This collection is used to store the session information associated with a specific user session.
 * Each document in this collection represents a session and contains relevant session data.
 * The session ID is used as a reference to associate session data with a specific user session.
 * The collection name is defined as a constant to ensure consistency across the application.
 * It is recommended to use a unique and descriptive name for the collection to avoid conflicts with other collections.
 * In this case, the collection name is set to 'test_sessions' for testing purposes.
 * In a production environment, it is advisable to use a more appropriate name that reflects the purpose of the collection.
 */
export const SESSION_COOKIE_NAME = 'test_sessions'
