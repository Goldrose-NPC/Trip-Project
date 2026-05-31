# Trip

一个基于 `Django + Vue2 + Vant` 的旅游景点移动端项目，采用前后端分离方式实现首页推荐、景点搜索、景点详情、门票展示、评论列表、手机验证码注册、登录与个人中心等功能。

这个仓库更适合作为“个人练手项目 / 课程项目 / 简历中的完整小型全栈作品”来展示：它覆盖了数据库建模、接口设计、表单校验、Redis 验证码缓存、移动端页面拆分、前后端联调等完整链路，同时也保留了一些可继续扩展的功能点。

## 项目定位

- 项目名称：旅游景点移动端展示系统
- 形态：移动端 H5 Web App
- 架构：前后端分离
- 前端：Vue 2、Vue Router、Vuex、Axios、Vant、Less
- 后端：Django 3、MySQL、Redis
- 适合展示的能力：
  - RESTful 风格接口设计
  - Django 自定义用户模型与表单校验
  - 基于 Redis 的短信验证码注册流程
  - Vue 组件化开发与移动端 UI 适配
  - 景点、门票、评论、轮播图等业务模块拆分

## 我帮你梳理后的项目结论

从代码现状来看，这不是一个“纯 Demo 页面”，而是一个已经具备业务主线的小型全栈项目：

- 已经完成的主链路：
  - 首页轮播图展示
  - 热门推荐 / 精选景点展示
  - 景点搜索与分页
  - 景点详情页
  - 门票信息展示
  - 评论列表与分页加载
  - 手机验证码注册
  - 用户登录 / 退出登录
  - 个人中心与用户信息读取
- 仍然属于“预留/半成品”的部分：
  - 景点图片页目前没有独立图片接口支撑
  - 个人信息编辑、头像上传在前端有交互雏形，但后端接口未闭环
  - 订单、收藏、地址、设置、帮助等入口是预留功能
  - 仓库里没有看到现成的演示初始化数据脚本，运行演示需要自行准备数据库内容

如果你要把它放进简历，我建议把它包装成：

> 一个基于 Django + Vue 的旅游景点移动端项目，完成了用户注册登录、景点检索、景点详情、门票展示、评论浏览与首页推荐等核心功能，并实现了验证码注册、分页接口、通用响应封装与移动端组件化页面开发。

这个表述是够格的，前提是 README 写清楚、截图补齐、仓库结构整理干净。

## 项目结构

```text
Trip/
├─ trip-backend/            # Django 后端
│  ├─ accounts/             # 用户、资料、登录记录、注册登录接口
│  ├─ sight/                # 景点、门票、评论、景点介绍
│  ├─ system/               # 轮播图、图片关联、短信验证码
│  ├─ utils/                # 通用模型、分页序列化、统一响应
│  ├─ docs/                 # 接口文档草稿、PDMan 数据模型
│  └─ trip/                 # Django 配置
├─ trip-mobile/             # Vue2 + Vant 前端
│  ├─ src/views/            # 页面级组件
│  ├─ src/components/       # 公共组件与业务组件
│  ├─ src/router/           # 路由配置
│  ├─ src/store/            # Vuex 状态管理
│  └─ src/utils/            # Axios 封装、接口常量
└─ README.md
```

## 功能清单

### 1. 首页推荐

- 轮播图接口：`/system/slider/list/`
- 首页包含轮播图、热门推荐、精选景点三部分
- 热门与精选数据都来自后端景点接口筛选参数
- 前端使用 `Banner`、`Hot`、`Fine` 三个组件拆分

### 2. 景点搜索与列表

- 接口：`/sight/sight/list/`
- 支持按景点名称模糊搜索
- 支持 `is_hot`、`is_top` 条件筛选
- 支持分页参数 `page` 与 `limit`
- 前端搜索页复用了景点列表组件 `ListSight.vue`

### 3. 景点详情

- 接口：
  - 景点详情：`/sight/sight/detail/<id>/`
  - 门票列表：`/sight/ticket/list/<id>/`
  - 评论列表：`/sight/comment/list/<id>/`
  - 景点介绍：`/sight/sight/info/<id>/`
- 展示内容包括：
  - 景点大图
  - 评分
  - 评论数量
  - 地区信息
  - 门票价格与库存信息
  - 热门评论

### 4. 用户体系

- 登录接口：`/accounts/user/api/login/`
- 退出接口：`/accounts/user/api/logout/`
- 用户信息接口：`/accounts/user/api/info/`
- 注册接口：`/accounts/user/api/register/`
- 使用自定义 `User` 模型，扩展了头像和昵称字段
- 注册流程包含：
  - 手机号格式校验
  - 昵称唯一性校验
  - Redis 中短信验证码校验
  - 自动创建 `Profile`
  - 自动登录
  - 记录登录日志

### 5. 短信验证码

- 接口：`/system/send/sms/`
- 当前实现为开发态验证码流程：
  - 校验手机号
  - 生成 6 位验证码
  - 存入 Redis，默认 5 分钟有效
  - 直接把验证码回传给前端显示
- 这是典型的开发 / 演示环境做法，方便联调

### 6. 个人中心

- 已实现：
  - 读取当前登录用户信息
  - 个人中心首页展示
  - 基础个人信息展示
  - 退出登录
- 预留但未完整实现：
  - 头像上传
  - 资料编辑保存
  - 订单、收藏、地址、设置等后续模块

## 核心数据模型

### 景点模块

- `Sight`：景点基础信息
  - 名称、描述、主图、详情图、正文内容
  - 评分、最低价格
  - 省市区乡镇
  - 是否热门 / 是否精选
- `Info`：景点介绍
  - 入园参考
  - 特色玩法
  - 交通到达
  - 温馨提示
- `Ticket`：门票
  - 票种、原价、折扣、库存、有效期、退改政策
- `Comment`：评论
  - 评论人、评分、点赞数、回复关系、公开状态、评论图片

### 用户模块

- `User`
  - 基于 Django `AbstractUser`
  - 扩展头像、昵称
- `Profile`
  - 真实姓名、邮箱、手机号、性别、年龄
- `LoginRecord`
  - 登录时间、IP、来源、客户端版本

### 系统模块

- `Slider`
  - 首页轮播图
- `ImageRelated`
  - 通用图片关联表，支持与景点、评论等内容关联

## 接口风格

项目内部已经抽出了统一响应结构与错误码：

- `200`：查询成功
- `201`：提交成功
- `400`：参数错误
- `401`：未登录
- `405`：请求方式不允许
- `500`：服务器异常

分页接口返回结构大致如下：

```json
{
  "meta": {
    "total_count": 20,
    "current_page": 1,
    "page_count": 4
  },
  "objects": []
}
```

## 技术亮点

- 前后端分离，前端通过 Axios 访问 Django 接口
- Vue 开发时通过 `vue.config.js` 代理 `/api` 到 Django 服务
- 登录态通过 Cookie 维持，Axios 开启 `withCredentials`
- 后端通过 Django Form 统一处理登录、注册、验证码校验逻辑
- 后端封装了统一 JSON 响应类，便于前后端约定错误处理
- 通过通用模型 `CommonModel` 复用 `is_valid / created_at / updated_at`
- 使用 `GenericRelation` 设计图片关联，支持景点和评论复用图片能力

## 页面截图清单

下面这些位置你后续运行项目后，按顺序截图即可。我把 README 里的占位和建议说明一起列出来了。

### 截图 1：首页

- 建议内容：轮播图 + 热门推荐 + 精选景点
- 建议文件名：`docs/screenshots/home.png`
- README 中可替换位置：

```md
![首页](docs/screenshots/home.png)
```

### 截图 2：搜索页 / 景点列表页

- 建议内容：搜索框、景点列表、分页器
- 建议文件名：`docs/screenshots/search.png`

```md
![搜索页](docs/screenshots/search.png)
```

### 截图 3：景点详情页

- 建议内容：景点头图、评分、门票、评论摘要
- 建议文件名：`docs/screenshots/sight-detail.png`

```md
![景点详情](docs/screenshots/sight-detail.png)
```

### 截图 4：评论列表页

- 建议内容：评论卡片、评分、图片、分页/下拉加载
- 建议文件名：`docs/screenshots/comments.png`

```md
![评论列表](docs/screenshots/comments.png)
```

### 截图 5：登录页

- 建议内容：手机号登录表单
- 建议文件名：`docs/screenshots/login.png`

```md
![登录页](docs/screenshots/login.png)
```

### 截图 6：注册页

- 建议内容：短信验证码注册流程
- 建议文件名：`docs/screenshots/register.png`

```md
![注册页](docs/screenshots/register.png)
```

### 截图 7：个人中心页

- 建议内容：头像、个人中心、退出登录
- 建议文件名：`docs/screenshots/mine.png`

```md
![个人中心](docs/screenshots/mine.png)
```

### 截图 8：个人信息页

- 建议内容：昵称、手机号、性别、邮箱等信息展示
- 建议文件名：`docs/screenshots/profile.png`

```md
![个人信息](docs/screenshots/profile.png)
```

### 可选截图 9：Django Admin 后台

- 如果你录简历项目会很加分
- 建议展示：景点、门票、评论、轮播图、用户数据模型
- 建议文件名：`docs/screenshots/admin.png`

```md
![管理后台](docs/screenshots/admin.png)
```

## 本地运行方式

### 1. 后端启动

建议环境：

- Python 3.9.x
- MySQL 5.7+ / 8.x
- Redis 6.x+

安装依赖：

```bash
cd trip-backend
pip install -r requirements.txt
```

数据库配置位于：

- `trip-backend/trip/settings.py`

默认数据库连接是：

- 数据库：`trip_django`
- 用户名：`root`
- 密码：`666666`
- 主机：`127.0.0.1`
- 端口：`3306`

Redis 配置：

- 地址：`redis://127.0.0.1:6379/1`

启动命令：

```bash
cd trip-backend
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

说明：

- 仓库中未发现现成的初始化演示数据脚本，因此需要你自行导入或在后台补充轮播图、景点、门票、评论数据。
- 如果没有数据，前端页面能打开，但内容会是空列表。

### 2. 前端启动

```bash
cd trip-mobile
npm install
npm run serve
```

默认开发地址：

- `http://localhost:8080`

前端通过代理把：

- `/api/*`

转发到：

- `http://127.0.0.1:8000/*`

对应配置文件：

- `trip-mobile/vue.config.js`

## 当前验证情况

本次整理 README 时，我做了最小程度的环境检查：

- 前端 `npm run lint` 已跑通
- 前端存在 `node_modules`，说明你这台机器以前已经装过依赖
- 后端未能执行 `python manage.py check`
  - 原因：当前环境没有安装 Django
  - 这不代表项目本身不能运行，只代表这次整理时本机 Python 环境不完整

## 已知问题与待优化点

- 仓库缺少现成的演示数据初始化脚本
- 个人中心中的部分入口是预留功能，不是完整闭环
- 用户资料编辑与头像上传缺少完整后端接口支持
- 景点图片页目前没有独立图片接口
- 配置仍然是本地开发配置，发布到公网前需要改造：
  - `DEBUG`
  - `SECRET_KEY`
  - 数据库密码
  - 静态资源与媒体文件配置

## 为什么它适合放到简历里

它的价值不在于“功能有多大”，而在于已经体现出完整工程思路：

- 有前后端分层，不是单页静态作品
- 有数据模型设计，不是纯假数据页面
- 有用户、景点、门票、评论、轮播图等真实业务实体
- 有登录、注册、验证码、分页、统一错误处理这些通用能力
- 有移动端 UI 组件化拆分

如果你要把它放到简历里，建议用“个人全栈项目”或“课程实践项目”的口径，而不是包装成生产级商业系统。

## 简历描述参考

你可以直接参考下面这版：

> 独立完成一个基于 Django + Vue2 + Vant 的旅游景点移动端项目，采用前后端分离架构，实现了首页推荐、景点搜索、景点详情、门票展示、评论浏览、手机验证码注册登录、个人中心等功能；后端完成用户/景点/评论等模型设计与分页接口封装，前端完成移动端页面组件化开发与接口联调。

如果你想再往上提一档，后续建议优先补这三件事：

1. 补一个初始化演示数据脚本或 SQL 文件
2. 把个人资料编辑和图片页补完整
3. 录一个 30~60 秒的项目演示 GIF 或短视频

