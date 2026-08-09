export const DEFAULT_SEXUAL_CONTENT = [
  'Graphic sexual activity',
  'Nudity',
  'Suggestive - Without nudity',
  'Content involving minors',
  'Abusive title or description',
  'Other sexual content'
] as const

export type DefaultSexualContentReport = (typeof DEFAULT_SEXUAL_CONTENT)[number]

export const DEFAULT_VIOLENT_OR_REPULSIVE = [
  'Adults fighting',
  'Physical attack',
  'Youth violence',
  'Animal abuse'
] as const

export type DefaultViolentOrRepulsive = (typeof DEFAULT_VIOLENT_OR_REPULSIVE)[number]

export const DEFAULT_HATRED_OR_ABUSIVE = [
  'Promotes hatred or violence',
  'Abusing vulnerable individuals',
  'Abusive title or description'
] as const

export type DefaultHatredOrAbusive = (typeof DEFAULT_HATRED_OR_ABUSIVE)[number]

export const DEFAULT_REPORT_TYPES = [...DEFAULT_SEXUAL_CONTENT, ...DEFAULT_VIOLENT_OR_REPULSIVE, ...DEFAULT_HATRED_OR_ABUSIVE]

export type DefaultReportTypes = DefaultSexualContentReport | DefaultViolentOrRepulsive | DefaultHatredOrAbusive

export const reportTypes: { title: string, reports: DefaultReportTypes[] }[] = [
  {
    'title': 'Sexual content',
    'reports': [
      'Graphic sexual activity',
      'Nudity',
      'Suggestive - Without nudity',
      'Content involving minors',
      'Abusive title or description',
      'Other sexual content'
    ]
  },
  {
    'title': 'Violent or repulsive content',
    'reports': [
      'Adults fighting',
      'Physical attack',
      'Youth violence',
      'Animal abuse'
    ]
  },
  {
    'title': 'Hatred or abusive content',
    'reports': [
      'Promotes hatred or violence',
      'Abusing vulnerable individuals',
      'Abusive title or description'
    ]
  }
]
