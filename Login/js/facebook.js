 window.fbAsyncInit = function() {
  FB.init({
    appId      : '802031603226333',
    cookie     : true,  
                        
    xfbml      : true,  
    version    : 'v2.2' 
  });
};
(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
function start(){
 FB.getLoginStatus(function(response){
  if(response.status==='connected')
   login();
 });
}
function login(){
 console.log("CONNECTED\n");
 FB.api('/me',function(response){
 console.log(JSON.stringify(response));
 $.post("login.php",{
		username:response.id,
		firstname:response.first_name,
		lastname:response.last_name,
		email:response.email
		},function(data,status){if(status==='success')
                                  window.location="../dashboard.php";					
					});
 });
}
function FBlogin(){
 FB.login(function(response){
 if(response.status==='connected')
  login();
   },{scope: 'public_profile,email'});
  }
