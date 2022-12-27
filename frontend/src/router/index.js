import {createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        component: () => import('../views/AboutView.vue')
    },
    {
        path: '/system',
        name: 'system',
        component: () => import('../views/system/SystemLoginView.vue')
    },
    {
        path: '/system/dashboard',
        name: 'dashboard',
        component: () => import('../views/system/DashboardView.vue')
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'not-found',
        component: () => import('../views/NotFoundView.vue')
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router