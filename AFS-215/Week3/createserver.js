const express = require("express")
const app = express()
app.use(express.json())

app.listen(3000, ()=> console.log("Server running in 3000? Yep!"))


