export const videoPaths = [
  '/videos/vid1.mp4',
  '/videos/vid2.mp4',
  '/videos/vid3.mp4',
  '/videos/vid4.mp4',
  '/videos/vid5.mp4',
  '/videos/vid6.mp4',
  '/videos/vid7.mp4',
  '/videos/vid8.mp4',
  '/videos/vid9.mp4'
]

/**
 * Returns a random video path from the predefined list
 * @returns {string} A random video path
 */
export function getRandomVideoPath(): string {
  const randomIndex = Math.floor(Math.random() * videoPaths.length)
  return videoPaths[randomIndex] as string
}
