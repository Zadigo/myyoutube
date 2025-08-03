export const defaultSexualContent = [
  'Graphic sexual activity',
  'Nudity',
  'Suggestive - Without nudity',
  'Content involving minors',
  'Abusive title or description',
  'Other sexual content'
] as const

export type DefaultSexualContentReport = (typeof defaultSexualContent)[number]

export const defaultViolentOrRepulsive = [
  'Adults fighting',
  'Physical attack',
  'Youth violence',
  'Animal abuse'
] as const

export type DefaultViolentOrRepulsive = (typeof defaultViolentOrRepulsive)[number]

export const defaultHatredOrAbusive = [
  'Promotes hatred or violence',
  'Abusing vulnerable individuals',
  'Abusive title or description'
] as const

export type DefaultHatredOrAbusive = (typeof defaultHatredOrAbusive)[number]

export const defaultReportTypes = [...defaultSexualContent, ...defaultViolentOrRepulsive, ...defaultHatredOrAbusive]

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
