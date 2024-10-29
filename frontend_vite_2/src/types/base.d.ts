import DayjsUtils from "@date-io/dayjs";
import { Axios } from "axios";

declare module '@vue/runtime-core' {
    interface ComponentCustomProperties {
        $client: Axios
        $authClient: Axios
        $quartClient: Axios
        $date: DayjsUtils
    }
}
