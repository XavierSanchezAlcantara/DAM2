
    function randomDate(){
      var valor= Math.floor(Math.random() * (366 - 1)) + 1;
      if (valor>=1&&valor<=31) {
        mes="enero";
      }else if(valor>=32&&valor<=59){
        mes="febrero";
      }else if (valor>=60&&valor<=90) {
        mes="marzo";     
      }else if (valor>=91&&valor<=120) {
        mes="abril";
      }else if (valor>=121&&valor<=151) {
        mes="mayo";
      }else if (valor>=152&&valor<=181) {
        mes="junio";
      }else{
        mes="asda";
      }
     window.alert(mes);   
     alert(mes);
    }

