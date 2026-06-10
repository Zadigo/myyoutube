import { twMerge } from 'tailwind-merge'
import { mergeProps } from 'vue'

export const ptViewMerge = (globalPTProps = {} as unknown, selfPTProps = {} as unknown, datasets: unknown) => {
    const { class: globalClass, ...globalRest } = globalPTProps
    const { class: selfClass, ...selfRest } = selfPTProps

    return mergeProps({ class: twMerge(globalClass, selfClass) }, globalRest, selfRest, datasets)
}
