export * from './debounce'

export function inProduction() {
    return import.meta.env.MODE !== 'development'
}
