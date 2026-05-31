<template>
  <div class="page-mine">
    <!-- 标题栏优化：添加返回按钮和设置入口 -->
    <van-nav-bar
      title="个人中心"
      fixed
      left-arrow
      right-text="设置"
      @click-right="$router.push('/settings')"
    />

    <!-- 用户信息区域优化：重新布局头像和文字 -->
    <div class="user-header">
      <div class="avatar-container">
        <!-- 头像点击区域扩大，为后续上传功能做准备 -->
        <div class="avatar-wrapper" @click="handleAvatarClick">
          <img
            v-if="user.avatar"
            :src="user.avatar"
            class="avatar-image"
          >
          <img
            v-else
            src="/static/mine/avatar.png"
            class="avatar-image"
          >
          <!-- 添加相机图标提示可上传 -->
          <van-icon name="photograph" class="camera-icon" />
        </div>
        <div class="user-info">
          <!-- 用户名显示优化 -->
          <p class="welcome-text">欢迎您，{{ user.nickname || '亲爱的用户' }}</p>
          <!-- 退出登录按钮样式优化 -->
          <van-button
            size="mini"
            round
            class="logout-btn"
            @click="logout"
          >
            退出登录
          </van-button>
        </div>
      </div>
    </div>

    <!-- 订单菜单优化：使用van-grid组件增强视觉效果 -->
    <van-grid :column-num="4" class="order-grid">
      <van-grid-item
        v-for="item in orderItems"
        :key="item.text"
        :icon="item.icon"
        :text="item.text"
        @click="$router.push(item.path)"
      />
    </van-grid>

    <!-- 新增功能区域：我的信息模块 -->
    <van-cell-group class="function-group">
      <van-cell
        title="个人信息"
        is-link
        icon="user-o"
        @click="$router.push('/profile')"
      />
      <van-cell
        title="我的收藏"
        is-link
        icon="like-o"
        @click="$router.push('/favorites')"
      />
      <van-cell
        title="收货地址"
        is-link
        icon="location-o"
        @click="$router.push('/address')"
      />
    </van-cell-group>

    <!-- 新增系统功能模块 -->
    <van-cell-group class="function-group">
      <van-cell
        title="系统设置"
        is-link
        icon="setting-o"
        @click="$router.push('/settings')"
      />
      <van-cell
        title="帮助中心"
        is-link
        icon="question-o"
        @click="$router.push('/help')"
      />
    </van-cell-group>

    <van-action-sheet
      v-model="showUploader"
      :actions="uploadActions"
      @select="onActionSelect"
    />

    <!-- 底部导航栏 -->
    <TripFooter />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TripFooter from '@/components/common/Footer'
import { AccountsApis } from '@/utils/apis'
import { ajax } from '@/utils/ajax'
import * as types from '@/store/mutations-types'

export default {
  components: {
    TripFooter
  },
  data () {
    return {
      // 订单菜单数据化，便于维护
      orderItems: [
        { text: '全部订单', icon: 'records', path: '/orders' },
        { text: '待支付', icon: 'pending-payment', path: '/orders?status=unpaid' },
        { text: '已完成', icon: 'checked', path: '/orders?status=completed' },
        { text: '已取消', icon: 'close', path: '/orders?status=canceled' }
      ],
      showUploader: false, // 添加控制显示的状态
      uploadActions: [
        {
          name: '拍照',
          callback: () => this.takePhoto() // 使用箭头函数绑定this
        },
        {
          name: '从相册选择',
          callback: () => this.pickFromGallery()
        },
        {
          name: '取消',
          color: '#ee0a24'
        }
      ]
    }
  },
  methods: {
    getUserInfo () {
      ajax.get(AccountsApis.userInfoUrl).then(({ data }) => {
        this.$store.commit(types.UPDATE_USER_INFO, data)
      })
    },
    logout () {
      ajax.get(AccountsApis.logoutUrl).then(() => {
        this.$notify({
          message: '欢迎下次再来',
          type: 'success'
        })
        this.$store.commit(types.DELETE_USER_INFO)
        this.$router.push({ name: 'Home' })
      })
    },
    // 新增头像点击处理（为上传功能预留）
    handleAvatarClick () {
      this.showUploader = true
    },
    takePhoto (
    ) {
    // 实现拍照逻辑
      console.log('调用拍照功能'
      )
    // 实际项目中这里应该调用相机API
    },

    pickFromGallery (
    ) {
    // 实现相册选择逻辑
      console.log('调用相册选择'
      )
    // 实际项目中这里应该调用文件选择API
    },
    onActionSelect (action) {
    // 执行对应的回调函数
      if (action.callback) {
        action.callback()
      }
      // 关闭弹窗
      this.showUploader = false
    }
  },
  computed: mapState(['user']),
  mounted () {
    this.getUserInfo()
  }
}
</script>

<style lang="less">
.page-mine {
  padding-bottom: 50px; /* 给底部导航留出空间 */

  /* 导航栏优化 */
  .van-nav-bar {
    background-color: transparent;

    &__title {
      color: #fff;
      font-weight: bold;
    }

    .van-icon, &__text {
      color: #fff;
    }
  }

  /* 用户信息区域优化 */
  .user-header {
    padding-top: 46px; /* 适配导航栏高度 */
    background: url(/static/mine/bg.jpg) no-repeat center;
    background-size: cover; /* 修改为cover使背景图更完整 */
    color: #fff;
    height: 220px; /* 稍微增加高度 */
    display: flex;
    justify-content: center;
    align-items: center;

    .avatar-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;

      .avatar-wrapper {
        position: relative;
        margin-bottom: 15px;

        .avatar-image {
          width: 88px;
          height: 88px;
          border-radius: 50%;
          border: 3px solid rgba(255,255,255,0.8); /* 添加白色边框 */
          box-shadow: 0 2px 8px rgba(0,0,0,0.2); /* 添加阴影效果 */
          transition: all 0.3s;
          &:active {
            transform: acle(0.95);
          }
        }

        .camera-icon {
          position: absolute;
          right: 0;
          bottom: 0;
          background: #07c160;
          color: white;
          border-radius: 50%;
          padding: 4px;
          font-size: 16px;
        }
      }

      .user-info {
        text-align: center;

        .welcome-text {
          font-size: 16px;
          margin-bottom: 10px;
        }

        .logout-btn {
          background: rgba(255,255,255,0.2);
          color: white;
          border: none;
          padding: 0 15px;
        }
      }
    }
  }

  /* 订单网格优化 */
  .order-grid {
    // margin: 15px 0;
    background: white;
    // border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);

    .van-grid-item {
      padding: 15px 0;

      .van-icon {
        font-size: 24px;
        margin-bottom: 5px;
        color: #1989fa;
      }
    }
  }

  /* 功能区域优化 */
  .function-group {
    // margin: 15px;
    // border-radius: 8px;
    overflow: hidden;

    .van-cell {
      padding: 12px 16px;

      &__title {
        font-size: 14px;
        text-align: left;
      }

      .van-icon {
        font-size: 18px;
        margin-right: 8px;
        color: #1989fa;
      }
    }
  }
}
</style>
