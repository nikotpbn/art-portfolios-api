<template>
    <Navbar/>
    <AboutContainer/>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import AboutContainer from '@/components/About.vue'

 export default {
    name: 'About',
    components: { Navbar, AboutContainer}
 }
</script>