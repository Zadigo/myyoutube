import { Axios } from "axios";

declare module '@vue/runtime-core' {
    interface ComponentCustomProperties {
        $client: Axios
        $authClient: Axios
    }
}
