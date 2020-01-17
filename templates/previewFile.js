 function previewFile(sel) {
 var preview = document.querySelector('#inp-' + sel);
var file    = document.querySelector('#'+sel).files[0];

var reader  = new FileReader();
reader.addEventListener("load", function () {
 preview.src = reader.result;
 }, false);
if (file) {
 reader.readAsDataURL(file);
 }
}