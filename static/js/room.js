function roomInfoRequest(num_of_guests=1, room_type=null){
    let url = `${window.origin}/api/rooms`;
    if(room_type){
        url = url+`/${room_type}`
    }else if(num_of_guests){
        url = url+`?guests=${num_of_guests}`
    }
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}

function availableRoomRequest(checkin_date_string, checkout_date_string, room_type){
    const start_date_string = checkin_date_string;
    const end_date_string = dateIndexToString(dateStringToIndex(checkout_date_string)-1);
    let url = `${window.origin}/api/rooms/${room_type}/available/from${start_date_string}to${end_date_string}`;
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json();
        }else{
            console.log(response.json());
        }
    })
    return p
}