class Search extends React.Component{
    state = {
        check_in_date: "",
        check_out_date: "",
        guests: 1
    }
    componentDidMount(){
        if(location.pathname==="/booking" && location.search){
            const search_string_1st = location.search.split("&")[0].split("?")[1].split("=");
            const search_string_2nd = location.search.split("&")[1].split("=");
            const search_string_3th = location.search.split("&")[2].split("=");
            const available_search_btn = document.getElementById("available_search_btn");
            //console.log(available_search_btn);
            available_search_btn.classList.remove("btn-search");
            available_search_btn.classList.add("btn-dark");
            
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
        const max_accommodate = 8;
        let select_items = [];
        for(let i=1; i<=max_accommodate; i++){
            select_items.push(
                <option value={i}>{i}</option>
            )
        }
        return(
            <form className="row g-1 w-95" onSubmit={this.handleSubmit}>
                <div className="col-6 col-md-4 px-1 mt-1">
                    <label for="inputCheckIn" className="form-label">入住日期</label>
                    <input type="date" className="form-control form-control-sm" id="inputCheckIn" min={dateIndexToString(1)} max={dateIndexToString(12*7)} 
                        value={this.state.check_in_date} onChange={this.handleChange("check_in_date")}/>
                </div>
                <div className="col-6 col-md-4 px-1 mt-1">
                    <label for="inputCheckOut" className="form-label">退房日期</label>
                    <input type="date" className="form-control form-control-sm" id="inputCheckOut" min={dateIndexToString(check_in_index+1)} max={dateIndexToString(12*7+1)}
                        value={this.state.check_out_date} onChange={this.handleChange("check_out_date")}/>
                </div>
                <div className="col-6 col-md-2 px-1 mt-1">
                    <label for="inputNum" className="form-label">住宿人數</label>
                    <select className="form-select form-select-sm" value={this.state.guests} onChange={this.handleChange("guests")}>
                        { select_items }
                    </select>
                </div>
                <div className="col-6 col-md-2 px-1 mt-2 mt-md-1">
                    <button type="submit" className="btn btn-sm btn-search px-0 h-100 w-100" id="available_search_btn">查詢空房</button>
                </div>
            </form>
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
    handleSubmit=(eObj)=>{
        eObj.preventDefault();
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