## Booking & Administration service for Dangedan B&B website

### 主要功能

### 前台(住客端)：

✔ 瀏覽客房資訊

✔ 查詢空房

✔ 線上訂房

✔ RWD

5.訂房簡訊及EMail通知

6.第三方api串接：IG

#### API規劃

ROOM

GET /api/rooms 取得所有房型資訊列表

GET /api/rooms/<str:room_type> 依房型取得房型資訊列表

GET /api/rooms?guests=<int:num_of_guests> 依入住人數取得房型資訊列表

GET /api/rooms/<str:room_type>/available/from<str:start_date_string>to<str:end_date_string> 依日期區間，搜尋可供預定的房間

ORDER

POST /api/orders 建立新的訂房資料

GET /api/order/<int:order_id> 依據訂單編號取得訂房資料


### 管理後台(民宿員工端)：

✔ 員工管理帳號登入、登出、及是否為已登入判斷。

2.當日(週)預定及入住資訊，彙總儀表板

3.訂單查詢、付款確認、及取消

4.住客資料登載及建立CRM資料庫

5.網站客房資訊上架、修改、關房、下架

6.員工管理帳號操作紀錄

#### API規劃

USER

GET /auth/user 取得目前已登入的員工資料

POST /auth/user 員工管理帳號登入

DELETE /auth/user 員工管理帳號登出

ORDER

GET /auth/orders 取得所有的訂房資料列表

GET /auth/orders/<str:status> 依據訂單狀態(新訂單、已付款、取消)取得的訂房資料列表

GET /auth/order/<int:order_id> 依據訂單編號取得訂房資料

PUT /auth/order/<int:order_id> 依據訂單編號修改訂房資料

PAYMENT

GET /auth/payment/<str:payment_id> 依據付款編號取得付款資料

POST /auth/payment/<int:order_id> 依據訂單編號，建立新的付款資料

PUT /auth/payment/<str:payment_id> 依據付款編號修改付款資料