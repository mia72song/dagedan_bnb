function getBookedListByOrderId(oid){
    const url = `${window.origin}/auth/booked/${oid}`;
    let p=fetch(url).then(response=>{
        if(response.status===200){
            return response.json()
        }else if(response===401){
            handleLogout()
        }else{
            console.log(response.json())
        }
    })
    return p
}