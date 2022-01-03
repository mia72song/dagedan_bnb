function getOrders(data_type=null, keyword=null){
    let url = `${window.origin}/auth/orders`;
    if(data_type && keyword){
        if(data_type==="status"){
            url = url+`/${keyword}`
        }else{
            url = url+`?${data_type}=${keyword}`
        }
    }
    let p = fetch(url).then(response=>{
        if(response.status!==500){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}
function orderRequestById(oid, method, data=null){
    pass
}