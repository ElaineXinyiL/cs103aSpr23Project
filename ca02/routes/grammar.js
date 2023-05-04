const express = require('express');
const router = express.Router();
// const User = require('../models/User')
const { openai } = require("../util");

router.get("/grammar", (req, res) => {
  res.render("grammar");
});

router.post("/grammar", async (req, res) => {
  const prompt = req.body.prompt;
  try {
    const completion = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: "can you find grammar errors of the following sentences:" + prompt,
      temperature: 0.8,
      max_tokens: 1024,
    });

    // pass prompt and answer parameters
    res.render(
      "grammar/result", 
      {prompt: prompt, answer: completion.data.choices[0].text}
    )
  } catch(error) {
    console.log(error);
  }
});

module.exports = router;