import { z } from 'zod'

export const AlgorithmKeywordSubconditionSchema = z.object({
  operator: z.enum(KEYWORD_OPERATORS),
  keywords: z.string().array()
})

export type AlgorithmKeywordSubcondition = z.infer<typeof AlgorithmKeywordSubconditionSchema> 

export const AlgorithmConditionBlockSchema = z.object({
  id: z.number(),
  theme: z.string(),
  keyword_operator: z.enum(KEYWORD_OPERATORS),
  keywords: z.string().array(),
  keywords_subconditions: AlgorithmKeywordSubconditionSchema.array(),
  video_sections: z.string().array(),
  join_operator: z.enum(JOIN_OPERATORS),
  negation: z.boolean().default(false)
})

export type AlgorithmConditionBlock = z.infer<typeof AlgorithmConditionBlockSchema>
