import { createRouter, createWebHistory } from 'vue-router';
import StickerPackList from './components/StickerPackList.vue';
import StickerList from './components/StickerList.vue';

const routes = [
  {
    path: '/', name: 'StickerPackList', component: StickerPackList
  },
  {
    path: '/sticker', name: 'StickerList', component: StickerList
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;