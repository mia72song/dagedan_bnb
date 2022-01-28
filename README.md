## Booking & Administration service for Dangedan B&B website

### 主要功能 ( ✔ 為已完成 )

#### 前台(住客端)： http://54.150.241.23:5000/

✔ 查詢空房：

- 依「日期區間」及「入住人數」搜尋可預定的房型資訊。

- 該房型最後n間的提示，否則不顯示該房型。

✔ 線上訂房：

- 判斷優惠條件，房價結算：平日價、單人入住。

- 最多可訂房數限制。

- 訂房資料填寫、及檢驗機制：格式正確性、聯絡資訊是否有效等。

✔ RWD：根據不同的螢幕尺寸調整顯示效果。

✔ 訂房EMail通知：

- Jinja2模板生成EMail內文。
 
- 「匯款回報頁面」連結：依據付款期限，提供表單填寫功能。
 
- 異步執行Send Mail。

6.第三方api串接：訂房簡訊通知

✔ API規劃如下：

- ROOM

    GET /api/rooms 取得所有房型資訊列表

    GET /api/rooms/{room_type} 依房型取得房型資訊列表

    GET /api/rooms?guests={num_of_guests} 依入住人數取得房型資訊列表

    GET /api/rooms/{room_type}/available/from{start_date_string}to{end_date_string} 依日期區間，搜尋可供預定的房間

- ORDER

    POST /api/orders 建立新的訂房資料

    GET /api/order/{order_id} 依據訂單編號取得訂房資料
    
- PAYMENT

    POST /api/payment/{order_id} 建立新的付款資料

    GET /api/payment/{order_id} 確認訂單付款狀態

#### 管理後台(民宿員工端)：

✔ 員工管理帳號登入：

- 密碼加密儲存。

- 登入成功後，顯示已登入的使用者名稱，及修改資料時，Update User標註。

- JSON Web Token授權。

✔ 訂單列表：

- 查詢：依據訂單狀態、訂房電話、入住日期、訂單編號，搜尋訂單。

- 修改：建檔匯款資料，修改訂單狀態，顯示「已付款」。

- 取消：手動取消訂單，或超過付款期限，系統自動取消、釋出空房。
  
3.當日(週)預定及入住資訊，彙總儀表板。

4.住客資料登載及建立CRM資料庫

5.網站客房資訊上架、修改、全日關房、下架

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
    
