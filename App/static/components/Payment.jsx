function getPaymentByOid(oid){
    let p = fetch(`${window.origin}/api/payment/${oid}`).then(response=>{
        if(response.status===500){
            console.log(response.json())
        }else{
            return response.json()
        }
    })
    return p
}

class Payment extends React.Component{
    state = {
        bank: "",
        account_no: "",
        account_name: "",
        amount: "",
        transfer_date: ""
    }
    render(){
        return(
            <form action="">
                <p>訂單編號：
                    <input type="text" disabled="true" readOnly="true" value={this.props.oid} required/>
                </p>
                <p>匯款銀行：
                    <input type="text" value={this.state.bank} onChange={this.handleChange("bank")} required/>
                </p>
                <p>帳號(末五碼)：
                    <input type="text" value={this.state.account_no} onChange={this.handleChange("account_no")} required/>
                </p>
                <p>戶名：
                    <input type="text" value={this.state.account_name} onChange={this.handleChange("account_name")} required/>
                </p>
                <p>金額：
                    <input type="text" value={this.state.amount} onChange={this.handleChange("amount")} required/>
                </p>
                <p>匯款日期：
                    <input type="date" value={this.state.transfer_date} onChange={this.handleChange("transfer_date")} required/>
                </p>
                <p/>
                <input type="submit" value="提交" /> 
            </form>
        )
    }
    handleChange=(dataType)=>{
        return(eObj=>{
            this.setState({[dataType]: eObj.target.value})
        })
    }
}

const search_string = window.location.search.split("?")[1].split("=");
const oid = (search_string[0]==="oid" && search_string[1]);
if(oid){
    getPaymentByOid(oid).then(resp=>{
        if(resp.ok){
            ReactDOM.render(<Payment oid={oid}/>, document.getElementById("payment_wrap"));
        }else if(resp.expired){
            alert("此連結已逾期失效，請電洽089-771551確認");
            location.href = "/";
        }else{
            console.log(resp.message);
        }
    })
}

