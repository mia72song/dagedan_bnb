class KeywordSearch extends React.Component{
    state = {
        select: "", 
        keyword: ""
    }
    componentDidMount(){
        if(location.pathname.split("/")[3]==="search"){
            const search_string = location.search.replace("?", "").split(/[=&]/);
            if(search_string.indexOf("id")>=0){
                this.setState({
                    select: "id", 
                    keyword: search_string[search_string.indexOf("id")+1]
                })
            }else if(search_string.indexOf("phone")>=0){
                this.setState({
                    select: "phone", 
                    keyword: search_string[search_string.indexOf("phone")+1]
                })

            }else if(search_string.indexOf("checkin")>=0){
                this.setState({
                    select: "checkin", 
                    keyword: search_string[search_string.indexOf("checkin")+1]
                })
            }
        }
    }
    render(){
        return(
            <div class="input-group mt-3">
                <select class="form-select" id="inputGroupSelect" value={this.state.select} onChange={this.handleChange("select")}>
                    <option value="">請選取搜尋項目</option>
                    <option value="id">訂單編號</option>
                    <option value="phone">訂房電話</option>
                    <option value="checkin">入住日期</option>
                </select>
                <input type={this.state.select==="checkin"? "date" : "text"} class="form-control" name="keyword" id="keywordInput" 
                value={this.state.keyword} onChange={this.handleChange("keyword")} placeholder="請輸入關鍵字" />
                <button class="btn btn-outline-secondary fw-bold" type="button" onClick={this.handleSearch}>搜尋</button>
            </div>
        )
    }
    handleChange=(dataType)=>{
        return(eObj=>{
            this.setState({[dataType]: eObj.target.value})
        })
    }
    handleSearch=()=>{
        location.href = `/admin/orders/search?${this.state.select}=${this.state.keyword}`;
    }
}
ReactDOM.render(<KeywordSearch />, document.getElementById("group_selector"));