> 前提说明:
> * API调用遵循RESTful规范
> * jQuery `$.ajax()` 方法的 `type`参数可选值:
>     - `GET`: 查询 数据列表 或 单个数据
>     - `POST`: 添加 数据
>     - `PUT`: 更新 数据
>     - `DELETE`: 删除 数据
>     - `OPTIONS`:  查看Api信息
>     - `PATCH`: 更新 数据
> * `DELETE`、`OPTIONS` 无需`data`参数
> * `GET` `data`参数可选, 用户查询筛选
> * `POST`、`PUT` 需要完整`data`参数
> * `PATCH` 暂时保留不使用
> * 页面中相关的js常量:
>     ```js
>     // API根路径
>     GLOGAL.API_BASE = "/api/";
>     // 当前用户(可能未登录)
>     GLOGAL.CURRENT_USER = {
>         "id": 2,
>         "username": "admin",
>         "phone": "13271955906",
>         "url": "http://127.0.0.1:8989/api/users/2/"
>     };
>     // 用户是否登录
>     GLOGAL.CURRENT_LOGINED = true;
>     ```

## 示例 - jQuery 发送 ajax 调用 Api
- 添加/更新 通用代码:
    ```js
    var data = {
        /*内容省略, 参见下方 `data` 结构*/
    };
    $.ajax({ 
        /* type, url 省略 */
        data: JSON.stringify(data),
        processData: false,
        contentType:"application/json; charset=utf-8",
        dataType: "json",
        success: function(resp){
            console.log(resp);
        },
        error: function(jqXHR){
            alert("Error: " + jqXHR.status);
        },
    });
    ```
- 带有queryString参数的查询 通用代码:
    ```js
    var data = {
        /*内容省略, 可为空*/
    };
    $.ajax({ 
        /* type, url 省略 */
        data: data,
        dataType: "json",
        success: function(resp){
            console.log(resp);
        },
        error: function(jqXHR){
            alert("Error: " + jqXHR.status);
        },
    });
    ```
- 删除/无queryString参数的查询 通用代码:
    ```js
    $.ajax({ 
        /* type, url 省略 */
        dataType: "json",
        success: function(resp){
            console.log(resp);
        },
        error: function(jqXHR){
            alert("Error: " + jqXHR.status);
        },
    });

## 示例 - 请求 和 `data` 结构
> * 注
>     - 以下数据中的 `inspector` 取自 `GLOGAL.CURRENT_USER.url`
>     - 请求路径请以 `GLOGAL.API_BASE` 作为前缀拼接
>     - json 数据中的`url`格式的数据均非手动拼接得到, 而是取自现有数据

1. 添加 机构需求(单个)
    ```
    POST /api/organization-demands/
    ```
    ```json
    {
        "organization": "http://127.0.0.1:8989/api/organizations/1/",
        "name": "医用酒精",
        "remark": null,
        "amount": -1,
        "receive_amount": 0
    }
    ```
    注: `organization` 取自查询到的 `organization` 数据
2. 添加 机构募捐信息
    ```
    POST /api/organizations/
    ```
    ```json
    {
        "contacts": [],
        "demands": [],
        "province": "湖北省",
        "city": "武汉市",
        "name": "武汉市人民医院",
        "address": "武汉",
        "source": "微信",
        "verified": false,
        "is_manual": false,
        "inspector": "http://127.0.0.1:8989/api/users/2/",
        "emergency": 0
    }
    ```

3. 更新 机构募捐信息
    ```
    PUT /api/organizations/2/
    ```
    ```json
    {
        "url": "http://127.0.0.1:8989/api/organizations/2/",
        "id": 2,
        "contacts": [
            {
                "organization": "http://127.0.0.1:8989/api/organizations/2/",
                "name": "12345678960",
                "phone": "12345678960"
            }
        ],
        "demands": [],
        "province": "湖北省",
        "city": "武汉市",
        "name": "武汉市人民医院",
        "address": "武汉",
        "source": "微信",
        "verified": false,
        "add_time": "2020-02-01T11:13:16.896248+08:00",
        "is_manual": false,
        "inspector": "http://127.0.0.1:8989/api/users/2/",
        "emergency": 0
    }
    ```