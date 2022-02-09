class Booked extends React.Component{
    render(){
        //console.log(this.props.data)
        const data = this.props.data
        const arrival_time = data.arrival_datetime.split(" ")[1].split(":");
        return(
            <a href={`${window.origin}/admin/order/${data.order_id}`} className="text-decoration-none py-1">
                { data.booker }
                <br/>
                { data.phone }
                <br/>
                { "預計 " + arrival_time[0] + ":" + arrival_time[1] + " 抵達" }
            </a>
        )
    }
}

const start_date_string = dateIndexToString(0);
const end_date_string = dateIndexToString(6);
//console.log(csrf_token);
fetch(`${window.origin}/auth/booked?start=${start_date_string}&end=${end_date_string}`).then(response=>{
    if(response.status===500){
        console.log(response.json())
    }else{
        return(response.json())
    }
}).then(resp=>{
    //console.log(resp);
    resp.data.forEach(i=>{
        //console.log(i);
        ReactDOM.render(<Booked data={i} />, document.getElementById(`${i.date}_${i.room_no}`));
    })
})