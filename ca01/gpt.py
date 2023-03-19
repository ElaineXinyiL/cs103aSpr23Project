'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''

    def __init__(self, apikey):
        ''' store the apikey in an instance variable '''
        self.apikey = apikey
        # Set up the OpenAI API client
        openai.api_key = apikey  # os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self, prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def getResponse1(self, prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt="can you find grammar errors of the following sentences:"+prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    def getResponseHorror(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt="Generate a short horror story including given keywords:" + prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        response = completion.choices[0].text
        return response

    def getResponseJoke(self, prompt):
        ''' Generate a GPT response for a simple joke based on a few keywords '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt="can you generate a joke based on these keywords:" + prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    def getRapBattle(self,prompt):
        ''' Generate a GPT response '''
        full_prompt = f"""
            Please generate a script of a rap battle between designated persons. You need to play as them credibly, 
            taking their personal story, contribution or anecdotes into consideration. You also need to bash your 
            opponent with your smart. Add their name before each one's words. The name of them are {prompt}. Now, 
            start. Remember, MAKE IT EPIC!"""
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=full_prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def getResponseMovieLine(self, prompt):
        ''' Generate a GPT response for a movie line based on a few keywords '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt="Get a movie line from a character in a movie with the following keywords:" + prompt + " from the movie",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
    )

        response = completion.choices[0].text
        return response


if __name__ == '__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponseJoke("what does openai's GPT stand for?"))
