export interface LoginApiResponse {
  access: string
  refresh: string
}

export interface CustomLoginApiResponse extends LoginApiResponse {
  failureCount: number
}

export type RefreshApiResponse = Pick<LoginApiResponse, 'access'>
