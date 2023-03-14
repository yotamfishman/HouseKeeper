<template>
    <VueSidebarMenuAkahon :isMenuOpen="true"
                           :isSearch="false"
                           :menuTitle="'House Keeper'"
                           :menuLogo="'/favicon.ico'"
                           :profileImg="'/src/assets/img/profile.jpg'"
                           :menuItems="[
                            {
                              link: '/',
                              name: 'My Chores',
                              tooltip: 'My Chores',
                              icon: 'bx-message-square-check'
                            },
                            {
                              link: '/add',
                              name: 'Add Chores',
                              tooltip: 'Add Chores',
                              icon: 'bx-plus-circle'
                            },
                            {
                              link: '/',
                              name: 'Ratings',
                              tooltip: 'Ratings',
                              icon: 'bx-trending-up'
                            },
                            {
                              link: '/',
                              name: 'Overview',
                              tooltip: 'Overview',
                              icon: 'bx-grid-alt'
                            }
                           ]"
                            />
  </template>
  
  
  <script lang="ts">
  import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
  
  export default {
    name: "SideBar.vue",
    components: { VueSidebarMenuAkahon },
    data() {
      return {};
    },
  };
  </script>

<style>
</style>