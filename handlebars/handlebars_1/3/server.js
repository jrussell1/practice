//dependencies
var express = require("express");
var exphbs = require("express-handlebars");
var app = express();
//define port 8080
var PORT = process.env.PORT || 8080;
//define handlebars
app.engine("handlebars", exphbs({ defaultLayout: "main"}));
app.set("view engine", "handlebars");

var icecream = [
    {name: 'vanilla', price: 10, awesomeness: 3},
    {name: 'chocolate', price: 4, awesomeness: 8},
    {name: 'banana', price: 1, awesomeness: 1},
    {name: 'greentea', price: 5, awesomeness: 7},
    {name: 'jawbreakers', price: 6, awesomeness: 2},
  ];

app.get("/icecream/:name", function(req,res) {
    for (var i = 0; i < icecream.length; i++) {
        if (icecream[i].name === req.params.name) {
            return res.render("icecream", icecream[i]);
        }
    }
});

app.get("/icecream", function(req, res) {
    res.render("icecream1", { icecream1: icecream });
});

app.listen(PORT, function() {
    // Log (server-side) when our server has started
    console.log("Server listening on: http://localhost: " + PORT);
});