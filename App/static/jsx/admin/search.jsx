class KeywordSearch extends React.Component{
    render(){
        return(
            <div class="input-group mt-3">
                <select class="form-select" id="inputGroupSelect">
                    <option selected>請選取搜尋項目</option>
                    <option value="order_id">訂單編號</option>
                    <option value="phone">訂房電話</option>
                    <option value="check_in_date">入住日期</option>
                </select>
                <input type="text" class="form-control" name="keyword" id="keyword" placeholder="請輸入關鍵字" />
                <button class="btn btn-outline-primary" type="button">搜尋</button>
            </div>
        )
    }
}
ReactDOM.render(<KeywordSearch />, document.getElementById("group_selector"));