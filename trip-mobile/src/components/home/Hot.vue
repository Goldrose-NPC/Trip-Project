<template>
    <!-- <热点导航> -->
    <div class="home-hot-box">
      <!-- <顶上导航> -->
     <van-cell title="热门推荐"
     icon="/static/home/hot/fire.png"
     is-link
     title-style="text-align:left"
     value="全部榜单"
     :to="{name: 'Search', query: {isHot: 1}}"/>
     <!-- //<顶上导航> -->
     <!-- <景点列表> -->
      <div class="box-main">
        <router-link class="hot-item"
        :to="{name: 'SightDetail', params:{id: item.id}}"
        v-for="item in dataList"
        :key="item.id">
            <div class="img">
                <span></span>
                <img :src="item.main_img" alt="">
            </div>
            <h5 class="van-ellipsis">{{ item.name }}</h5>
            <div class="line-price">
                <span class="price">¥{{ item.min_price }}</span>起
            </div>
        </router-link>
      </div>
     <!-- //<景点列表> -->
    </div>
</template>
<script>
import { ajax } from '@/utils/ajax'
import { SightApis } from '@/utils/apis'
export default {
  data () {
    return {
      dataList: []
    }
  },
  methods: {
    /**
     * 查询热门景点的数据
     */
    getDataList () {
      ajax.get(SightApis.sightListUrl, {
        params: {
          is_hot: 1
        }
      }).then(({data}) => {
        this.dataList = data.objects
      })
    }
  },
  created () {
    // 获取接口数据
    this.getDataList()
  }
}
</script>
<style lang="less">
.home-hot-box{
    padding: 0 10px;
    .van-cell{   //重写van-cell
        padding: 10px 0;
    }
    .box-main{
        width:100%;
        display: flex;
        padding-top: 10px;
        overflow-x: scroll;  //滚动条
    }
    .hot-item{
        display: flex;
        flex-direction: column;
        width: 100px;
        margin-right: 10px;
        padding-bottom: 10px;

        .img{
            position: relative;

            span {
                position: absolute;
                left: 0;
                top: 0;
                display: inline-block; //显示
                width: 42px;
                height: 20px;
                z-index: 10;
            }

            img{
                width: 100px;
                height: 100px;
            }
        }

        h5{
            color: #212121;
            padding: 2px 0; //上下 左右
            font-size: 12px;
            margin: 0;
        }
        .line-price{
            color: #212121; //起字的颜色
            font-size: 12px;

            .price{
                color: #f50;
                font-size: 13px;
            }
        }
        &:nth-child(1) .img span {
            background: url(/static/home/hot/top1.png) no-repeat;
            background-size: 100% auto; //高度 宽度
        }
        &:nth-child(2) .img span {
            background: url(/static/home/hot/top2.png) no-repeat;
            background-size: 100% auto; //高度 宽度
        }
        &:nth-child(3) .img span {
            background: url(/static/home/hot/top3.png) no-repeat;
            background-size: 100% auto; //高度 宽度
        }
    }
}

</style>
