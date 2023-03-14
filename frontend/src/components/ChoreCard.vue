<template>
 <b-card
    no-body
    class="text-center chore-card m-3"
    style="max-width: 15rem;"
  >
  <b-card-body>
        <b-card-img
        :src="icon"
        alt="Image"
        class="p-3"
        ></b-card-img>
        <b-card-title>{{title}}</b-card-title>
        <b-card-text>{{description}}</b-card-text>
        <b-card-text>{{duretion}}</b-card-text>
    </b-card-body>
  </b-card>
</template>

<script lang="ts">  
  export default {
    props: {
        title: {
            type: String,
            required: true,
        },
        description: {
            type: String,
            required: true,
        },
        icon: {
            type: String,
            required: true,
        },
        duretion: {
            type: String,
            required: true,
        }
    },
    name: "ChoreCard.vue",
    data() {
      return {};
    },
  };
</script>

<style>
.chore-card {
    color: black;
    padding: 1rem;
    border: 1px solid #888888 !important;
    box-shadow: 0px 0px 5px #888888;
}
</style>