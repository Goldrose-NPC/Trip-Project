## 景点列表的接口
### 请求地址
/sight/sight/list
### 调用方式
GET
###请求参数
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
            <td>当前所在页（默认为第一页）</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>is_hot</td>
            <td>boolean</td>
            <td>是否为热门</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>is_top</td>
            <td>boolean</td>
            <td>是否为精选</td>
        </tr>
    </tbody>
</table>

### 返回结果
```
{
    "meta": {
        "total_count": 10,
        "page_count": 2,
        "current_page": 1
    },
    "objects": [
        {
            "id": 1,
            "name": "广州长隆旅游度假区",
            "main_img": "static/home/hot/h2.jpg",
            "score": 5.0,
            "province": "广东省",
            "comment_count": 0
        },
        {
            "id": 10,
            "name": "增城白水寨风景名胜区",
            "main_img": "static/home/hot/h9.jpg",
            "score": 5.0,
            "province": "广东省",
            "comment_count": 0
        },
        {
            "id": 9,
            "name": "岭南印象园",
            "main_img": "static/home/hot/h8.jpg",
            "score": 5.0,
            "province": "广东省",
            "comment_count": 0
        },
        {
            "id": 8,
            "name": "珠江夜游",
            "main_img": "static/home/hot/h10.jpg",
            "score": 4.5,
            "province": "广东省",
            "comment_count": 0
        },
        {
            "id": 7,
            "name": "广东科学中心",
            "main_img": "static/home/hot/h6.jpg",
            "score": 4.5,
            "province": "广东省",
            "comment_count": 0
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
            <td>object</td>
            <td>分页元数据，详情如下</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>total_count</td>
            <td>int</td>
            <td>总数据条数</td>
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
            <td>current_page</td>
            <td>int</td>
            <td>当前页码</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>objects</td>
            <td>Array</td>
            <td>景点数据列表，详情如下</td>
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
            <td>景点名称</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>main_img</td>
            <td>String</td>
            <td>主图URL</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>score</td>
            <td>float</td>
            <td>景点评分（0-5）</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>province</td>
            <td>String</td>
            <td>所在省份</td>
        </tr>
    </tbody>
    <tbody>
        <tr class="warning">
            <td>comment_count</td>
            <td>int</td>
            <td>评论数</td>
        </tr>
    </tbody>
</table>