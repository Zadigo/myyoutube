import { z } from 'zod'
import { defaultMainCategories } from '../constants'

export const fileUploadRequestDataSchema = z.object({
  video: z.instanceof(File).nullable(),
  title: z.string().nullable(),
  description: z.string().nullable(),
  channel_playlist: z.string().nullable(),
  recording_location: z.string().nullable(),
  visibility: z.boolean(),
  category: z.enum(defaultMainCategories),
  subcategory: z.string().nullable(),
  age_restricted: z.boolean()
})

export type FileUploadRequestDataSchema = z.infer<typeof fileUploadRequestDataSchema>
