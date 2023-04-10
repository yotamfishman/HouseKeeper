import  { createApp } from "vue";
import Login from "@/views/login.vue";

import BootstrapVueNext from 'bootstrap-vue-next'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';
import "@/assets/main.css";

const app = createApp(Login);

app.use(BootstrapVueNext)

app.mount("#app");
