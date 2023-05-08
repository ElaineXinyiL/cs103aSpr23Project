const express = require("express");
const router = express.Router();
const PromptItem = require("../models/Prompt");
const { isLoggedIn, openai } = require("../util");

router.get("/horror", isLoggedIn, async (req, res, next) => {
  const items = await PromptItem.find({ userId: req.user._id, demo: "horror" }).sort({createdAt:1});
  res.render("horror/index", { items });
});

router.post("/horror", isLoggedIn, async (req, res) => {
  const prompt = req.body.prompt;
  try {
    const completion = await openai.createCompletion({
      model: "text-davinci-003",
      prompt:
        "Generate a horror story based on following keywords, be specific" +
        prompt,
      temperature: 0.8,
      max_tokens: 1024,
    });

    // save prompt and answer to database
    const promptItem = new PromptItem({
      userId: req.user._id,
      requests: prompt,
      answer: completion.data.choices[0].text,
      demo: "horror",
    });
    await promptItem.save();

    // pass prompt and answer parameters
    res.render("horror/result", {
      prompt: prompt,
      answer: completion.data.choices[0].text,
    });
  } catch (error) {
    console.log(error);
  }
});

router.get("/horror/result/:id", isLoggedIn, async (req, res, next) => {
  const promptItem = await PromptItem.findOne({ _id: req.params.id });
  res.render("horror/result", {
    prompt: promptItem.requests,
    answer: promptItem.answer,
  });
});

router.get("/horror/remove/:id", isLoggedIn, async (req, res, next) => {
  await PromptItem.deleteOne({ _id: req.params.id });
  res.redirect("/horror");
});

module.exports = router;
