import { createApp } from 'vue'
import { requestClipboardWritePermission } from 'copy-image-clipboard'
import './style.css'
import App from './App.vue'
import router from './router'

createApp(App)
  .use(router)
  .mount('#app')

// register service worker
navigator.serviceWorker.register('service-worker.js', { scope: "." });

// request permissions
requestClipboardWritePermission();
