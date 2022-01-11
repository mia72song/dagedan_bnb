// 取得所有，或依據條件(訂單編號、訂單狀況、訂房電話，入住日期)查詢訂單列表
function getOrders(data_type=null, keyword=null){
    let url = `${window.origin}/auth/orders`;
    if(data_type && keyword){
        if(data_type==="order_id"){
            url = `${window.origin}/auth/order/${keyword}`
        }
        else if(data_type==="status"){
            url = url+`/${keyword}`
        }else{
            // booker_phone, check_in_date
            url = url+`?${data_type}=${keyword}`
        }
    }
    let p = fetch(url, {
        method: "get", 
        credentials: "include", 
        headers: {
            "Authorization": `Bearer ${localStorage.getItem("jwt")}`
        }
    }).then(response=>{
        if(response.status===200){
            return response.json()
        }else if(response.status===401){
            //console.log(response.json())
            handleLogout()
        }else{
            console.log(response.json())
        }
    })
    return p
}

// 依據訂單編號oid，修改其唯一訂單狀態
function updateOrderStatusById(self, oid, status){
    pass
}