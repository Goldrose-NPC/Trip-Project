<template>
  <div class="page-home">
    <!-- <h1>三国旅游网</h1> -->
    <!-- <Banner图> -->
    <Banner />
    <!-- <热门推荐> -->
    <Hot />
    <!-- 精选景点 -->
    <Fine />
    <!-- 底部导航栏 -->
    <TripFooter />
  </div>
</template>

<script>
// @ is an alias to /src
// import axios from 'axios'
// import Vue from 'vue'
// import { Button } from 'vant';
// @代表src目录
import Banner from '@/components/home/Banner'
import Hot from '@/components/home/Hot'
import Fine from '@/components/home/Fine'
import TripFooter from '@/components/common/Footer'

export default {
  name: 'Home',
  components: {
    // Banner图
    Banner,
    // 热门推荐
    Hot,
    // 精选景点
    Fine,
    // 底部导航栏
    TripFooter
  },
  created () {
  }
}
</script>
<style lang="less" scoped>
.page-home {
  width: 100%;
}
</style>
