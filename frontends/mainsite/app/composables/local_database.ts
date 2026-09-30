export function uselocalDatabase() {
  const comments = useLocalStorage<BaseComment[]>('comments', [])
  const likedComments = useLocalStorage<string[]>('likedComments', [])
  const dislikedComments = useLocalStorage<string[]>('dislikedComments', [])

  return {
    comments,
    likedComments,
    dislikedComments
  }
}
