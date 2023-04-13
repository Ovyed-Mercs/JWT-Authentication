const getState = ({ getStore, getActions, setStore }) => {
	let apiUrl=process.env.BACKEND_URL
	return {
		store: {},
		actions: {
			signin:()=>{
				let requestOptions = {
					method: 'POST',
					headers: {"Content-Type": "application/json"},
					body: {email:"email",
					password:"password"},
				  };
				  
				  fetch(apiUrl+"/api/login", requestOptions)
					.then(response => response.text())
					.then(result => console.log(result))
					.catch(error => console.log('error', error));
			},
			access_private: ()=>{
				let requestOptions = {
				method: 'GET',
				headers: {
					"Authorization": "Bearer "+localStorage.getItem("token"),
					"Content-Type": "application/json"
				}};

				fetch(apiUrl+"/api/private", requestOptions)
				.then(response => response.json())
				.then(result => console.log(result))
				.catch(error => console.log('error', error));
			}
		}
	};
};

export default getState;
