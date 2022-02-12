document.querySelectorAll("button[id^='get_payment_btn_']").forEach(btn=>{
    btn.addEventListener("click", getPaymentByOid);
})

function getPaymentByOid(eObj){
    //console.log(csrf_token);
    const oid = eObj.target.id.split("_")[3];
    const payment_div = document.getElementById(`payment_${oid}`);

    if(payment_div.style.display==="block"){
        return
    }

    document.querySelectorAll("div[id^='payment_']").forEach(div=>{
        div.style.display = "none";
    });
    
    fetch(`${window.origin}/admin/api/payment/${oid}`).then(response=>{
        if(response.status==200){
            return response.json()
        }else{
            console.log(response.json());
        }
    }).then(resp=>{
        payment_div.style.display = "block";
        ReactDOM.render(<PaymentForm data={resp.data} oid={oid}/>, payment_div);
    })
}

class PaymentForm extends React.Component{
    state = {
        bank: "", // 銀行
        account_no: "", //帳號至先五碼
        name: "", // 戶名
        amount: "",
        transfer_date: ""
    }
    labels = {
        bank: "匯款銀行", 
        account_no: "帳號末五碼", 
        name: "匯款戶名", 
        amount: "金額",
        transfer_date: "匯款日期"
    }
    componentDidMount(){
        if(this.props.data){
            this.setState({
                bank: this.props.data.bank,
                account_no: this.props.data.account_no,
                name: this.props.data.name,
                amount: this.props.data.amount,
                transfer_date: this.props.data.transfer_date
            })
        }
    }
    render(){
        //console.log(this.state);
        let form_content = []
        Object.keys(this.labels).forEach(col=>{
            
        })
        return(
            <form className="mx-auto fs-6" id={`payment_form_${this.props.oid}`}>
                This is PaymentForm
            </form>
        )
    }
}