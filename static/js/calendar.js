function getCalendar(search_string){
    let url = `${window.origin}/api/calendar/${search_string}`
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}