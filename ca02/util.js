const express = require('express');
const app = express();
const openAI = require('openai');
// configure dotenv
require("dotenv").config();

/* **************************************** */
/*  middleware to make sure a user is logged in
/* **************************************** */

function isLoggedIn(req, res, next) {
  // if they are logged in, continue; otherwise redirect to /login
  if (res.locals.loggedIn) {
    next();
  } else {
    res.redirect("/login");
  }
}

/* **************************************** */
/*  require openai module and use dotenv to load API key from .env file
/* **************************************** */
// Importing and setting up the OpenAI API client
const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

module.exports = { isLoggedIn, openai };