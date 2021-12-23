function dateIndexToString(n=1){  // 自今天起算的第n天，今天為0，明天即為1，...以此類推
    let date_obj = new Date(); //目前日期時間
    let now_s = date_obj.getTime(); //目前毫秒數
    date_obj.setTime(now_s+1000*60*60*24*n); // 加n天
    let d = date_obj.getDate();
    if(d<10){
        d = "0"+ d.toString();
    }else{
        d = d.toString();
    }
    let m = date_obj.getMonth()+1;
    if(m<10){
        m = "0"+ m.toString();
    }else{
        m = m.toString();
    }
    return (date_obj.getFullYear().toString()+"-"+m+"-"+d)
}
function dateStringToIndex(date_string){
    const one_day_ms = 1000*60*60*24;
    const today_string = dateIndexToString(0);
    let today_ms = new Date(today_string).getTime();
    let target_date_ms = new Date(date_string).getTime()
    return (target_date_ms-today_ms)/one_day_ms
}

function getWeeklyCalendar(start_date_string, num_of_guests){
    const url = `${window.origin}/api/booked_calendar/start=${start_date_string}&guests=${num_of_guests}`;
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json();
        }else{
            console.log(response.json());
        }
    })
    return p
}