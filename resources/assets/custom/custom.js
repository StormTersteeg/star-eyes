$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function encrypt() {
  var data = document.getElementById("data_encrypt").value
  var key = document.getElementById("key_e").value

  pywebview.api.encrypt(data, key).then(function(result) {
    document.getElementById("result_encrypt").innerHTML = result
  })
}

function decrypt() {
  var data = document.getElementById("data_decrypt").value
  var key = document.getElementById("key_d").value

  pywebview.api.decrypt(data, key).then(function(result) {
    document.getElementById("result_decrypt").innerHTML = result
  })
}