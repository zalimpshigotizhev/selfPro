import './assets/style/main.sass'
import 'element-plus/dist/index.css'
import 'floating-vue/dist/style.css'    

import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import FloatingVue from 'floating-vue'

const app = createApp(App)

app.use(FloatingVue)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)


app.mount('#app')
