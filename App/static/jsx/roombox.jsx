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
        let best_price;
        if(this.state){
            best_price = (this.state.data[0].is_holiday ? this.props.info.rate_holiday: this.props.info.rate_weekday)
        }
        return(
            <div>
                {this.state && (
                    <div className="card mt-3">
                        <div className="row g-0">
                            <div className="col-md-4">
                                <img src={this.props.info.images && this.props.info.images[0]} class="img-fluid rounded-start w-100" alt="..."/>
                            </div>
                            <div className="col-md-8">
                                <div className="card-body">
                                    <h4 className="card-title" id={`Book_${this.props.type}`}>
                                        {this.props.info.name}
                                        <span className="badge bg-secondary mx-3">適用{this.props.info.accommodate}人</span>
                                    </h4>
                                    <p className="card-text room_description">{this.props.info.description}</p>
                                    <p className="card-subtitle my-2 text-secondary">
                                        優惠方案：
                                        <span>單人入住 {this.props.info.single_discount*100} 折</span>
                                    </p>
                                </div>
                                <div className="card-body row text-center">
                                    <div className="col-7" id="price">
                                        <h1 className="card-subtitle">
                                            <span>NT </span>
                                            { comma(best_price) }
                                            { best_price<this.props.info.rate_holiday && <span> UP</span> }
                                        </h1>
                                    </div>
                                    <div className="col-5">
                                        <a href={`#Book_${this.props.type}`} className="btn btn-dark book_now_btn" onClick={this.handleBookingForm}>Book Now</a>
                                        <p className="card-text">
                                            {
                                            this.state.min_quantity<=2 && 
                                            <small className="text-secondary">最後{this.state.min_quantity}間</small>
                                            }                                            
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
                {this.state && (
                    <div id={`booking_detail_${this.props.type}`} className="px-1 px-md-3">
                        {"<!--由/static/jsx/roombox.jsx渲染-->"}
                    </div>
                )}
            </div>
        )
    }
    //打開訂房表單
    handleBookingForm=()=>{
        document.querySelectorAll("div[id^='booking_detail_']").forEach(div=>{
            div.style.display="";
        })
        let booking_form = document.getElementById(`booking_detail_${this.props.type}`);
        if(booking_form.style.display===""){
            booking_form.style.display="block";
            ReactDOM.render(<BookingForm info={this.props.info} available={this.state}/>, booking_form);
        }
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
