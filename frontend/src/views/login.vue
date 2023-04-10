<template>
    <div class="login-container">
      <b-form @submit="onSubmit" class="login-form">
        <b-form-group id="username-group" label="Username:" label-for="username">
          <b-form-input id="username" v-model="form.name" required></b-form-input>
        </b-form-group>
  
        <b-form-group id="password-group" label="Password:" label-for="password">
          <b-form-input id="password" v-model="form.passwd" type="password" required></b-form-input>
        </b-form-group>
  
        <b-button type="submit" variant="primary">Login</b-button>
      </b-form>
    </div>
  </template>
    
<script lang="ts">
    import axios from "axios"

    export default {
        name: "Login.vue",
        data() {
            return {
                form: {
                    name: '',
                    passwd: ''
                },
                show: true
            }
        },
        methods: {
            onSubmit(event: any) {
                event.preventDefault()
                axios.post('/login', {
                    name: this.form.name,
                    passwd: this.form.passwd
                }).then(response => {
                    window.location.href = '/'; // Redirect the client to the new URL
                }).catch(error => {
                    console.log(error)
                })
            }
        }
    }
</script>
    
<style>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-form {
  width: 400px;
  background-color: #fff;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>