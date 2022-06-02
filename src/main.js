import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import ArgonDashboard from "./plugins/argon-dashboard";
import "element-plus/lib/theme-chalk/index.css";
import Toaster from "@meforma/vue-toaster";
// import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

const appInstance = createApp(App);
appInstance.use(router);
appInstance.use(ArgonDashboard);
appInstance.use(Toaster)
// appInstance.use(VueMaterial)
appInstance.mount("#app");

// https://www.creative-tim.com/vuematerial/components/table