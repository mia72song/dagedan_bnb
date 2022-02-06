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
        captcha:"",
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
            <form className="booking_form" onSubmit={this.handelSubmit}>
                <div class="row g-0">
                    <div class="col-12 col-md-5 my-3">
                        <div class="booking_detail">
                            <h6 class="mb-3 text-center">- 訂房明細 -</h6>
                            <p class="my-3">期間：{this.state.check_in_date} ~ {this.state.check_out_date}，共 {this.state.nights} 晚</p>
                            <p>房型：
                                {this.props.info.name} * 
                                <input type="number" value={this.state.quantity} min="1" max={Math.min(this.state.num_of_guests, this.props.available.min_quantity)} 
                                class="form-control form-control-sm form-control-inline"
                                onChange={this.handleChange("quantity")}/>
                                間
                            </p>
                            <p>人數：
                                <input type="number" value={this.state.num_of_guests} min="1" max={this.props.info.accommodate} 
                                class="form-control form-control-sm form-control-inline"
                                onChange={this.handleChange("num_of_guests")}/>
                                人
                            </p>
                            <p>總金額：新台幣
                                <input type="text" disabled="true" readOnly="true" class="form-control form-control-inline"
                                value={this.updateAmount(this.state.quantity, this.state.num_of_guests)} 
                                id={`total_amount_${this.state.room_type}`}/>
                                元    
                            </p>
                        </div>
                    </div>
                    <div class="col-12 col-md-1 arrow_img_div">
                        <img src="/static/images/right.png" class="mx-auto d-block"alt=""/>
                    </div>
                    <div class="col-12 col-md-6 my-3">
                        <div class="booker_info mx-auto px-1 px-sm-auto">
                            <h6 class="mb-3 text-center">- 訂房人資料 -</h6>
                            <div class="row g-0 align-items-center">
                                <div class="col-auto">
                                    <label for="booker_name" class="col-form-label">訂房全名：</label>
                                </div>
                                <div class="col-auto col-input-text">
                                    <input type="text" id="booker_name" value={this.state.name} onChange={this.handleChange("name")}
                                    class="form-control form-control-sm" pattern="^[\u4e00-\u9fa5]+$|^[a-zA-Z\s]+$" required/>
                                </div>
                                <div class="col-6 col-sm-auto radio_container">
                                    <div class="form-check form-check-inline my-auto">
                                        <input class="form-check-input" type="radio" name="booker_gender" id="male" value="male" 
                                        checked={this.state.gender==="male"} onChange={this.handelGenderCheck("male")}/>
                                        <label class="form-check-label" for="male">先生</label>
                                    </div>
                                    <div class="form-check form-check-inline my-auto">
                                        <input class="form-check-input" type="radio" name="booker_gender" id="female" value="female"
                                        checked={this.state.gender==="female"} onChange={this.handelGenderCheck("female")}/>
                                        <label class="form-check-label" for="female">小姐</label>
                                    </div>
                                </div>
                            </div>
                            <div class="row g-0 align-items-center">
                                <div class="col-auto">
                                    <label for="booker_phone" class="col-form-label">聯絡手機：</label>
                                </div>
                                <div class="col-auto col-input-text">
                                    <input type="tel" minlength="10" maxlength="20" id="booker_phone" value={this.state.phone} onChange={this.handleChange("phone")} 
                                    class="form-control form-control-sm" required/>
                                </div>
                                <div class="col-5">
                                </div>
                            </div>
                            <div class="row g-0 align-items-center">
                                <div class="col-auto">
                                    <label for="booker_email" class="col-form-label">電子信箱：</label>
                                </div>
                                <div class="col-auto">
                                    <input type="email" id="booker_email" class="form-control form-control-sm col-input-longtext" 
                                    value={this.state.email} onChange={this.handelEmailChange} required/>
                                </div>
                            </div>
                            <div class="row g-0 align-items-center">
                                <div class="col-auto">
                                    <label for="captcha" class="col-form-label">信箱驗證：</label>
                                </div>
                                <div class="col-auto col-input-text">
                                    <input type="text" id="captcha" value={this.state.captcha} onChange={this.handleChange("captcha")} 
                                    class="form-control form-control-sm" required/>
                                </div>
                                <div class="col-4 px-2">
                                    <button type="button" class="btn btn-sm btn-outline-secondary" id="send_captcha_btn"
                                    disabled onClick={this.sendCaptcha}>發送驗證碼</button>
                                </div>
                            </div>
                            <div class="row g-0 align-items-center">
                                <div class="col-auto">
                                    <label for="arrival_datetime" class="col-form-label">預計抵達：</label>
                                </div>
                                <div class="col-auto">
                                    <input type="datetime-local" id="arrival_datetime" class="form-control form-control-sm col-input-longtext"
                                    min={`${this.state.check_in_date}T15:00`} max={`${this.state.check_in_date}T21:00`} 
                                    value={this.state.arrival_datetime} onChange={this.handleChange("arrival_datetime")} />
                                </div>
                            </div>
                            <input type="submit" class="btn btn-outline-primary mt-2" value="確認訂房"
                            disabled={(this.state.name===""||this.state.phone===""||this.state.email===""||this.state.captcha==="")}/>
                        </div>
                    </div>
                </div>
            </form>
        )
    }
    //房價結算
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
    //訂房人性別切換
    handelGenderCheck=(gender)=>{
        return()=>{
            this.setState({gender})
        }
    }
    //訂房人EMail輸入及驗證，驗證通過則「發送驗證碼」按鍵有效，否則無效(disabled)
    handelEmailChange=(eObj)=>{
        const pattern = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;
        let email = eObj.target.value;
        this.setState({email});
        if(email.match(pattern)){
            document.getElementById("send_captcha_btn").removeAttribute("disabled");
        }else{
            document.getElementById("send_captcha_btn").setAttribute("disabled", "true");
        }
    }
    //發送驗證碼
    sendCaptcha=()=>{
        
    }
    //其他資料欄位輸入
    handleChange=(dataType)=>{
        return(eObj)=>{
            let value = (
                (dataType==="num_of_guests" || dataType==="quantity")? 
                parseInt(eObj.target.value) : eObj.target.value
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
    //發送訂房資料
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
        // console.log(booking_data);
        createNewOrder(booking_data).then(resp=>{
            // console.log(resp)
            if(resp.ok){
                location.href = `${window.origin}/bill?oid=${resp.oid}`
            }
        })
    }
}