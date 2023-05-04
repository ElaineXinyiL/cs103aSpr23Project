const express = require('express');
const router = express.Router();
const { openai } = require("../util");

router.get("/rap", (req, res) => {
  res.render("rap/index");
});

router.post("/rap", async (req, res) => {
  const prompt = req.body.prompt;
  try {
    const completion = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: generatePrompt(prompt),
      temperature: 0.8,
      max_tokens: 1024,
    });

    // pass prompt and answer parameters
    res.render(
      "rap/result", 
      {prompt: prompt, answer: completion.data.choices[0].text}
    )
  } catch(error) {
    console.log(error);
  }
});

function generatePrompt(prompt) {
  return `Please generate a script of a rap battle between designated persons. You need to play as them credibly, 
    taking their personal story, contribution or anecdotes into consideration. You also need to bash your 
    opponent with your smart. Add their name before each one's words. The name of them are ${prompt}. Now, 
    start. Remember, MAKE IT EPIC!`
}

module.exports = router;