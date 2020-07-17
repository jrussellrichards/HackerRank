function stripProperty(obj, prop) {
    var clone = {}
  for (let key in obj) {
    if(key!=prop){
        clone[obj] = obj[key];

    }  

  return clone;
}}


var objeto = {
    nombre : 'goku',
    apellido: 'kakaroto',
    edad:18
}


stripProperty(obj,'edad')
