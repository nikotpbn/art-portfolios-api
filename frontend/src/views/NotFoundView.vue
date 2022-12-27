<template>
    <Navbar />
    <div class="not-found-container">
        <font-awesome-icon icon="fa-solid fa-face-sad-cry" />
        <h1>404 Page Not Found.</h1>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
    name: 'not-found',
    components: {
        Navbar,
    }
}
</script>