Vue.use(Vuex)

var messages = {
    state: () => ({
        messages: [
            { id: 1, type: 'success', content: 'this is a message', visible: true },
            { id: 2, type: 'success', content: 'this is a message', visible: true }
        ]
    }),

    mutations: {
        addMessage(state, payload) {
            state.messages.push(payload)
        }
    },
    
    actions: {
        addSuccessMessage({ commit }, message) {
            message['type'] = 'success'
            commit('addMessage', message)
        }
    }
}

var authentication = {
    namespaced: true,
    state: () => ({
        authenticated: false
    }),
    mutations: {
        updateuser(state, payload) {
            state.authenticated = payload.authenticated
        }
    },
    actions: {
        setuser({ commit }, payload) {
            commit("updateuser", payload)
        }
    }
}

var store = new Vuex.Store({
    state: () => ({
        currentVideo: {
            reference: null,
            isRated: false
        }
    }),
    modules: {
        authentication,
        messages
    },

    mutations: {
        setCurrentVideo(state, attrs) {
            state.currentVideo.reference = attrs
        },
        setRated(state, payload) {
            state.isRated = payload
        }
    },

    actions: {
        updateCurrentVideo({ commit }, attrs) {
            commit('setCurrentVideo', attrs)
        }
    }
})
