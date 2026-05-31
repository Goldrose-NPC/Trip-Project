import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import * as filters from './utils/filters'
// VantUI组件库
import Vant from 'vant'
import 'vant/lib/index.css'

Vue.use(Vant)
Vue.config.productionTip = false

// 注册过滤器
Object.keys(filters).forEach(k => Vue.filter(k, filters[k]))

window.app = new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
