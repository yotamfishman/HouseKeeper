import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "My Chores",
      component: () => import("../views/main.vue"),
    },
    {
      path: "/add",
      name: "Add Chores",
      component: () => import("../views/add.vue"),
    },
  ],
});

export default router;
