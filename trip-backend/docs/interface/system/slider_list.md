## 首页轮播图的接口
### 请求地址
/system/slider/list
### 调用方式
GET
###请求参数
<table class="table table-hover table-condensed">
    <thead>
        <tr>
            <th>字段</th>
            <th>必选</th>
            <th>类型</th>
            <th>说明</th>
        </tr>
    </thead>
    <tbody>
        <tr class="warning">
            <td>types</td>
            <td>true</td>
            <td>int</td>
            <td>轮播图类型（1：首页轮播）</td>
        </tr>
    </tbody>
</table>

### 返回结果
```
{
    "meta": {},
    "object": [
        {
            "id": 1,
            "img_url": "http%3A//localhost%3A8080/static/home/banner/banner1.jpg",
            "target_url": null,
            "name": "轮播图1"
        },
        {
            "id": 2,
            "img_url": "http%3A//localhost%3A8080/static/home/banner/banner2.jpg",
            "target_url": null,
            "name": "轮播图2"
        }
    ]
}
```

### 返回字段的说明
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
            <td>分页元数据</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>objects</td>
            <td></td>
            <td>objects下位轮播图对象，详情如下</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>id</td>
            <td>int</td>
            <td>记录ID</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>name</td>
            <td>String</td>
            <td>名称</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>desc</td>
            <td>String</td>
            <td>描述信息</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>img_url</td>
            <td>String</td>
            <td>图片地址</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>target_url</td>
            <td>String</td>
            <td>跳转的html链接地址</td>
        </tr>
    </tbody>
</table>