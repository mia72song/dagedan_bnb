let search_string_1st;
let search_string_2nd;
let search_string_3th;

function comma(value){
    if(!isNaN(Number(value))){
        return value.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",")
    }else{
        alert(`${value}不是數字!`)
    }
}
class RoomBox extends React.Component{
    state = {
        total_quantity: null
    }
    componentDidMount(){
        this.token=PubSub.subscribe("QUANTITY", (_, quantity)=>{
            // console.log("RoomBox被通知：", quantity);
            let total_quantity;
            if(this.state.total_quantity){
                total_quantity = this.state.total_quantity+quantity;
            }else{
                total_quantity = quantity;
            }
            this.setState({total_quantity});
        })
    }
    render(){
        const rooms = this.props.rooms;
        let rooms_content = [];
        Object.keys(rooms).forEach(type=>{
            rooms_content.push(<RoomInfo type={type} info={rooms[type]}/>);
        })
        return(
            <div id="room_box">
                { this.state.total_quantity===0 && <h1 id="no_available_msg">搜尋期間內無空房</h1> }
                { rooms_content }
            </div>
        )
    }
    componentWillUnmount(){
        // 取消KEYWORD消息訂閱
        PubSub.unsubscribe(this.token);
    }
}
class RoomInfo extends React.Component{
    state = null
    componentDidMount(){
        const check_in_date = (search_string_1st[0]==="checkin" && search_string_1st[1]);
        const check_out_date = (search_string_2nd[0]==="checkout" && search_string_2nd[1]);
        availableRoomRequest(check_in_date, check_out_date, this.props.type).then(resp=>{
            if(resp.min_quantity!==0){
                this.setState(resp)
            }
            PubSub.publish('QUANTITY', resp.min_quantity);
        })
    }
    render(){
        return(
            <div>
                {this.state && (
                    <div className="room_info_div">
                        <div className="room_img_div">
                            <img src={this.props.info.images && this.props.info.images[0]} alt=""/>    
                        </div>
                        <div className="room_detail">
                            <div>
                                <h3 id={`room_type_${this.props.type}`}>{this.props.info.name}</h3>
                                <p>{this.props.info.description}<a href="#">更多詳情</a></p>
                            </div>
                            <div className="special_price">
                                <h4>特價方案：</h4>
                                <p>平日特價：
                                    <span className="currency">NT </span>
                                    <span className="price">{comma(this.props.info.rate_weekday)}</span>
                                </p>
                                <p>一人入住：
                                    <span className="currency">NT </span>
                                    <span className="price">{comma(this.props.info.rate_weekday*this.props.info.single_discount)}</span>
                                    <span className="currency"> 起</span>
                                </p>
                            </div>
                        </div>
                        <div className="room_rate">
                            <div>
                                <p>每晚定價：(適用{this.props.info.accommodate}人)</p>
                                <h1><span>NT </span>{comma(this.props.info.rate_holiday)}</h1>
                            </div>
                            <div>
                                <a href={`#room_type_${this.props.type}`}>
                                    <button type="button" class="btn btn-dark book_now_btn" onClick={this.handleBookingForm}>Book Now</button>
                                </a>
                                {this.state.min_quantity<=2 && <p>最後{this.state.min_quantity}間</p>}
                            </div>
                        </div>
                    </div>
                )}
                {this.state && (
                    <div id={`booking_detail_${this.props.type}`}>
                        <BookingForm info={this.props.info} available={this.state}/>
                    </div>
                )}
            </div>
        )
    }
    handleBookingForm=()=>{
        document.querySelectorAll("div[id^='booking_detail_']").forEach(div=>{
            div.style.display="";
        })
        let booking_form = document.getElementById(`booking_detail_${this.props.type}`);
        if(booking_form.style.display===""){
            booking_form.style.display="block";
        }
    }
}
class BookingForm extends React.Component{
    state = {
        room_type: "",
        check_in_date: "",
        check_out_date: "",
        nights: 1,
        num_of_guests: 1,
        quantity: 1,
        name: "",
        gender: "male",
        phone: "",
        email: "",
        arrival_datetime: ""
    }
    componentDidMount(){
        const check_in_date = (search_string_1st[0]==="checkin" && search_string_1st[1]);
        const check_out_date = (search_string_2nd[0]==="checkout" && search_string_2nd[1]);
        this.setState({
            room_type: this.props.available.room_type,
            check_in_date,
            check_out_date,
            nights: dateStringToIndex(check_out_date)-dateStringToIndex(check_in_date),
            num_of_guests: parseInt(search_string_3th[0]==="guests" && search_string_3th[1]),
            arrival_datetime: `${check_in_date}T15:00`
        })
    }
    render(){
        //console.log(this.props.info);
        //console.log(this.props.available);
        return(
            <div>
                BookingForm
            </div>
        )
    }
    updateAmount=(quantity, guests)=>{
        let amount = 0;
        this.props.available.data.forEach(date=>{
            if(date.is_holiday){
                amount = amount+this.props.info.rate_holiday*quantity
            }else{
                amount = amount+this.props.info.rate_weekday*quantity
            }
            if(parseInt(guests)===1){
                amount = amount*this.props.info.single_discount
            }
        })
        return parseInt(amount)
    }
}
if(window.location.search!==""){
    search_string_1st = location.search.split("&")[0].split("?")[1].split("=");
    search_string_2nd = location.search.split("&")[1].split("=");
    search_string_3th = location.search.split("&")[2].split("=");
    const num_of_guests = (search_string_3th[0]==="guests" && search_string_3th[1]);
    roomInfoRequest(num_of_guests).then(respR=>{
        ReactDOM.render(<RoomBox rooms={respR.data}/>, document.getElementById("room_box_wrap"));
    });
}
