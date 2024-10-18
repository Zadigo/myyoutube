export interface LoginResponse {
  access: string
  refresh: string
}

export interface CustomUser {
  id: number
  firstname: string
  lastname: string
  get_full_name: string
}

