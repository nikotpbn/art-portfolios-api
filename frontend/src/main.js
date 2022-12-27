import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

import './assets/main.css'
import './assets/gallery.css'
import './assets/navbar.css'

createApp(App).use(router, axios).mount('#app')
