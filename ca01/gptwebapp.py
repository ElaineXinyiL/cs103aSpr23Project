'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <p>links of pages</p>
        <ul>
        <li><a href="{url_for('about')}">About the app</a></li>
        <li><a href="{url_for('team')}">Introduction of the team</a></li>
        <li><a href="{url_for('form1')}">Find grammar errors of sentences</a></li>
        <li><a href="{url_for('horror')}">Get a horror story by keywords</a></li>
        <li><a href="{url_for('rap')}">Generate a rap battle</a></li>
        </ul>
    '''
@app.route('/about')
def about():
    ''' what your program does '''
    return f'''
        <h1>About</h1>
        <p>Xin Yi Liu: Find grammar errors of sentences</p>
        <p>Yixuan He: Get a horror story by keywords</p>
        <p>Ruihao Shen: Generate a rap battle between whoever you want</p>
    '''

@app.route('/team')
def team():
    ''' short bio of each member and role '''
    return f'''
        <h1>Team</h1>
        <h3>Xin Yi Liu</h3>
        <p>develop a form page to find grammar errors, and modify other pages</p>
        <h3>Yixuan He</h3>
        <p>develop a form page to get a horror story by keywords</p>
        <h3>Ruihao Shen</h3>
        <p>First year MS3. Role: Developing a rap battle generator</p>
    '''

@app.route('/form1', methods=['GET', 'POST'])
def form1():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt'] 
        answer = gptAPI.getResponse1(prompt)
        return f'''
        <h1>Find grammar errors</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('form1')}> make another query</a>
        '''
    else:
        return '''
        <h1>Find grammar errors</h1>
        Enter your scentences below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/horror', methods=['GET', 'POST'])
def horror():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt'] 
        answer = gptAPI.getResponseHorror(prompt)
        return f'''
        <h1>Get a horror story by keywords</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        <a href={url_for('horror')}> make another query</a>

        '''
    else:
        return '''
        <h1>Get a horror story by keywords</h1>
        Enter your scentences below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/rap', methods=['GET', 'POST'])
def rap():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt'] 
        answer = gptAPI.getRapBattle(prompt)
        return f'''
        <h1>Want an EPIC rap battle? You got it!</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black;white-space: pre-wrap">{answer}</div>
        <a href={url_for('rap')}> make another EPIC battle!</a>

        '''
    else:
        return '''
        <h1>Want an EPIC rap battle? You got it!</h1>
        Name your fighters!!!
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)