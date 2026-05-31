/**
 * 存放项目中所有的接口地址
 */
const apiHost = process.env.VUE_APP_API_BASE_URL || '/api/'
/**
 * 用户账户相关的接口
 */
const AccountsApis = {
  // 用户登录
  loginUrl: apiHost + 'accounts/user/api/login/',
  // 用户退出登录
  logoutUrl: apiHost + 'accounts/user/api/logout/',
  // 用户信息
  userInfoUrl: apiHost + 'accounts/user/api/info/',
  // 用户注册
  registerUrl: apiHost + 'accounts/user/api/register/'
}
/**
 * 系统模块的接口
 */
const SystemApis = {
  // 轮播图列表
  sliderListUrl: apiHost + 'system/slider/list/',
  // 发送短信验证码
  sendSmsUrl: apiHost + 'system/send/sms/'
}

/**
 * 景点模块
 */
const SightApis = {
  // 景点列表
  sightListUrl: apiHost + 'sight/sight/list/',
  // 景点详情
  sightDetailUrl: apiHost + 'sight/sight/detail/#{id}/',
  // 门票列表
  sightTicketUrl: apiHost + 'sight/ticket/list/#{id}/',
  // 评论列表
  sightCommentUrl: apiHost + 'sight/comment/list/#{id}/'
}

export {
  AccountsApis,
  SystemApis,
  SightApis
}
