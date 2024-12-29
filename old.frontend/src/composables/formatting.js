export default function useFormatting () {
  function formatSubscribers (value, multiple = 1000000) {
    const result = value / multiple
    if (result >= 1) {
      return `${Math.round(result * 10) / 10}K`
    } else {
      return `${value}`
    }
  }

  return {
    formatSubscribers
  }
}
