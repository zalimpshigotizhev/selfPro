import { createRouter, createWebHistory } from 'vue-router'
import { ROUTES_PATHS } from '../constans/router'
import Intensive from '../pages/Intensive.vue'
import IntensiveAdd from '../pages/IntensiveAdd.vue'
import History from '../pages/History.vue'
import Profile from '../pages/Profile.vue'
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
    {
      path: ROUTES_PATHS.PROFILE,
      name: ROUTES_PATHS.PROFILE,
      component: Profile
    },
    {
      path: ROUTES_PATHS.INTENSIVE_ADD,
      name: ROUTES_PATHS.INTENSIVE_ADD,
      component: IntensiveAdd,
    },
    {
      path: ROUTES_PATHS.HISTORY,
      name: ROUTES_PATHS.HISTORY,
      component: History,
    }
  ]
})

export default router
