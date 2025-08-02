import type { DefaultMainCategories } from '~/apps/data'
import type { KeywordOperators, JoinOperators } from '~/apps/data/constants/operators'

export interface AlgorithmConditionBlock {
  id: number
  theme: DefaultMainCategories
  keyword_operator: KeywordOperators
  keywords: string[]
  keywords_subconditions: string[]
  video_sections: string[]
  join_operator: JoinOperators
  negation: boolean
}
