function orderRequestWithAuth(url){
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}
function getOrdersByStatus(status){
    // status = new, all, paid, cancel
    let url;
    if(status=="all"){
        url = `${window.origin}/auth/orders`
    }else{
        url = `${window.origin}/auth/orders/status=${status}`
    }
    let p = orderRequestWithAuth(url).then(resp=>{
        if(resp.data){
            return resp.data
        }
    })
    return p
}
function getOrderById(order_id){
    const url = `${window.origin}/auth/order/${order_id}`
    let p = orderRequestWithAuth(url).then(resp=>{
        if(resp.data){
            return resp.data
        }
    })
    return p
}
function getOrdersByKeyword(data_type, keyword){
    const url = `${window.origin}/auth/orders/${data_type}=${keyword}`
    let p = orderRequestWithAuth(url).then(resp=>{
        if(resp.data){
            return resp.data
        }
    })
    return p
}