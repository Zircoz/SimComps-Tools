var express = require('express');
const axios = require('axios');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/market', function(req, res, next){
  axios.get('https://www.simcompanies.com/api/v2/market/10')
  .then(response => {
    console.log(response.data);
    res.send(response.data);
  })
  .catch(error => {
    console.log(error);
    //res.send(error);
  })
});
module.exports = router;
