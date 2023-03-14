import { createRouter, createWebHistory } from "vue-router";
import main from "../views/main.vue"
import add from "../views/add.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "My Chores",
      component: main,
    },
    {
      path: "/add",
      name: "Add Chores",
      component: () => add,
    },
  ],
});

export default router;
