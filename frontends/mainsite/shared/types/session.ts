import { z } from 'zod'

export interface SessionData {}

/**
 * @deprecated use SessionData instead
 */
export interface SessionCache {
  categories: Arrayable<string>
}

/**
 * TODO: Move this to a separate file (schema) and import it here
 */
export const SessionDataSchema = z.object({
  language: z.object({
    choice: z.enum(['fr', 'en', 'es']).default('fr').describe('Used to store the language preference of the user'),
    selected: z.boolean().default(false)
  }).describe('Used to store the language preference of the user'),
  recommendations: z.array(z.number()),
  searchHistory: z.array(z.string())
})

export type _SessionData = z.infer<typeof SessionDataSchema>

