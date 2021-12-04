function getDateString(n=1){
    let date_obj = new Date() //目前日期時間
    let now_s = date_obj.getTime() //目前毫秒數
    date_obj.setTime(now_s+1000*60*60*24*n) // 加n天
    let d = date_obj.getDate()
    if(d<10){
        d = "0"+ d.toString()
    }else{
        d = d.toString()
    }
    let m = date_obj.getMonth()+1
    if(m<10){
        m = "0"+ m.toString()
    }else{
        m = m.toString()
    }
    return (date_obj.getFullYear().toString()+"-"+m+"-"+d)
}

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

function getRooms(){
    let url = `${window.origin}/api/rooms`
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}