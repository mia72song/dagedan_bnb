function createNewPayment(oid, data){
    const url = `${window.origin}/auth/payment/${parseInt(oid)}`;
    let p=fetch(url, {
        method: "post",
        credentials: "include",
        headers: {
            "Content-Type":"application/json",
            "Authorization": `Bearer ${localStorage.getItem("jwt")}`
        },
        body: JSON.stringify(data)
    }).then(response=>{
        if(response.status===200){
            return response.json()
        }else if(response.status===403){
            handleLogout()
        }else{
            console.log(response.json())
        }
    })
    return p
}

function updatePayment(pid, data){
    const url = `${window.origin}/auth/payment/${pid}`;
    let p=fetch(url, {
        method: "put",
        credentials: "include",
        headers: {
            "Content-Type":"application/json",
            "Authorization": `Bearer ${localStorage.getItem("jwt")}`
        },
        body: JSON.stringify(data)
    }).then(response=>{
        if(response.status===200){
            return response.json()
        }else if(response.status===403){
            handleLogout()
        }else{
            console.log(response.json())
        }
    })
    return p
}

function getPayment(pid){
    const url = `${window.origin}/auth/payment/${pid}`;
    let p = fetch(url).then(response=>{
        if(response.status===200){
            return response.json()
        }else if(response.status===401){
            handleLogout()
        }else{
            console.log(response.json())
        }
    })
    return p
}