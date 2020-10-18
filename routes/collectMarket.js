var express = require('express');
const axios = require('axios');
var router = express.Router();

token = process.env.token
var resourceIDs = [...Array(114).keys()];
resourceIDs.shift();
resourceIDstring = resourceIDs.map(x => x.toString())
urls = resourceIDs.map(x => 'https://www.simcompanies.com/api/v2/market/'+x)
console.log(urls[0])
console.log(urls[1])
router.get('/token/:tokenID/all', function(req, res, next){
  axios.all(urls)
    .then(axios.spread((...responses)=>{
      var lowestPrices =
      //refactor this part to send to db in model
    })
})

router.get('/token/:tokenID/resource/:resourceID', function (req, res) {
  if (req.params.tokenID != token){
      res.send("unauthorized action");
  }
  var url = 'https://www.simcompanies.com/api/v2/market/'+req.params.resourceID
  axios.get(url)
    .then(function (response) {
      console.log(response.data)
      //res.send(response.data)
      res.send(response.data)
    })
    .catch(function (error) {
      console.log(error)
      res.send(error)
    })
    .then(function () {
    });
})
module.exports = router;
