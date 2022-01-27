class Search extends React.Component{
    state={
        check_in_date: "",
        check_out_date: "",
        guests: 1
    }
    componentDidMount(){
        if(location.search){
            const search_string_1st = location.search.split("&")[0].split("?")[1].split("=");
            const search_string_2nd = location.search.split("&")[1].split("=");
            const search_string_3th = location.search.split("&")[2].split("=");
            this.setState({
                check_in_date: (search_string_1st[0]==="checkin" && search_string_1st[1]),
                check_out_date: (search_string_2nd[0]==="checkout" && search_string_2nd[1]),
                guests: (search_string_3th[0]==="guests" && search_string_3th[1])
            })
        }else{
            this.setState({
                check_in_date: dateIndexToString(1),
                check_out_date: dateIndexToString(2)
            })
        }
    }
    render(){
        const check_in_index = dateStringToIndex(this.state.check_in_date);
        return(
            <div id="available_search">
                <div className="check_in_date_div">
                    <p>入住日期</p>
                    <input type="date" name="check_in_date" id="check_in_date" min={dateIndexToString(1)} max={dateIndexToString(12*7)}
                        value={this.state.check_in_date} onChange={this.handleChange("check_in_date")}/>
                </div>
                <div className="check_out_date_div">
                    <p>退房日期</p>
                    <input type="date" name="check_out_date" id="check_out_date" min={dateIndexToString(check_in_index+1)} max={dateIndexToString(12*7+1)}
                        value={this.state.check_out_date} onChange={this.handleChange("check_out_date")}/>
                </div>
                <div className="num_of_guests_div">
                    <p>住宿人數</p>
                    <input type="number" name="guests" id="guests" min="1" max="99" 
                        value={this.state.guests} onChange={this.handleChange("guests")}/>
                </div>
                <div className="submit_div">
                    <button type="submit" onClick={this.handleSubmit}>查詢空房</button>
                </div>
            </div>
        )
    }
    handleChange=(dataType)=>{         
        return (eObj)=>{
            if(dataType==="check_in_date"){
                const check_in_date = eObj.target.value;
                const check_in_index = dateStringToIndex(check_in_date);
                const check_out_date = dateIndexToString(check_in_index+1);
                this.setState({
                    check_in_date,
                    check_out_date
                })
            }else{
                this.setState({[dataType]: eObj.target.value})
            }
        }
    }
    handleSubmit=()=>{
        const {check_in_date, check_out_date, guests} = this.state
        if(dateStringToIndex(check_out_date)>dateStringToIndex(check_in_date)){
            let search_string = "checkin="+check_in_date+"&checkout="+check_out_date+"&guests="+guests
            location.href = `${window.origin}/booking?${search_string}`
        }else{
            alert("退房日期必須晚於入住日期")
            return
        }
    }
}

ReactDOM.render(<Search />, document.getElementById("search_wrap"));