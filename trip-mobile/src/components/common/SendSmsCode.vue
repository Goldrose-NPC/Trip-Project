<template>
    <!-- 短信验证码发送相关逻辑 -->
     <van-button
     size="small"
     type="primary"
     @click="sendSmsCode"
     >{{ sendBtnText }}</van-button>
</template>
<script>
import { SystemApis } from '@/utils/apis'
import { ajax } from '@/utils/ajax'
export default {
  props: ['phoneNum'],
  data () {
    return {
      sendBtnText: '发送验证码',
      counter: 60,
      timer: null
    }
  },
  methods: {
    /**
     * 倒计时
     */
    countDown () {
      this.timer = setInterval(() => {
        this.sendBtnText = `(${this.counter}秒)后重新发送`
        this.counter--
        if (this.counter < 0) {
          clearInterval(this.timer)
          this.sendBtnText = '发送验证码'
        }
      }, 1000)
    },
    /**
     * 发送验证码
     */
    sendSmsCode () {
      // 判断手机号是否已输入
      if (!this.phoneNum) {
        this.$notify('请输入手机号')
        return false
      }
      // 调用接口，发送短信验证码
      ajax.post(SystemApis.sendSmsUrl, {
        phone_num: this.phoneNum
      }).then((response) => {
      // 提示用户验证码已经发送
        this.$notify({
          message: `验证码为：${response.data.sms_code}, ${response.data.timeout / 60}分钟内有效`,
          duration: 1000 * 10,
          type: 'success'
        })
        this.isSmsSend = true
        // 开启倒计时60s之后才能再次点击
        this.countDown()
      }).catch(err => {
        // 如果发生异常，提示用户重新操作
        this.isSmsSend = false
        this.sendBtnText = '点击发送验证码'
        console.log('SendSmsCode-sendSmsCode', err)
      })
    }
  }
}
</script>
