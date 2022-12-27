<template>
    <div class="container" style="height: 80vh; display: flex; justify-content: center; align-items: center;">
        <form @submit.prevent="submit">
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="email">
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
            </div>
            <div style="text-align: center;">
                <button type="submit" class="btn btn-primary">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>

import axios from 'axios'
import router from "@/router";

export default {
    name: "SystemLoginView",
    data() {
        return {
            email: '',
            password: '',
        }
    },
    methods: {
        submit() {
            axios.post(
                'http://192.168.1.244:8000/api/user/login/',
                `username=${this.email}&password=${this.password}`,
            ).then((response) => {
                localStorage.setItem( 'token', response.data.token );
                localStorage.setItem( 'username', response.data.user_name );
                localStorage.setItem( 'email', response.data.email );
                router.push("/system/dashboard");

            })
            .catch((error) => {
                let msg = ''
                if (error.response) {
                    // The request was made and the server responded with a status code
                    // that falls out of the range of 2xx
                    if (error.response.status === 400) {
                        msg = 'wrong credentials.'
                        console.log(msg)
                    }
                }
            });
        }

    },
    setup() {
        const token = localStorage.getItem('token');
        if (token != null) {
            axios.get('http://192.168.1.244:8000/api/user/me/', {
            headers: {
                'Authorization': `Token ${token}`
            }
            }
            ).then((response) => {
                if (response.data.isAuthenticated === true) {
                    router.push("/system/dashboard");
                }

            }).catch((error) => {
                console.log(error)
        });
        }
    }
}
</script>