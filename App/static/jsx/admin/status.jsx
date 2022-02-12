class StatusSelect extends React.Component{
    state = {
        order_status: "new"
    }
    componentDidMount(){
        if(location.pathname.split("/")[3] && location.pathname.split("/")[3]!=="search"){
            this.setState({order_status: location.pathname.split("/")[3]});
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
            location.href = "/admin/orders";
        }else{
            location.href = `/admin/orders/${eObj.target.value}`;
        }
    }
}
ReactDOM.render(<StatusSelect />, document.getElementById("status_selector"));