export function useBlocks () {
    const app = getCurrentInstance()

    function handleDeleteBlock (index: number) {
        if (app) {
            app.emit('delete-block', index)
        }
    }

    return {
        handleDeleteBlock
    }
}
