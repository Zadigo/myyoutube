import { createVueLocalStorage, createVueSession } from '@/plugins/vue-storages';
import { render } from '@testing-library/vue';
import { Component } from 'vue';
import { setupVuetify } from "./setupVuetify";

export function renderWithVuetify(component: Component, options = {}) {
    const vuetify = setupVuetify()
    const session = createVueSession()
    const localstorage = createVueLocalStorage()

    return render(component, {
        global: {
            plugins: [
                vuetify,
                session,
                localstorage
            ],
        },
        ...options,
    });
}
