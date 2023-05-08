const express = require('express');
const router = express.Router();
const PromptItem = require('../models/Prompt');
const { isLoggedIn, openai } = require("../util");

router.get("/joke", 
  isLoggedIn,
  async (req, res, next) => {
    const items = await PromptItem.find({userId:req.user._id, demo:"joke"})
                                  .sort({createdAt:1});
    res.render("joke", {items});
});

router.post("/joke", 
  isLoggedIn,
  async (req, res) => {
  const prompt = req.body.prompt;
  try {
    const completion = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: "Generate a joke based on following keywords, be specific" + prompt,
      temperature: 0.8,
      max_tokens: 1024,
    });

    // save prompt and answer to database
    const promptItem = new PromptItem({
      userId: req.user._id,
      requests: prompt,
      answer: completion.data.choices[0].text,
      demo: "joke",
    });
    await promptItem.save();

    // pass prompt and answer parameters
    res.render(
      "joke/result", 
      {prompt: prompt, answer: completion.data.choices[0].text}
    )
  } catch(error) {
    console.log(error);
  }
});


router.get("/joke/result/:id",
  isLoggedIn,
  async (req, res, next) => {
    const promptItem = await PromptItem.findOne({_id:req.params.id});
    res.render("joke/result", {
      prompt: promptItem.requests,
      answer: promptItem.answer,
    });
});

router.get("/joke/remove/:id",
  isLoggedIn,
  async (req, res, next) => {
    await PromptItem.deleteOne({_id:req.params.id});
    res.redirect("/joke");
});

module.exports = router;