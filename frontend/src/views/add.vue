<template>
    <div class="add-form-container">
      <b-form @submit.prevent="submitForm">
        <b-form-group id="title-input-group" label="Title" label-for="title-input">
          <b-form-input id="title-input" v-model="title" required></b-form-input>
        </b-form-group>
        <b-form-group id="description-input-group" label="Description" label-for="description-input">
          <b-form-textarea id="description-input" v-model="description" rows="5" required></b-form-textarea>
        </b-form-group>
        <b-form-group id="icon-input-group" label="Icon" label-for="icon-input">
          <b-form-select v-model="selectedIcon" :options="iconOptions"></b-form-select>
          <div class="selected-icon"><i :class="selectedIcon"></i></div>
        </b-form-group>
        <b-form-group id="duration-input-group" label="Duration" label-for="duration-input">
          <div class="duration-input-container">
            <b-form-input id="duration-input" v-model="duration" type="text" pattern="[0-9]+(m|h)" required></b-form-input>
          </div>
        </b-form-group>
        <div class="form-buttons">
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </div>
      </b-form>
    </div>
</template>
  
<script lang="ts">
  import axios from "axios"

  export default {
    name: "add.vue",
    data() {
      return {
        title: '',
        description: '',
        selectedIcon: '/icons/trash',
        duration: ''
      }
    },
    computed: {
      iconOptions() {
        return [
          { value: '/icons/trash.svg', text: 'Trash' },
          { value: '/icons/leaf.svg', text: 'Plants' },
          { value: '/icons/sink.svg', text: 'Sink' }
        ]
      }
    },
    methods: {
      submitForm() {
        const taskData = {
          title: this.title,
          description: this.description,
          icon: this.selectedIcon,
          duration: this.duration.replace('m', ' minutes').replace('h', ' hours')
        }
        console.log(taskData)
        axios.post('add', taskData).then(response => {
            alert("The chore was added successfully")
            window.location.href = '/'; // Redirect the client to the new URL)
      }).catch(error => { console.log(error.response.data) });
    }
  }
}
</script>
  
<style>
  body {
    background-color: #333333;
  }
  .add-form-container {
    display: block;
    margin: 0 auto;
    width: 80%;
    justify-content: center;
    align-items: center;
    padding-top: 30px;
    height: 100vh;
  }
  .add-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 2rem;
    background-color: #f9f9f9;
    border-radius: 0.5rem;
  }
  .add-form-title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 2rem;
    color: #333333;
    text-align: center;
  }
  .add-form-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    color: #333333;
  }
  .add-form-duration {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
  }
  .add-form-duration label {
    color: #333333;
    margin-right: 1rem;
  }
  .add-form-duration select {
    width: 60%;
  }
  .add-form-button {
    margin-top: 2rem;
    width: 100%;
  }
  .form-label{
    color: #f0f0f0;
  }
  input[type="text"], textarea {
    width: 100%;
    padding: 0.5rem;
    border-radius: 0.5rem;
    border: none;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    color: #333333;
    background-color: #f0f0f0;
  }
  input[type="text"]::placeholder, textarea::placeholder {
    color: #666666;
  }
</style>