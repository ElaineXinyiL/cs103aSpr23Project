const express = require("express");
const router = express.Router();
const Prompt = require("../models/Prompt");
const { isLoggedIn, openai } = require("../util");

router.get("/grammar", isLoggedIn, async (req, res, next) => {
  const items = await Prompt.find({
    $and: [{ userId: req.user._id }, { demo: "1" }],
  }).sort({
    createdAt: 1,
  });
  res.render("grammar", { items });
});

router.post("/grammar", isLoggedIn, async (req, res) => {
  const prompt = req.body.prompt;
  const request = "check grammar: " + prompt;
  try {
    const completion = await openai.createCompletion({
      model: "text-davinci-003",
      prompt:
        "can you find grammar errors of the following sentences:" + prompt,
      temperature: 0.8,
      max_tokens: 1024,
    });
    //save request and answer to database
    const request_data = new Prompt({
      userId: req.user._id,
      requests: request,
      answer: completion.data.choices[0].text,
      demo: "1",
    });
    await request_data.save();
    // pass prompt and answer parameters
    res.render("grammar/result", {
      prompt: prompt,
      answer: completion.data.choices[0].text,
    });
  } catch (error) {
    console.log(error);
  }
});
router.get("/grammar/result/:id",
  isLoggedIn,
  async (req, res, next) => {
    const promptItem = await Prompt.findOne({_id:req.params.id});
    res.render("grammar/result", {
      prompt: promptItem.requests,
      answer: promptItem.answer,
    });
});

router.get("/grammar/remove/:id",
  isLoggedIn,
  async (req, res, next) => {
    await Prompt.deleteOne({_id:req.params.id});
    res.redirect("/grammar");
});
module.exports = router;
