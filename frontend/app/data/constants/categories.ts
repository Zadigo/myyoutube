export const defaultMainCategories = [
  'Documentaries',
  'TV Shows',
  'Fashion',
  'Music',
  'Sports',
  'Podcasting'
] as const

export type DefaultMainCategories = (typeof defaultMainCategories)[number] | (string & {})


export const defaultCategories = [
  {
    'title': 'Documentaries',
    'subcategories': [
      {
        'title': 'Animal',
        'restrictions': false
      }
    ]
  },
  {
    'title': 'TV Shows',
    'subcategories': [
      {
        'title': 'Cooking',
        'restrictions': false
      },
      {
        'title': 'Fashion',
        'restrictions': false
      },
      {
        'title': 'Politics',
        'restrictions': true
      },
      {
        'title': 'Real TV',
        'restrictions': false
      }
    ]
  },
  {
    'title': 'Fashion',
    'subcategories': [

    ]
  },
  {
    'title': 'Music',
    'subcategories': [
    ]
  },
  {
    'title': 'Sports',
    'subcategories': [
      {
        'title': 'Basketball',
        'restrictions': false
      },
      {
        'title': 'Tennis',
        'restrictions': false
      }
    ]
  },
  {
    'title': 'Gaming',
    'subcategories': [
    ]
  },
  {
    'title': 'YouTuber channels',
    'subcategories': [

    ]
  },
  {
    'title': 'Podcasting',
    'subcategories': [
      {
        'title': 'General',
        'restrictions': false
      },
      {
        'title': 'Politics',
        'restrictions': true
      }
    ]
  }
]
