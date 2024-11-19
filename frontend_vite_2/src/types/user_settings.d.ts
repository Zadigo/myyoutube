export type BooleanOperator = 'And' | 'Or'
export type NegationOperators = 'Not negated' | 'Not'
export type KeywordOperator = 'Exact match' | 'Include related' | 'Approximate match' | 'Expression' | 'Exclude'
export type KeywordOperatorArray = (KeywordOperator)[]

export interface KeywordSubcondition {
    operator: KeywordOperator
    keywords: string[]
}

export interface AlgorithmConditionBlock {
    id: number
    theme: string
    keyword_operator: KeywordOperator
    keywords: string[]
    keywords_subconditions: KeywordSubcondition[]
    video_sections: string[]
    join_operator: 'And' | 'Or'
    negation: boolean
}

