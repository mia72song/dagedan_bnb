function roomRequest(type=null){
    let url;
    if(type){
        url = `${window.origin}/api/room/${type}`;
    }else{
        url = `${window.origin}/api/rooms`;
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