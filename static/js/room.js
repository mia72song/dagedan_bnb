function roomRequest(type=null){
    let url;
    if(type==null){
        url = `${window.origin}/api/rooms`
    }else{
        url = `${window.origin}/api/room/${type}`
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