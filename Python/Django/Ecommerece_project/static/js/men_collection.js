console.log("Ajax implementaion in our E-commerce Project");

url = '/shop/men_collection/';

let lnk = document.getElementById('men_collection')
lnk.addEventListener('click' , btnhandler)

function btnhandler()
{
	console.log("You have clicked on this link");
	const xhr  = new XMLHttpRequest();
	xhr.open("GET" , url,true);

	xhr.onprogress = function()
	{

		console.log('On Progress');

	}

	xhr.onload = function()
	{
		console.log(this.responseText);
	}

	
	xhr.send();

}