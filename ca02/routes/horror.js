const express = require('express');
const router = express.Router();
const { openai } = require("../util");

router.get("/horror", (req, res) => {
  res.render("horror");
});

router.post("/horror", async (req, res) => {
  const prompt = req.body.prompt;
  try {
    const completion = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: "Generate a horror story based on following keywords, be specific" + prompt,
      temperature: 0.8,
      max_tokens: 1024,
    });

    // pass prompt and answer parameters
    res.render(
      "horror/result", 
      {prompt: prompt, answer: completion.data.choices[0].text}
    )
  } catch(error) {
    console.log(error);
  }
});

module.exports = router;