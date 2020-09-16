var mainHeading = document.getElementById("main")
mainHeading.addEventListener("mouseenter", (e)=>{    
    mainHeading.style.textDecoration= e.target.style.textDecoration == "none"? "underline": "none"
})
console.log(document.getElementById("main"))