import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

createApp(App).mount('#app')

// register service worker
navigator.serviceWorker.register('service-worker.js', { scope: "." });
