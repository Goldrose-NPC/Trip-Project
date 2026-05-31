<template>
  <div class="profile-page">
    <!-- 导航栏 -->
    <van-nav-bar
      title="个人信息"
      left-arrow
      @click-left="$router.go(-1)"
    />

    <!-- 用户头像 -->
    <div class="avatar-section">
      <van-image
        round
        width="80px"
        height="80px"
        :src="userInfo.user.avatar || '/static/mine/avatar.png'"
        @click="showAvatarActions"
      />
      <van-icon name="photograph" class="camera-icon" />
    </div>

    <!-- 基本信息 -->
    <van-cell-group>
      <van-cell title="昵称" :value="userInfo.user.nickname" is-link @click="editField('nickname')" />
      <!-- <van-cell title="手机号" :value="userInfo.user.username" /> -->
      <van-cell title="手机号" :value="userInfo.user.username || '未绑定'" is-link @click="editField('phone_num')"/>
      <van-cell title="真实姓名" :value="userInfo.profile.real_name || '未设置'" is-link @click="editField('real_name')" />
      <van-cell title="性别" :value="userInfo.profile.sex_display || '未设置'" is-link @click="showGenderPicker" />
      <van-cell title="邮箱" :value="userInfo.profile.email || '未设置'" is-link @click="editField('email')" />
    </van-cell-group>

    <!-- 详细信息 -->
    <!-- <van-cell-group title="详细信息">
      <van-cell title="真实姓名" :value="userInfo.profile.real_name || '未设置'" is-link @click="editField('real_name')" />
      <van-cell title="性别" :value="userInfo.profile.sex_display || '未设置'" is-link @click="showGenderPicker" />
      <van-cell title="邮箱" :value="userInfo.profile.email || '未设置'" is-link @click="editField('email')" />
    </van-cell-group> -->

    <!-- 头像操作面板 -->
    <van-action-sheet
      v-model="showUploader"
      :actions="uploadActions"
      @select="onActionSelect"
    />

    <!-- 性别选择器 -->
    <van-popup v-model="showGenderPopup" position="bottom">
      <van-picker
        :columns="genderOptions"
        show-toolbar
        @cancel="showGenderPopup = false"
        @confirm="onGenderConfirm"
      />
    </van-popup>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { AccountsApis } from '@/utils/apis'
import { ajax } from '@/utils/ajax'
import * as types from '@/store/mutations-types'

export default {
  data () {
    return {
      userInfo: {
        user: {
          avatar: '',
          nickname: '',
          username: ''
        },
        profile: {
          real_name: '',
          sex: 1,
          sex_display: '男',
          email: ''
        }
      },
      showUploader: false,
      showGenderPopup: false,
      uploadActions: [
        { name: '拍照', method: this.takePhoto },
        { name: '从相册选择', method: this.pickFromGallery },
        { name: '取消', color: '#ee0a24' }
      ],
      genderOptions: [
        { text: '男', value: 1 },
        { text: '女', value: 0 }
      ]
    }
  },
  computed: {
    ...mapState(['user'])
  },
  methods: {
    // 获取用户信息
    async fetchUserInfo () {
      try {
        const { data } = await ajax.get(AccountsApis.userInfoUrl)
        this.userInfo = {
          user: {
            ...data.user,
            avatar: data.user.avatar || this.user.avatar
          },
          profile: data.profile
        }
        // 更新store中的用户信息
        this.$store.commit(types.UPDATE_USER_INFO, data.user)
      } catch (error) {
        console.error('获取用户信息失败:', error)
        this.$notify({ type: 'danger', message: '获取信息失败' })
      }
    },

    // 显示头像操作面板
    showAvatarActions () {
      this.showUploader = true
    },

    // 处理头像操作选择
    onActionSelect (action) {
      if (action.method) {
        action.method()
      }
      this.showUploader = false
    },

    // 拍照
    takePhoto () {
      console.log('调用拍照功能')
      // 实际项目中这里应该调用相机API
      // this.uploadAvatar(file)
    },

    // 从相册选择
    pickFromGallery () {
      console.log('调用相册选择')
      // 实际项目中这里应该调用文件选择API
      // this.uploadAvatar(file)
    },

    // 上传头像
    async uploadAvatar (file) {
      try {
        const formData = new FormData()
        formData.append('avatar', file)

        const { data } = await ajax.post('/accounts/upload-avatar/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })

        this.userInfo.user.avatar = data.avatar_url
        this.$notify({ type: 'success', message: '头像上传成功' })
      } catch (error) {
        console.error('头像上传失败:', error)
        this.$notify({ type: 'danger', message: '头像上传失败' })
      }
    },

    // 编辑字段
    editField (field) {
      this.$dialog.prompt({
        title: `编辑${this.getFieldName(field)}`,
        message: `当前${this.getFieldName(field)}: ${this.userInfo.profile[field] || '未设置'}`,
        inputPlaceholder: `请输入${this.getFieldName(field)}`,
        showCancelButton: true
      }).then(value => {
        this.updateProfile({ [field]: value })
      }).catch(() => {
        // 取消编辑
      })
    },

    // 获取字段显示名称
    getFieldName (field) {
      const map = {
        nickname: '昵称',
        real_name: '真实姓名',
        email: '邮箱'
      }
      return map[field] || field
    },

    // 显示性别选择器
    showGenderPicker () {
      this.showGenderPopup = true
    },

    // 性别选择确认
    onGenderConfirm (picker, value) {
      this.updateProfile({ sex: value })
      this.showGenderPopup = false
    },

    // 更新个人信息
    async updateProfile (data) {
      try {
        await ajax.patch(AccountsApis.userInfoUrl, data)
        this.$notify({ type: 'success', message: '更新成功' })
        this.fetchUserInfo() // 刷新数据
      } catch (error) {
        console.error('更新失败:', error)
        this.$notify({ type: 'danger', message: '更新失败' })
      }
    }
  },
  created () {
    this.fetchUserInfo()
  }
}
</script>

<style lang="less" scoped>
.profile-page {
  padding-bottom: 20px;

  .avatar-section {
    padding: 30px 0;
    text-align: center;
    position: relative;

    .camera-icon {
      position: absolute;
      right: calc(50% - 60px);
      bottom: 30px;
      background: #07c160;
      color: white;
      border-radius: 50%;
      padding: 4px;
      font-size: 16px;
    }
  }

  .van-cell__value {
    color: #969799;
  }
  .van-cell-group {
    text-align: left;
  }
}
</style>
