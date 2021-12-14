function paymentRequest(method, data){
    const url = `${window.origin}/auth/payment`;
    let p=fetch(url, {
        method,
        credentials: "include",
        headers: {
            "Content-Type":"application/json"
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
function getPaymentRequest(pid){
    const url = `${window.origin}/auth/payment/${pid}`;
    let p = fetch(url).then(response=>{
        if(response.status!==500){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}