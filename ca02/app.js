const createError = require('http-errors');
const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const layouts = require("express-ejs-layouts");

// require router from router index file
const router = require("./routes/index");

// require user model
const User = require('./models/User');


/* **************************************** */
/*  Connecting to a Mongo Database Server   */
/* **************************************** */
const mongodb_URI = process.env.MONGODB_URI || 'mongodb://127.0.0.1:27017/gptdemo';
('MONGODB_URI=',process.env.MONGODB_URI);

const mongoose = require( 'mongoose' );
mongoose.connect(mongodb_URI);
const db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  console.log("we are connected!!!")
});


/* **************************************** */
/* Enable sessions and storing session data in the database */
/* **************************************** */
const session = require("express-session"); // to handle sessions using cookies 
var MongoDBStore = require('connect-mongodb-session')(session);

const store = new MongoDBStore({
  uri: mongodb_URI,
  collection: 'mySessions'
});

// Catch errors                                                                      
store.on('error', function(error) {
  console.log(error);
});


/* **************************************** */
/* creating the app */
/* **************************************** */
var app = express();

app.use(session({
  secret: 'This is a secret',
  cookie: {
    maxAge: 1000 * 60 * 60 * 24 * 7 // 1 week                                        
  },
  store: store,
  // Boilerplate options, see:                                                       
  // * https://www.npmjs.com/package/express-session#resave                          
  // * https://www.npmjs.com/package/express-session#saveuninitialized               
  resave: true,
  saveUninitialized: true
}));

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
const port = process.env.PORT || 5000;
app.use(layouts);


// configure app to use routes
app.use("/", router);

/* **************************************** */
/* handle the error */
/* **************************************** */

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};
  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

// listen to specified app
app.listen(port, () => console.log(`Server is running on port ${port}!`));

module.exports = app;
