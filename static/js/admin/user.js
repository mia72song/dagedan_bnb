function userRequest(method, data=null){
    const url = `${window.origin}/auth/user`;
    let body;
    if(data){
        body=JSON.stringify(data)
    };
    let p=fetch(url, {
        method,
        credentials:"include",
        headers:{
            "Content-Type":"application/json"
        },
        body
    }).then(response=>{
        if(response.status!==500){
            return response.json()
        }else{
            console.log(response.json())
        }
    })
    return p
}