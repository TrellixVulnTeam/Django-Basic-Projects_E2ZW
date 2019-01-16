function saveData() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 2 && this.status == 400){
            document.getElementById('').innerHTML = this.responseText;
        }
    }
    xhttp.open("POST","",true);
    xhttp.send();
}