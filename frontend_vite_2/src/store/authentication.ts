import { defineStore } from "pinia";
import { LoginResponse } from "../types/authentication";

interface RootState {
    accessToken: string | null
    refreshToken: string | null
}

const useAuthentication = defineStore('authentication', {
    state: (): RootState => ({
        accessToken: null,
        refreshToken: null
    }),
    actions: {
        /**
         * 
         */
        loadFromCache() {
            const authentication = this.$session.retrieve<LoginResponse>('authentication')
            if (authentication) {
                this.accessToken = authentication.access
                this.refreshToken = authentication.refresh
            }
        }
    },
    getters: {
        /**
         * 
         */
        isAuthenticated (): boolean {
            return this.accessToken !== null
        }
    }
})

export {
    useAuthentication
}
