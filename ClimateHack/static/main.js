document.addEventListener('load',() => {
    var x = document.getElementById('submitgroup').style.width;
    document.getElementById('bobo').style.width = x;
})

function submit() {

    btn.classList.add("loading"); // Loading effect

    // const form = document.getElementById("form");

    // form.addEventListener("submit", function(event) {
    //     let isValid = true; 

    //     var carbonate = document.getElementById("carbonate").value.trim();
    //     var carbon = document.getElementById("carbon").value.trim();
    //     var region = document.getElementById("region").value.trim();
    //     var latitude = document.getElementById("latitude").value.trim();
    //     var longitude = document.getElementById("longitude").value.trim();
    //     var pH = document.getElementById("pH").value.trim();
    //     let btn = document.getElementById("submitgroup");

       
    //     if (carbonate === "") {
    //         alert("Please enter the amount of carbonate!");
    //         isValid = false;
    //     }
    //     if (carbon === "") {
    //         alert("Please enter the amount of carbon!");
    //         isValid = false;
    //     }
    //     if (region === "") {
    //         alert("Please enter the climate!");
    //         isValid = false;
    //     }
    //     if (latitude === "") {
    //         alert("Please enter the latitude!");
    //         isValid = false;
    //     }
    //     if (longitude === "") {
    //         alert("Please enter the longitude!");
    //         isValid = false;
    //     }
    //     if (pH === "") {
    //         alert("Please enter the pH!");
    //         isValid = false;
    //     }


    //     if (!isValid) {
    //         event.preventDefault();
            
    //     } 
    // });
};
