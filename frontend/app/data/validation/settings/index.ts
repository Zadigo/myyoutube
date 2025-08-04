import z from 'zod'
import { joinOperators, keywordOperators } from '~/data/constants'

export const AlgorithmKeywordSubconditionSchema = z.object({
  operator: z.enum(keywordOperators),
  keywords: z.string().array()
})

export type AlgorithmKeywordSubcondition = z.infer<typeof AlgorithmKeywordSubconditionSchema> 

export const AlgorithmConditionBlockSchema = z.object({
  id: z.number(),
  theme: z.string(),
  keyword_operator: z.enum(keywordOperators),
  keywords: z.string().array(),
  keywords_subconditions: AlgorithmKeywordSubconditionSchema.array(),
  video_sections: z.string().array(),
  join_operator: z.enum(joinOperators),
  negation: z.boolean().default(false)
})

export type AlgorithmConditionBlock = z.infer<typeof AlgorithmConditionBlockSchema>
