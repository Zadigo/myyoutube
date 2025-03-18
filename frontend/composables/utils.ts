import { isRef, ref } from 'vue'

type ArrayAnyValues = (string | number)[]
type RefArrayAnyValues = ArrayAnyValues | Ref<(string | number)[]>
// type RefObjectAnyValues = Ref<Record<string, (string | number)[] | string | number>>

export function useUtilities () {
    function scrollToTop () {
        window.scroll({ top: 0, behavior: 'smooth' })
    }

    // TODO: Remove. Use as simple function
    function isNull<T>(item: T): boolean {
        let trueValue

        if (isRef(item)) {
            trueValue = item.value
        } else {
            trueValue = item
        }

        return (
            trueValue === null ||
            typeof trueValue  === 'undefined' ||
            trueValue === '' ||
            trueValue === ' '
        )
    }

    function hasNull<T extends ArrayAnyValues>(items: T): boolean {
        return items.some(v => {
            return v === null || v === '' || typeof v === 'undefined'
        })
    }

    function readFile (e: Event): string | undefined {
        let preview
        const input = e.target as HTMLInputElement

        if (input.files) {
            const file = input.files[0]
            const reader = new FileReader

            reader.onload = e => {
                preview = e.target?.result
            }

            reader.readAsDataURL(file)
        }

        return preview
    }

    function readFiles (e: Event): (string | ArrayBuffer | null | undefined)[] {
        const input = e.target as HTMLInputElement
        
        if (input.files) {
            let preview: string | ArrayBuffer | undefined | null
            const reader = new FileReader

            reader.onload = e => {
                preview = e.target?.result
            }

            return Object.values(input.files).map(f => {
                if (f) {
                    reader.readAsDataURL(f)
                }
                return preview
            }) 
        }
        
        return []
    }

    // function debounce<F extends (...args[]: any[]) => void>(fn: F, delay: number): (...args: Parameters<F>) => void {
    //     let timer: ReturnType<typeof setTimeout>

    //     return function (...args: Parameters<F>) {
    //         clearTimeout(timer)
    //         timer = setTimeout(() => fn(...args), delay)
    //     };
    // }

    return {
        isNull,
        scrollToTop,
        // debounce,
        hasNull,
        readFile,
        readFiles
    }
}

export function useListManager () {
    const managedObject = ref<Record<string, (string | number)[] | string | number | null>>()
    const managedList = ref<RefArrayAnyValues>([])
    const history = ref<ArrayAnyValues>([])
    const deletions = ref<ArrayAnyValues>([])

    function updateList<T extends RefArrayAnyValues>(items: T, value: string | number) {
        if (Array.isArray(items)) {
            if (items.includes(value)) {
                const index = items.indexOf(value)
                items.splice(index, 1)
            } else {
                items.push(value)
            }
        } else {
            if (items.value.includes(value)) {
                const index = items.value.indexOf(value)
                items.value.splice(index, 1)
            } else {
                items.value.push(value)
            }
        }
    }

    function update(key: string, value: string | number): boolean {
        if (managedObject.value) {
            if (Array.isArray(managedObject.value[key])) {
                if (managedObject.value[key].includes(value)) {
                    const index = managedObject.value[key].indexOf(value)
                    managedObject.value[key].splice(index, 1)
                } else {
                    managedObject.value[key].push(value)
                }
                return true
            }
        }
        return false
    }

    function save<T extends RefArrayAnyValues>(items: T, item: string | number) {
        if (managedList.value.length === 0) {
            if (isRef(items)) {
                managedList.value = [...items.value]
            } else {
                managedList.value = [...items]
            }
        }

        if (managedList.value.includes(item)) {
            const index = managedList.value.indexOf(item)
            const result = managedList.value.splice(index, 1)
            deletions.value = [...result]
            return false
        } else {
            managedList.value.push(item)
            history.value.push(item)
            return true
        }
    }

    return {
        deletions,
        managedObject,
        managedList,
        history,
        updateList,
        update,
        save
    }
}
