const express = require('express');
const router = express.Router();
// const User = require('../models/User')
const {
    openai
} = require("../util");

router.get("/movie", (req, res) => {
    res.render("movie");
});

router.post("/movie", async (req, res) => {
    const prompt = req.body.prompt;
    try {
        const completion = await openai.createCompletion({
            model: "text-davinci-003",
            prompt: "Get a movie line based on following keywords, be specific" + prompt,
            temperature: 0.8,
            max_tokens: 1024,
        });

        console.log(completion.propmt);
        // pass prompt and answer parameters
        res.render(
            "movie/result", {
                prompt: prompt,
                answer: completion.data.choices[0].text
            }
        )
    } catch (error) {
        console.log(error);
    }
});

module.exports = router;