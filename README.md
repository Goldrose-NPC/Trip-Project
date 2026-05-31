# Trip Project

基于 `Django + Vue 2 + Vant` 的旅游景点移动端 Web 应用，采用前后端分离架构，围绕景点浏览、搜索、详情展示、门票信息、评论内容和用户登录注册等核心场景构建。

## 项目简介

Trip Project 面向旅游景点展示场景，提供移动端 H5 访问体验。项目包含首页推荐、景点列表检索、景点详情展示、门票信息展示、评论列表浏览、短信验证码注册、用户登录与个人中心等功能模块。

后端负责用户体系、景点数据、轮播图、门票、评论、验证码等业务逻辑；前端负责移动端页面渲染、接口调用、登录态处理和组件化 UI 组织。

## 项目亮点

- 前后端分离实现移动端旅游景点浏览场景，覆盖首页推荐、搜索、详情、评论、登录注册等完整主流程
- 后端采用 Django 组织用户、景点、轮播图、门票、评论等业务模块，并提供统一 JSON 响应与分页结构
- 前端采用 Vue 2 + Vant 搭建移动端 H5 界面，页面拆分清晰，具备较完整的组件复用结构
- 注册流程接入 Redis 验证码校验机制，体现了表单校验、缓存使用和登录态处理的完整链路
- 对历史图片路径和开发环境媒体访问做了兼容处理，便于本地运行和项目演示

## 技术栈

### Frontend

- Vue 2
- Vue Router
- Vuex
- Axios
- Vant
- Less

### Backend

- Django 3.0.9
- MySQL
- Redis
- Pillow
- django-redis

## 功能概览

### 已实现功能

- 首页轮播图展示
- 热门推荐景点展示
- 精选景点展示
- 景点名称搜索
- 景点列表分页
- 景点详情页展示
- 门票列表展示
- 评论列表展示与分页加载
- 手机验证码注册
- 用户登录 / 退出登录
- 用户基本信息读取
- 登录日志记录

### 当前保留的扩展点

- 景点图片独立页面
- 景点介绍页完整前端展示
- 个人资料编辑闭环
- 头像上传接口闭环
- 订单、收藏、地址、设置等扩展业务模块

## 项目结构

```text
Trip/
├─ trip-backend/
│  ├─ accounts/                # 用户、资料、登录记录、注册登录接口
│  ├─ sight/                   # 景点、门票、评论、景点介绍
│  ├─ system/                  # 轮播图、图片关联、短信验证码
│  ├─ utils/                   # 通用模型、分页封装、统一响应
│  ├─ docs/                    # 接口文档草稿、数据模型设计文件
│  └─ trip/                    # Django 配置
├─ trip-mobile/
│  ├─ src/views/               # 页面组件
│  ├─ src/components/          # 公共组件与业务组件
│  ├─ src/router/              # 路由配置
│  ├─ src/store/               # Vuex 状态管理
│  ├─ src/utils/               # 接口地址、请求封装、工具方法
│  └─ public/static/           # 演示用静态资源
├─ docs/
│  └─ screenshots/             # README 截图目录
└─ README.md
```

## 系统架构

```text
trip-mobile (Vue 2 + Vant)
        │
        │  Axios / /api proxy / cookie
        ▼
trip-backend (Django)
├─ accounts  用户、注册、登录、资料、登录记录
├─ sight     景点、门票、评论、详情介绍
├─ system    轮播图、短信验证码、图片关联
└─ utils     通用模型、分页序列化、统一响应
        │
        ├─ MySQL   业务数据存储
        └─ Redis   验证码与缓存
```

前端通过 `Axios` 请求 Django 接口，开发环境下由 Vue Dev Server 将 `/api` 代理到后端服务。后端负责数据查询、表单校验、用户登录态与验证码逻辑，MySQL 用于持久化业务数据，Redis 用于缓存与短信验证码场景。

## 主要业务模块

### 1. 首页推荐

- 轮播图数据来自 `/system/slider/list/`
- 首页展示轮播图、热门推荐、精选景点
- 首页组件拆分为 `Banner`、`Hot`、`Fine`

### 2. 景点列表与搜索

- 接口：`/sight/sight/list/`
- 支持按名称模糊搜索
- 支持 `is_hot`、`is_top` 条件筛选
- 支持 `page`、`limit` 分页参数
- 前端复用 `ListSight.vue` 作为通用景点卡片组件

### 3. 景点详情

- 景点详情：`/sight/sight/detail/<id>/`
- 门票列表：`/sight/ticket/list/<id>/`
- 评论列表：`/sight/comment/list/<id>/`
- 景点介绍：`/sight/sight/info/<id>/`

详情页当前可展示以下信息：

- 景点名称与头图
- 评分与评论数
- 所在地区
- 门票价格与库存信息
- 热门评论摘要

### 4. 用户体系

- 登录接口：`/accounts/user/api/login/`
- 退出接口：`/accounts/user/api/logout/`
- 用户信息接口：`/accounts/user/api/info/`
- 注册接口：`/accounts/user/api/register/`

注册流程包括：

- 手机号格式校验
- 昵称唯一性校验
- Redis 短信验证码校验
- 自动创建用户资料
- 自动登录
- 登录日志记录

### 5. 短信验证码

- 接口：`/system/send/sms/`
- 校验手机号格式
- 生成 6 位验证码
- 验证码写入 Redis，默认有效期 5 分钟
- 当前实现为开发调试模式，验证码会直接返回给前端

## 核心数据模型

### 景点模块

- `Sight`
  - 景点基础信息
  - 包含名称、描述、图片、评分、最低价格、地区、热门/精选标记
- `Info`
  - 景点详细介绍
  - 包含入园参考、特色玩法、交通说明、温馨提示
- `Ticket`
  - 景点门票信息
  - 包含票种、价格、折扣、库存、有效期、退改政策
- `Comment`
  - 景点评论信息
  - 包含评论人、评分、点赞、回复关系、评论图片

### 用户模块

- `User`
  - 基于 Django `AbstractUser`
  - 扩展头像与昵称字段
- `Profile`
  - 用户详细资料
  - 包含真实姓名、邮箱、手机号、性别、年龄
- `LoginRecord`
  - 登录日志
  - 记录登录账号、IP、来源、版本、登录时间

### 系统模块

- `Slider`
  - 首页轮播图
- `ImageRelated`
  - 通用图片关联表
  - 可关联景点、评论等不同业务对象

## 接口约定

项目使用统一 JSON 响应结构和错误码封装。

### 常见状态码

- `200` 查询成功
- `201` 提交成功
- `400` 参数错误
- `401` 未登录
- `405` 请求方式不允许
- `500` 服务器异常

### 分页响应示例

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

## 运行环境

### Backend

- Python 3.9.x
- MySQL 5.7+ 或 8.x
- Redis 6.x+

### Frontend

- Node.js 12+
- npm 6+

## 本地运行

### 1. 启动后端

安装依赖：

```bash
cd trip-backend
pip install -r requirements.txt
```

复制环境变量示例文件，并按本地环境修改：

```bash
cd trip-backend
copy .env.example .env
```

后端支持以下环境变量：

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_DB_ENGINE`
- `DJANGO_DB_NAME`
- `DJANGO_DB_USER`
- `DJANGO_DB_PASSWORD`
- `DJANGO_DB_HOST`
- `DJANGO_DB_PORT`
- `DJANGO_REDIS_URL`
- `DJANGO_MEDIA_URL`

默认 Redis 配置：

- `redis://127.0.0.1:6379/1`

执行迁移并启动服务：

```bash
cd trip-backend
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

### 2. 启动前端

复制前端环境变量示例文件：

```bash
cd trip-mobile
copy .env.development.example .env.development
```

如需自定义接口地址，可配置：

- `VUE_APP_API_BASE_URL`

```bash
cd trip-mobile
npm install
npm run serve
```

默认访问地址：

- `http://localhost:8080`

开发环境下，前端会将 `/api/*` 代理到 Django 服务：

- Proxy Target: `http://127.0.0.1:8000/`

对应配置文件：

- `trip-mobile/vue.config.js`

## 页面截图

项目运行截图统一存放在 `docs/screenshots/` 目录，以下为当前主要页面展示。

### 首页

首页包含轮播图、热门推荐、精选景点等内容。

![首页](docs/screenshots/首页.png)

### 搜索页

搜索页支持景点关键字检索、列表展示和分页切换。

![搜索页](docs/screenshots/搜索页.png)

### 景点详情页

景点详情页展示景点头图、评分、地址、门票信息和评论摘要。

![景点详情](docs/screenshots/景点详情.png)

### 评论列表页

评论列表页支持评论内容展示与分页加载。

![评论列表](docs/screenshots/评论列表.png)

### 登录页

![登录页](docs/screenshots/登录页.png)

### 注册页

![注册页](docs/screenshots/注册页.png)

### 个人中心页

个人中心页提供用户信息概览和退出登录入口。

![个人中心](docs/screenshots/个人中心页.png)

### 个人信息页

个人信息页展示昵称、手机号、真实姓名、性别和邮箱等资料。

![个人信息](docs/screenshots/个人信息页.png)

## 已知说明

- 当前仓库未包含现成的演示数据初始化脚本
- 若数据库中没有初始化数据，前端页面会正常渲染但列表内容为空
- 前端部分页面和入口仍处于预留状态，尚未形成完整业务闭环
- 当前配置以本地开发环境为主，部署到生产环境前需要调整数据库、缓存、静态资源和安全配置
- 历史提交中如果曾包含真实密钥或真实数据库密码，应在实际环境中及时轮换

## 后续可优化方向

- 补充初始化数据脚本或示例 SQL
- 完成景点图片页和景点介绍页的前端展示
- 补全用户资料编辑与头像上传接口
- 优化静态资源体积与前端打包结果
- 增加测试用例与部署说明
