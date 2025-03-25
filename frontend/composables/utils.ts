import { isRef } from 'vue'

type ArrayAnyValues = (string | number)[]

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

    return {
        isNull,
        scrollToTop,
        hasNull,
        readFile,
        readFiles
    }
}
