function getPaymentByOid(oid){
    let p = fetch(`${window.origin}/api/payment/${oid}`).then(response=>{
        if(response.status===500){
            console.log(response.json())
        }else{
            return response.json()
        }
    })
    return p
}