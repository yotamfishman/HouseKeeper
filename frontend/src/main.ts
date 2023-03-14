import  { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import BootstrapVueNext from 'bootstrap-vue-next'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';
import "./assets/main.css";

const app = createApp(App);

app.component('vue-sidebar-menu-akahon', VueSidebarMenuAkahon);

app.use(router);
app.use(BootstrapVueNext)

app.mount("#app");
