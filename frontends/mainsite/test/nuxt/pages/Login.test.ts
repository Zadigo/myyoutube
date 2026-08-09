import { mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it, expect, vi } from 'vitest'
import Login from '~/pages/login.vue'

describe('pages > login', () => {
  it('render login page', async () => {
    const component = await mountSuspended(Login)
    
    const email = component.find('input[type="email"]')
    const password = component.find('input[type="password"]')
    const button = component.find('button')

    expect(email.exists()).toBe(true)
    expect(password.exists()).toBe(true)
    expect(button.exists()).toBe(true)
  })
})
