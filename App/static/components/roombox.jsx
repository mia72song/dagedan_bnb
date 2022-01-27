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
                                <h3>{this.props.info.name}</h3>
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
                                <button className="book_now_btn" onClick={this.handleBookingForm}>Book Now</button>
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
        // console.log(this.props);
        return(
            <form className="booking_form" onSubmit={this.handelSubmit}>
                <div className="booking_detail">
                    <h4>- 訂房明細 -</h4>
                    <p>期間：{this.state.check_in_date} ~ {this.state.check_out_date}，共 {this.state.nights} 晚</p>
                    <p>房型：
                        {this.props.info.name} * 
                        <input type="number" value={this.state.quantity} min="1" max={Math.min(this.state.num_of_guests, this.props.available.min_quantity)} 
                        onChange={this.handleChange("quantity")}/>
                        間
                    </p>
                    <p>人數：
                        <input type="number" value={this.state.num_of_guests} min="1" max={this.props.info.accommodate} 
                        onChange={this.handleChange("num_of_guests")}/>
                        人
                    </p>
                    <p>總金額：新台幣
                        <input type="text" disabled="true" readOnly="true" id={`total_amount_${this.state.room_type}`}
                        value={this.updateAmount(this.state.quantity, this.state.num_of_guests)}/>
                        元    
                    </p>
                </div>
                <div className="arrow_img_div">
                    <img src="static\images\right.png" alt=""/>
                </div>
                <div className="booker_info">
                    <h4>- 訂房人資訊 -</h4>
                    <div>
                        <label for="booker_name">訂房全名：</label>
                        <input type="text" value={this.state.name} onChange={this.handleChange("name")} pattern="^[\u4e00-\u9fa5]+$|^[a-zA-Z\s]+$" required/>
                        <span className="radio_container">
                            <input type="radio" checked={this.state.gender==="male"} onChange={this.handelGenderCheck("male")}/>
                            <label for="">先生</label>
                        </span>
                        <span className="radio_container">
                            <input type="radio" checked={this.state.gender==="female"} onChange={this.handelGenderCheck("female")}/>
                            <label for="">小姐</label>
                        </span>
                    </div>
                    <div>
                        <label for="phone">聯絡手機：</label>
                        <input type="tel" minlength="10" maxlength="20" value={this.state.phone} onChange={this.handleChange("phone")} required/>
                    </div>
                    <div>
                        <label for="email">E-Mail：</label>
                        <input type="email" value={this.state.email} onChange={this.handleChange("email")} required/>  
                    </div>
                    <div>
                        <label for="arrival_datetime">預計抵達時間：</label>
                        <input type="datetime-local" min={`${check_in_date}T15:00`} max={`${check_in_date}T21:00`} 
                        value={this.state.arrival_datetime} onChange={this.handleChange("arrival_datetime")}/> 
                    </div>
                    <div>
                        <input type="submit" value="確認訂房" />    
                    </div>
                </div>
            </form>
        )
    }
    handleChange=(dataType)=>{
        return(eOby)=>{
            let value = (
                (dataType==="num_of_guests" || dataType==="quantity")? 
                parseInt(eOby.target.value) : eOby.target.value
            );
            if(dataType==="num_of_guests" && value===1){
                this.setState({
                    num_of_guests: 1,
                    quantity: 1
                });
            }else{
                this.setState({[dataType]: value});
            }
        }
    }
    handelGenderCheck=(gender)=>{
        return(eObj)=>{
            this.setState({gender})
        }
    }
    handelSubmit=(eObj)=>{
        eObj.preventDefault();
        // 結算金額
        const amount = document.getElementById(`total_amount_${this.state.room_type}`).value;
        // 建立訂房明細
        let booking = [];
        const available_array = this.props.available.data;
        for(let n=0; n<this.state.nights; n++){
            const room_nos = available_array[n].available_rooms;
            const date = available_array[n].date;
            for(let q=0; q<this.state.quantity; q++){                    
                let bid = `${date}_${room_nos[q]}`;
                booking.push(bid);
            }
        }
        let booking_data = this.state;
        booking_data["booking"] = booking;
        booking_data["amount"] = parseInt(amount);
        console.log(booking_data);
        createNewOrder(booking_data).then(resp=>{
            // console.log(resp)
            if(resp.ok){
                location.href = `${window.origin}/bill?oid=${resp.oid}`
            }
        })
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
