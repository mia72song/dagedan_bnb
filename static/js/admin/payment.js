function paymentRequestWithData(method, data){
    const url = `${window.origin}/auth/payment`;
    let p=fetch(url, {
        method,
        credentials: "include",
        headers: {
            "Content-Type":"application/json",
            "Authorization": `Bearer ${localStorage.getItem("jwt")}`
        },
        body: JSON.stringify(data)
    }).then(response=>{
        if(response.status===403){
            location.href = `/admin`;
        }else if(response.status===200){
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