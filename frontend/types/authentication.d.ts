import type { UserChannel } from "./channels"

export interface LoginApiResponse {
  access: string
  refresh: string
}

export interface CustomUser {
  id: number
  firstname: string
  lastname: string
  get_full_name: string
}

export interface UserProfile {
  id: number
  avatar: string
  birthdate: string
  telephone: string
  address: string
  city: string
  zip_code: string
  is_professional: boolean
}

export interface ViewingProfile {
  id: number
  account_type: string
  subscriptions: string[],
  night_mode: boolean
  algorithm_decides: boolean
  recommend_popular_videos: boolean
  preferred_categories: string[]
  performance: string
  playlists_private: boolean
  subscriptions_private: boolean
  personalize_ads: false
}

export interface BlockedChannel {
  channel: UserChannel
  user: CustomUser
}
