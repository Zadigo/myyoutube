/**
 * Transforms an array of items into a format suitable for use as menu items.
 * Each item in the array is transformed into an object with a specified field name. 
 * @param items The array of items to transform into menu items
 * @param field The field name to use for the menu items, defaults to 'name'
 */
export function useMenuItems<T extends string, F extends string = 'name'>(items: T [], field: F = 'name' as F) {
  const transformedItems = items.map(item => ({ [field]: item } as { [K in F]: T }))
  const menuItems = toRef<{ [K in F]: T }[]>(transformedItems)

  return {
    menuItems
  }
}
