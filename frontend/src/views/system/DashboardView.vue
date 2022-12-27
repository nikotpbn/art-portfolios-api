<template>
    <div v-if="isAuthenticated">
        dashboard
    </div>
    <div v-else>
        Redirect
    </div>
</template>

<script>
import axios from 'axios'
import router from "@/router";

export default {
    name: "SystemDashboard",
    data() {
        return {
            isAuthenticated: false,
        }
    },
    mounted() {
        const token = localStorage.getItem('token');
        axios.get('http://192.168.1.244:8000/api/user/me/', {
            headers: {
                'Authorization': `Token ${token}`
            }
        }
        ).then((response) => {
            console.log(response.data)

        }).catch((error) => {
            console.log(error);
        });
    },
    beforeMount() {
        const token = localStorage.getItem('token');
        if (token === null) {
            console.log('null')
            router.push("/system");
        }
        axios.get('http://192.168.1.244:8000/api/user/me/', {
            headers: {
                'Authorization': `Token ${token}`
            }
        }
        ).then((response) => {
            console.log(response.data)

        }).catch((error) => {
            console.log(error);
        });
    }
}
</script>