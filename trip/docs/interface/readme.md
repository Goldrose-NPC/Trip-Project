#  慕旅游网的接口文档
RESTful风格接口
* 200 请求数据成功
* 201 提交数据成功
* 400 参数错误
* 401 未登录
* 403 没有权限
* 500 服务器正忙


## 接口请求地址
1.测试环境
http://test.xxxx.com/

2.生产环境


## 错误代码及文字提示
```
{
    "error_code":"40000",
    "error_msg":"该字段不能为空",
    "error_list": {
        "password": [
            "该字段不能为空。"
        ]    
    }    
}
```

## 请求头添加内容

## 分页请求参数
<table class="table table-hover table-condensed">
    <thead>
        <tr>
            <th>字段</th>
            <th>类型</th>
            <th>说明</th>
        </tr>
    </thead>
    <tbody>
        <tr class="warning">
            <td>page</td>
            <td>int</td>
            <td>当前页（默认为第一页）</td>
        </tr>
    </tbody>
</table>

## 分页响应参数
<table class="table table-hover table-condensed">
    <thead>
        <tr>
            <th>字段</th>
            <th>类型</th>
            <th>说明</th>
        </tr>
    </thead>
    <tbody>
        <tr class="warning">
            <td>meta</td>
            <td></td>
            <td>分页源数据，解释如下</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>total_count</td>
            <td>int</td>
            <td>根据传入条件检索出来的记录条数</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>current_page</td>
            <td>int</td>
            <td>当前第几页</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>page_count</td>
            <td>int</td>
            <td>总页数</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>objects</td>
            <td>Array</td>
            <td>objects为返回对象列表</td>
        </tr>
    </tbody>
</table>

## 接口列表
### 1.系统模块
* [1.1 轮播图接口](./system/slider_list.md)
* [1.2 轮播图接口](./system/slider_list.md)

### 2.景点模块
* [2.1 景点列表接口](./sight/sight_list.md)