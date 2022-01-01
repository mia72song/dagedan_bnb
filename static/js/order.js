function orderRequest(url){
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json()
        }else if(response.status===500){
            console.log(response.json());
        }else{
            handleLogout();
        }
    })
    return p
}
function getOrdersByStatus(status){
    // status = NEW, ALL, PAID, CANCEL
    let url;
    if(status=="ALL"){
        url = `${window.origin}/auth/orders`
    }else{
        url = `${window.origin}/auth/orders/status=${status}`
    }
    let p = orderRequest(url).then(resp=>{
        if(resp.data){
            return resp.data
        }
    })
    return p
}
function getOrderById(order_id){
    const url = `${window.origin}/auth/order/${order_id}`
    let p = orderRequest(url).then(resp=>{
        if(resp.data){
            return resp.data
        }
    })
    return p
}
function getOrdersByKeyword(data_type, keyword){
    const url = `${window.origin}/auth/orders/${data_type}=${keyword}`
    let p = orderRequest(url).then(resp=>{
        if(resp.data){
            return resp.data
        }
    })
    return p
}

function postOrder(data){
    let p = fetch(`${window.origin}/api/orders`, {
        method: "post",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }).then(response=>{
        if(response.status!==500){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}