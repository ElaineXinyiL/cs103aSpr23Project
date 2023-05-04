const express = require('express');
const router = express.Router();
const { isLoggedIn } = require("../util");

router.get('/about', 
  isLoggedIn,
  (req,res,next) => {
    res.render('about');
  }
)

module.exports = router;