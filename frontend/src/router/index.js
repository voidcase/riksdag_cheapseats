import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Topic from '@/components/Topic'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/doc/:id',
      name: 'Topic',
      component: Topic
    }
  ]
})
