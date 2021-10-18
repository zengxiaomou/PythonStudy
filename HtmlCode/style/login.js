function check_code() {
  console.log("打印 ");
  var code =document.getElementById('username').value;
  console.log(code)
  var reg=/^[0-9A-Za-z]{6,10}$/;
  var span= document.getElementById('span_user');
  if(reg.test(code)){
    span.className='ok';
  }else {
      span.className='error';
  }

}