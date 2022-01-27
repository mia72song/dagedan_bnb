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

function createNewPayment(oid, data){
    let p = fetch(`${window.origin}/api/payment/${oid}`, {
        method: "post", 
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }).then(response=>{
        if(response.status!==500){
            return response.json()
        }else{
            console.log(response.json())
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
            <form action="" onSubmit={this.handleSubmit}>
                <p>訂單編號：
                    <input type="text" disabled="true" readOnly="true" value={this.props.oid} required/>
                </p>
                <p>匯款銀行：
                    <input type="text" value={this.state.bank} onChange={this.handleChange("bank")} pattern="^[\u4e00-\u9fa5]+$|^[a-zA-Z\s]+$" required/>
                </p>
                <p>帳號(末五碼)：
                    <input type="text" value={this.state.account_no} onChange={this.handleChange("account_no")} minlength="5" maxlength="20" pattern="\d*" required/>
                </p>
                <p>戶名：
                    <input type="text" value={this.state.account_name} onChange={this.handleChange("account_name")} pattern="^[\u4e00-\u9fa5]+$|^[a-zA-Z\s]+$" required/>
                </p>
                <p>金額：
                    <input type="text" value={this.state.amount} onChange={this.handleChange("amount")} pattern="\d*" required/>
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
            if(dataType!=="amount"){
                this.setState({[dataType]: eObj.target.value})
            }else{
                let value = (
                    (eObj.target.value==="" || !parseInt(eObj.target.value)) ? 0 : parseInt(eObj.target.value)
                );
                this.setState({[dataType]: value})
            }
        })
    }
    handleSubmit=(eObj)=>{
        eObj.preventDefault();
        let post_data = {}
        if(this.state.amount>0){
            post_data = this.state;
            post_data["oid"] = this.props.oid;
            createNewPayment(this.props.oid, post_data).then(resp=>{
                if(resp.ok){
                    alert("提交成功!!民宿將於24小時內確認後，以電話及EMail通知");
                    location.href = "/";
                }else if(resp.error){
                    alert("提交付款資料失敗，請電洽089-771551確認")
                }
            })
        }
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