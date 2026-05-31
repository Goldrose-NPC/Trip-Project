import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Search from '../views/Search.vue'
import Mine from '../views/Mine.vue'
import SightList from '../views/sight/SightList.vue'
import SightDetail from '../views/sight/SightDetail.vue'
import SightInfo from '../views/sight/SightInfo.vue'
import SightComment from '../views/sight/SightComment.vue'
import SightImage from '../views/sight/SightImage.vue'
import AccountLogin from '../views/accounts/Login.vue'
import AccountRegister from '../views/accounts/Register.vue'
import Profile from '../views/accounts/Profile.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/mine',
    name: 'Mine',
    component: Mine
  },
  // 景点详情
  {
    path: '/sight/list',
    name: 'SightList',
    component: SightList
  },
  // 景点详情
  {
    path: '/sight/detail/:id',
    name: 'SightDetail',
    component: SightDetail
  },
  // 景点介绍
  {
    path: '/sight/info/:id',
    name: 'SightInfo',
    component: SightInfo
  },
  // 景点评论
  {
    path: '/sight/comment/:id',
    name: 'SightComment',
    component: SightComment
  },
  // 景点下的图片
  {
    path: '/sight/image/:id',
    name: 'SightImage',
    component: SightImage
  },
  // 用户登录
  {
    path: '/accounts/Login/',
    name: 'AccountLogin',
    component: AccountLogin
  },
  // 用户注册
  {
    path: '/accounts/register/',
    name: 'AccountRegister',
    component: AccountRegister
  },
  // 用户个人信息
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  }
]

const router = new VueRouter({
  routes
})

export default router
