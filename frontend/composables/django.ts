export function useDjangoUtilities() {
  function mediaPath(path: string | null | undefined, altImage?: string | undefined): string | undefined {
    const baseUrl = useRuntimeConfig().public.djangoProdUrl

    if (path) {
      if (path.startsWith('http')) {
        return path
      }

      const fullPath = path.startsWith('/media') ? `${path}` : `/media/${path}`
      return new URL(fullPath, baseUrl).toString()
    } else {
      return altImage
    }
  }

  return {
    mediaPath
  }
}
