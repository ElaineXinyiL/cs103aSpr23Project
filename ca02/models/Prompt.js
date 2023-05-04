"use strict";
const mongoose = require("mongoose");
const Schema = mongoose.Schema;

var promptSchema = Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
  requests: String,
  answer: String,
});

module.exports = mongoose.model("Prompt", promptSchema);
