function roomRequest(num_of_guests=1){
    const url = `${window.origin}/api/rooms?guests=${num_of_guests}`;
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}
function availableRoomsRequest(checkin_date_string, checkout_date_string, room_type){
    const start_date_string = checkin_date_string;
    const end_date_string = dateIndexToString(dateStringToIndex(checkout_date_string)-1);
    let url = `${window.origin}/api/check_available/from${start_date_string}to${end_date_string}/${room_type}`;
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json();
        }else{
            console.log(response.json());
        }
    })
    return p
}