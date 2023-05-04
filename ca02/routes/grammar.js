const express = require('express');
const router = express.Router();
// const User = require('../models/User')
const Prompt = require('../models/Prompt')
const { openai } = require("../util");

router.get("/grammar", (req, res) => {
  res.render("grammar");
});

router.post("/grammar", async (req, res) => {
  const prompt = req.body.prompt;
  const request =  "check grammar" + prompt;
  try {
    const completion = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: "can you find grammar errors of the following sentences:" + prompt,
      temperature: 0.8,
      max_tokens: 1024,
    });
    //save request and answer to database
    const request_data = new Prompt(
      {userId:req.session.user._id, 
      requests:request,
      answer:completion.data.choices[0].text,
      })
    await request_data.save()
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