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
        document.querySelectorAll("button[id^='captcha_btn_']").forEach(btn=>{
            btn.setAttribute("disabled", "true");
        })
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
        const max_quantity = Math.min(Math.min(this.state.num_of_guests, this.props.available.min_quantity));
        const quantity_options = [];
        for(let i=1; i<=max_quantity; i++){
            quantity_options.push(
                <option value={i}>{i}</option>
            )
        }
        const num_of_guests_options = [];
        for(let i=1; i<=this.props.info.accommodate; i++){
            num_of_guests_options.push(
                <option value={i}>{i}</option>
            )
        }
        return(
            <form className="booking_form" onSubmit={this.handelSubmit}>
                <div className="row g-0">
                    <div className="col-12 col-md-5 my-3">
                        <div className="booking_detail">
                            <h6 className="mb-4 text-center">- 訂房明細 -</h6>
                            <p className="mb-3">期間：{this.state.check_in_date} ~ {this.state.check_out_date}，共 {this.state.nights} 晚</p>
                            <div className="row g-0 align-items-center my-2">
                                <div className="col-auto">
                                房型：{this.props.info.name} * 
                                </div>
                                <div className="col-2 mx-2">
                                    <select className="form-select form-select-sm form-control-inline" value={this.state.quantity} onChange={this.handleChange("quantity")}>
                                        { quantity_options }
                                    </select>
                                </div>
                                <div className="col-auto">間</div>
                            </div>
                            <div className="row g-0 align-items-center my-2">
                                <div className="col-auto">
                                人數：
                                </div>
                                <div className="col-2 mx-2">
                                    <select className="form-select form-select-sm form-control-inline" value={Math.min(this.state.num_of_guests, this.props.info.accommodate)} onChange={this.handleChange("num_of_guests")}>
                                        { num_of_guests_options }
                                    </select>
                                </div>
                                <div className="col-auto">人</div>
                            </div>
                            <div className="row g-0 align-items-center my-2">
                                <div className="col-auto">
                                總金額：新台幣
                                </div>
                                <div className="col-4 mx-1">
                                    <input type="text" disabled="true" readOnly="true" className="form-control form-control-inline"
                                    value={this.updateAmount(this.state.quantity, this.state.num_of_guests)} 
                                    id={`total_amount_${this.state.room_type}`}/>
                                </div>
                                <div className="col-auto">元</div>
                            </div>
                        </div>
                    </div>
                    <div className="col-12 col-md-1 my-3 arrow_img_div">
                        <img src="/static/images/right.png" className="mx-auto d-block"alt=""/>
                    </div>
                    <div className="col-12 col-md-6 my-3">
                        <div className="booker_info">
                            <h6 className="text-center mb-3">- 訂房人資料 -</h6>
                            <div className="d-flex align-items-center flex-wrap">
                                <div className="">
                                    <label for="booker_name" className="col-form-label">訂房全名：</label>
                                </div>
                                <div className="col-input-text">
                                    <input type="text" id="booker_name" value={this.state.name} onChange={this.handleChange("name")}
                                    className="form-control form-control-sm" pattern="^[\u4e00-\u9fa5]+$|^[a-zA-Z\s]+$" required/>
                                </div>
                                <div className="mx-3 radio_container">
                                    <div className="form-check form-check-inline">
                                        <input className="form-check-input my-2" type="radio" name="booker_gender" id="male" value="male" 
                                        checked={this.state.gender==="male"} onChange={this.handelGenderCheck("male")}/>
                                        <label className="form-check-label" for="male">先生</label>
                                    </div>
                                    <div className="form-check form-check-inline">
                                        <input className="form-check-input my-2" type="radio" name="booker_gender" id="female" value="female"
                                        checked={this.state.gender==="female"} onChange={this.handelGenderCheck("female")}/>
                                        <label className="form-check-label" for="female">小姐</label>
                                    </div>
                                </div>
                            </div>
                            <div className="d-flex align-items-center">
                                <div className="">
                                    <label for="booker_phone" className="col-form-label">聯絡手機：</label>
                                </div>
                                <div className="col-input-text">
                                    <input type="tel" minlength="10" maxlength="20" id="booker_phone" value={this.state.phone} onChange={this.handleChange("phone")} 
                                    className="form-control form-control-sm" required/>
                                </div>
                                <div className="">
                                </div>
                            </div>
                            <div className="d-flex align-items-center">
                                <div className="">
                                    <label for="booker_email" className="col-form-label">電子信箱：</label>
                                </div>
                                <div className="">
                                    <input type="email" id="booker_email" className="form-control form-control-sm col-input-longtext" 
                                    value={this.state.email} onChange={this.handelEmailChange} placeholder="請輸入EMail" required/>
                                </div>
                            </div>
                            <div className="d-flex align-items-center">
                                <div className="">
                                    <label for="captcha" className="col-form-label">信箱驗證：</label>
                                </div>
                                <div className="col-input-text">
                                    <input type="text" id="captcha" value={this.state.captcha} onChange={this.handleChange("captcha")} 
                                    className="form-control form-control-sm" placeholder="請輸入驗證碼" required/>
                                </div>
                                <div className="mx-2">
                                    <button type="button" className="btn btn-sm btn-outline-secondary" id={`captcha_btn_${this.props.available.room_type}`}
                                    onClick={this.sendCaptcha}>發送驗證碼</button>
                                </div>
                            </div>
                            <div className="d-flex align-items-center">
                                <div className="">
                                    <label for="arrival_datetime" className="col-form-label">預計抵達：</label>
                                </div>
                                <div className="">
                                    <input type="datetime-local" id="arrival_datetime" className="form-control form-control-sm col-input-longtext"
                                    min={`${this.state.check_in_date}T15:00`} max={`${this.state.check_in_date}T21:00`} 
                                    value={this.state.arrival_datetime} onChange={this.handleChange("arrival_datetime")} />
                                </div>
                            </div>
                            <input type="submit" className="btn btn-outline-primary mt-2" value="確認訂房"
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
            document.getElementById(`captcha_btn_${this.props.available.room_type}`).removeAttribute("disabled");
        }else{
            document.getElementById(`captcha_btn_${this.props.available.room_type}`).setAttribute("disabled", "true");
        }
    }
    //發送驗證碼
    sendCaptcha=()=>{
        const url = `${window.origin}/api/captcha?email=${this.state.email}`;
        fetch(url).then(response=>{
            const resp = response.json();
            if(response.status===200){
                alert("驗證碼已發送")
            }else if(response.status===400){
                alert("驗證碼發送失敗，原因：信箱錯誤")
            }else{
                console.log(resp);
            }
        })
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
        const today = new Date();
        const check_in_date = new Date(this.state.check_in_date);
        if(today>=check_in_date){
            return
        }
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