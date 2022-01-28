class Bill extends React.Component{
    render(){
        return(
            <div>
                <h4>您已完成訂房，請按下列資訊在期限內進行付款：</h4>
                <table>
                    <tr>
                        <th>訂單編號</th>
                        <td>{this.props.oid}</td>
                    </tr>
                    <tr>
                        <th>收款帳戶</th>
                        <td>
                            <p>玉山銀行(808) 中山分行</p>
                            <p>帳號：0417-968-052086</p>
                            <p>戶名：林志豪</p> 
                        </td>
                    </tr>
                    <tr>
                        <th>金　　額</th>
                        <td>新台幣 {parseInt(this.props.data.amount)} 元</td>
                    </tr>
                    <tr>
                        <th>付款期限</th>
                        <td>{this.props.data.deadline}</td>
                    </tr>
                </table>
                <p className="reminder">*** 於付款期限內，完成匯款後，請來電089-771551確認，確保您的訂房權益。 ***</p>
            </div>
        )
    }
}
const search_string = location.search.split("?")[1].split("=");
const oid = (search_string[0]==="oid" && search_string[1]);
if(oid){
    getOrderByOid(oid).then(resp=>{
        if(resp.ok){
            ReactDOM.render(<Bill oid={oid} data={resp.data}/>, document.getElementById("bill_wrap"));
        }else if(resp.error){
            console.log(`${resp.message}:${oid}`)
        }
    })
}