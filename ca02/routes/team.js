const express = require('express');
const router = express.Router();
const { isLoggedIn } = require("../util");

router.get('/team', 
  isLoggedIn,
  (req,res,next) => {
    res.render('team');
  }
)

module.exports = router;