import { createRouter, createWebHistory } from 'vue-router'
import EditorView from "@/views/EditorView.vue";
import ChatView from "@/views/ChatView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/editor',
      name: 'editor',
      component: EditorView
    },
    {
      path: '/chat',
      name: 'chat',
      component: ChatView
    }
  ]
})

export default router
