<template>
    <b-container class="m-3">
        <b-row class="justify-content-md-center">
                <ChoreCard
                v-for="chore in chores"
                :title="chore.title"
                :description="chore.description"
                :icon="chore.icon"
                :duretion="chore.duretion"
             />
        </b-row>
    </b-container>
</template>

<script lang="ts">
import ChoreCard from "../components/ChoreCard.vue";
  
  export default {
    name: "main.vue",
    components: { ChoreCard },
    data() {
      return {
        chores: [
            {
            title: "Take out the trash",
            description: "Take the trash out from the can",
            icon: "/icons/trash.svg",
            duretion: "4 minutes",
            },
            {
                title: "Wash the dishes",
                description: "wash all the dishes in th sinks",
                icon: "/icons/sink.svg",
                duretion: "30 minutes",
            },
            {
                title: "Water the plants",
                description: "Make sure to water to water the plants in the living roo as well",
                icon: "/icons/leaf.svg",
                duretion: "10 minutes"
            },
            
    ]
      };
    },
  };
</script>

<style>
</style>