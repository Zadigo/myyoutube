import type { _DatabaseObject } from '..'

/**
 * @deprecated
 */
export interface CustomUser extends _DatabaseObject {
  firstname: string
  lastname: string
  get_full_name: string
}

export interface UserProfile extends _DatabaseObject {
  avatar: string
  birthdate: string
  telephone: string
  address: string
  city: string
  zip_code: string
  is_professional: boolean
}

export interface ViewingProfile extends _DatabaseObject {
  account_type: string
  subscriptions: string[]
  night_mode: boolean
  algorithm_decides: boolean
  recommend_popular_videos: boolean
  preferred_categories: string[]
  preferred_ad: string[]
  performance: string
  blocked_keywords: []
  playlists_private: boolean
  subscriptions_private: boolean
  personalize_ads: false
}
