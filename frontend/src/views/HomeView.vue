<template>
  <Navbar/>
    <div class="images-wrapper mt-5">
        <div v-for="art in arts" :key="art.id" class="card text-white bg-dark mb-3" style="width: 20rem;">
            <img v-bind:src="art.image" class="gallery-card-image card-img-top" alt="..." />
            <div class="card-body">
                <p class="card-text">Title: {{ art.title }}</p>
                <p class="card-text">Subtitle: {{ art.subtitle }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import axios from 'axios'

export default {
  name: "HomeView",
  components: {Navbar},
  data () {
    return {
      arts: null,
    }
  },
  methods: {
    getArts() {
    axios.get('http://192.168.1.244:8000/api/arts/', { headers: {} })
    .then((response) => {
        let fff = response.data;
        fff.sort(function(a, b){
            return a.created_at.localeCompare(b.create_at);
        });
      this.arts = response.data;
    })
    .catch((error) => {
      console.log(error);
      console.log('badbad')
    });
    }

  },
  created() {
    this.getArts();
  }
}
</script>