function createNewOrder(data){
    let p = fetch(`${window.origin}/api/orders`, {
        method: "post",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }).then(response=>{
        if(response.status==403){
            alert("驗證碼錯誤!!")
        }else if(response.status!==500){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}

function getOrderByOid(oid){
    let p = fetch(`${window.origin}/api/order/${oid}`).then(response=>{
        if(response.status!==500){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}

function getAddOnServices(){
    const url = `${window.origin}/api/add_on_services`;
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}