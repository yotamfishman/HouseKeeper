<template>
    <b-container class="m-3">
        <b-row class="justify-content-md-center">
                <ChoreCard
                v-for="chore in chores"
                :title="chore.title"
                :description="chore.description"
                :icon="chore.icon"
                :duration="chore.duration"
             />
        </b-row>
    </b-container>
</template>

<script lang="ts">
import ChoreCard from "../components/ChoreCard.vue";
import axios from "axios"

interface CardData {
  title: string, 
  description: string, 
  icon: string, 
  duration: string,
  _id: number,
}

interface Data {
  chores: CardData[]
}
  
  export default {
    name: "main.vue",
    components: { ChoreCard },
    data() : Data {
      return {
        chores: []
      };
    },
    mounted () {
      axios.get("http://127.0.0.1:5000/my-chores.json").then(response => (this.chores = response.data))
    }
  };
</script>

<style>
</style>