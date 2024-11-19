import { createVuetify } from "vuetify";

import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { aliases, mdi } from "vuetify/iconsets/mdi";
import colors from "vuetify/util/colors";

import DayJsAdapter from "@date-io/dayjs";

import 'vuetify/styles';
import '@mdi/font/css/materialdesignicons.css';

import '@testing-library/jest-dom';

export function setupVuetify() {
    return createVuetify({
        components,
        directives,
        date: {
            adapter: DayJsAdapter,
        },
        theme: {
            themes: {
                light: {
                    dark: false,
                    colors: {
                        primary: colors.red.darken1,
                    },
                },
            },
        },
        icons: {
            defaultSet: "mdi",
            aliases,
            sets: {
                mdi,
            },
        },
    });
}
