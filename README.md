## Booking & Administration service for Dangedan B&B website

### 主要功能 ( ✔ 為已完成功能 )

### 前台(住客端)： http://54.150.241.23:8080/

✔ 瀏覽民宿及客房資訊。

✔ 查詢空房：以「日期區間」及「入住人數」搜尋可供預定的房型，以及最後2間(含以下)的提示。

✔ 線上訂房：房價結算(優惠判斷：平日、單人)，及訂房資料填寫。驗證後傳至後端資料庫建檔。

✔ RWD 響應式網頁：根據不同的螢幕尺寸調整顯示效果。

5.訂房簡訊及EMail通知

6.第三方api串接：IG動態分享

✔ API規劃如下：

- ROOM

    GET /api/rooms 取得所有房型資訊列表

    GET /api/rooms/{room_type} 依房型取得房型資訊列表

    GET /api/rooms?guests={num_of_guests} 依入住人數取得房型資訊列表

    GET /api/rooms/{room_type}/available/from{start_date_string}to{end_date_string} 依日期區間，搜尋可供預定的房間

- ORDER

    POST /api/orders 建立新的訂房資料

    GET /api/order/{order_id} 依據訂單編號取得訂房資料


### 管理後台(民宿員工端)：

✔ 員工管理帳號登入：含密碼加密儲存，顯示已登入的使用者名稱，及取得JSON Web Token授權。

2.當日(週)預定及入住資訊，彙總儀表板。

✔ 訂單查詢、付款確認、及取消

4.住客資料登載及建立CRM資料庫

5.網站客房資訊上架、修改、關房、下架

6.員工帳號操作紀錄及權限管制

✔ API規劃如下：

- USER

    GET /auth/user 取得目前已登入的員工資料

    POST /auth/user 員工管理帳號登入

    DELETE /auth/user 員工管理帳號登出

- ORDER 請求時，headers須夾帶jwt授權 Authorization: Bearer <jwt_token>

    GET /auth/orders 取得所有的訂單資料列表

    GET /auth/orders/{status} 依據訂單狀態(新訂單、已付款、取消)取得的訂單列表

    GET /auth/order/{order_id} 依據訂單編號，取得訂單資料

    PUT /auth/order/{order_id} 依據訂單編號，修改訂單資料

- BOOKED 請求時，headers須夾帶jwt授權 Authorization: Bearer <jwt_token>

    GET /auth/booked/{order_id} 依據訂單編號，取得訂房明細

- PAYMENT 請求時，headers須夾帶jwt授權 Authorization: Bearer <jwt_token>

    GET /auth/payment/{payment_id} 依據付款編號取得付款資料

    POST /auth/payment/{order_id} 依據訂單編號，建立新的付款資料

    PUT /auth/payment/{payment_id} 依據付款編號，修改付款資料
    
