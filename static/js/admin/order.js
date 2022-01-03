function getOrders(col_name=null, keyword=null){
    let url = `${window.origin}/auth/orders`;
    if(col_name && keyword){
        url = url+`?${col_name}=${keyword}`
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