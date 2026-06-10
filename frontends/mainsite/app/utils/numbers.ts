export function useNumbersUtils() {
  function shorten(num: number): string {
    // Handle negative numbers
    const isNegative = num < 0;
    num = Math.abs(num);

    // Define thresholds and suffixes
    const thresholds = [
      { value: 1e9, suffix: 'B' },  // Billion
      { value: 1e6, suffix: 'M' },  // Million
      { value: 1e3, suffix: 'K' }   // Thousand
    ];

    // Find appropriate threshold
    for (let i = 0; i < thresholds.length; i++) {
      const threadshold = thresholds[i]

      if (isDefined(threadshold)) {
        if (num >= threadshold.value) {
          const shortened = num / threadshold.value;
          // Format with up to 1 decimal place, removing trailing zeros
          const formatted = Math.round(shortened * 10) / 10;
          return (isNegative ? '-' : '') + formatted + threadshold.suffix;
        }
      } else {
        return ''
      }
    }

    // Return original number if less than 1000
    return (isNegative ? '-' : '') + num.toString();
  }

  return {
    shorten
  }
}
