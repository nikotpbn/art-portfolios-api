<template>
    <router-view></router-view>
</template>

<script>
  import NavbarComponent from '@/components/Navbar.vue'
  import HomeView from './views/HomeView.vue';
  export default {
    name: "App",
    components: {
    NavbarComponent,
    HomeView
},
  }
</script>

<style>
nav {
  padding: 30px
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>