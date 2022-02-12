class StatusSelect extends React.Component{
    state = {
        order_status: "new"
    }
    componentDidMount(){
        if(location.search.includes("status")){
            const search_string = location.search.replace("?", "").split(/[=&]/);
            const index = search_string.indexOf("status")+1;
            this.setState({order_status: search_string[index]});
        }else{
            this.setState({order_status: "all"});
        }
    }
    render(){
        return(
            <div className="input-group mt-3 justify-content-end">
                <label className="input-group-text bg-secondary text-white fst-normal" for="inputStatusSelect">訂單狀態</label>
                <select className="form-select" id="inputStatusSelect" value={this.state.order_status} onChange={this.handleSelect}>
                    <option value="all">全部訂單</option>
                    <option value="new">新訂單</option>
                    <option value="pending">待確認</option>
                    <option value="paid">已付款</option>
                </select>
            </div>
        )
    }
    handleSelect=(eObj)=>{
        //console.log(eObj.target.value);
        if(eObj.target.value==="all"){
            location.href = "/admin/order";
        }else{
            location.href = `/admin/order?status=${eObj.target.value}`;
        }
    }
}
ReactDOM.render(<StatusSelect />, document.getElementById("status_selector"));