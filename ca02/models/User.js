'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;

var userSchema = Schema( {
  username: String,
  passphrase: String,
  // keep track of all requests the user has made
  requests: [{ type: String }],
} );

module.exports = mongoose.model( 'User', userSchema );
