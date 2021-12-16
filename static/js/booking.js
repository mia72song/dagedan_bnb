function getBookingListByDate(start_date_string, end_date_string){
    const url = `${window.origin}/auth/booking/start=${start_date_string}&end=${end_date_string}`
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json();
        }else if(response.status===500){
            console.log(response.json());
        }else{
            handleLogout()
        }
    })
    return p
}
function getBookingListByOrderId(order_id){
    const url = `${window.origin}/auth/booking/oid=${order_id}`
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json();
        }else if(response.status===500){
            console.log(response.json());
        }else{
            handleLogout()
        }
    })
    return p
}