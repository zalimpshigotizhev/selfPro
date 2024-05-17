import { createRouter, createWebHistory } from 'vue-router'
import { ROUTES_PATHS } from '../constans/router'
import Intensive from '../pages/Intensive.vue'
import Auth from '../pages/Auth.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: ROUTES_PATHS.HOME,
      name: ROUTES_PATHS.HOME,
      component: Intensive
    },
    {
      path: ROUTES_PATHS.AUTH,
      name: ROUTES_PATHS.AUTH,
      component: Auth
    },
  ]
})

export default router
