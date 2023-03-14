<script setup lang="ts">
import SideBar from "./components/SideBar.vue"
name:"App.vue"
components: {
  SideBar
  }

</script>

<template>
    <SideBar/>
    <router-view/>
  <div>
  </div>
</template>

<style>

</style>
