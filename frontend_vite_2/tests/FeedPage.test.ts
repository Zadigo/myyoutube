import { client } from "@/plugins/axios";
import { screen, waitFor } from "@testing-library/vue";
import { afterEach, beforeEach, describe, it } from "node:test";
import { createPinia, setActivePinia } from 'pinia';
import { expect, vi } from "vitest";
import { renderWithVuetify } from "./renderVuetify";

import FeedPage from '@/pages/FeedPage.vue';
import MockAdapter from 'axios-mock-adapter';

const mock = new MockAdapter(client);

describe('FeedPage', () => {
    beforeEach(() => {
        setActivePinia(createPinia())
    })

    afterEach(() => {
        mock.reset()
        vi.clearAllMocks()
    })

    it('can render', async () => {
        mock.onGet('/video/').reply(200, {
            data: [],
        });

        renderWithVuetify(FeedPage)
        
        await waitFor(() => {
            expect(screen.getByText('Filters')).toBeInTheDocument()
        })

        expect('a').toEqual('a')
    })
})
