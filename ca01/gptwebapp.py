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
from flask import request, redirect, url_for, Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

# Define some CSS styles
STYLES = '''
            body {
                background-color: #111;
                font-family: 'Roboto Mono', monospace;
                color: #fff;
                margin: 0;
            }
            header {
                text-align: center;
                padding: 2rem 0;
            }
            h1 {
                font-size: 5rem;
                font-weight: bold;
                letter-spacing: 0.5rem;
                margin: 0;
                text-transform: uppercase;
                text-shadow: 0 0 0.5rem #fff, 0 0 1rem #fff, 0 0 2rem #fff, 0 0 4rem #0ff, 0 0 8rem #0ff, 0 0 16rem #0ff;
            }
            .front {
                margin: 0 3rem;
            }
            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin: 2rem 0;
            }
            pre {
                font-size: 1.8rem;
                white-space: pre-wrap;
                word-wrap: break-word;
            }
            pre.horror-response {
                padding: 20px;
                margin-left: 60px;
            }
            hr {
                border: none;
                height: 0.5rem;
                background: linear-gradient(to right, #0ff, #fff);
                margin: 2rem 0;
                width: 100%;
            }
            a {
                color: #0ff;
                font-size: 1.2rem;
                text-decoration: none;
                transition: color 0.2s;
                display: flex;
            }
            a:hover {
                color: #fff;
            }
            .keyword {
                color: #0ff;
            }

            input[type=submit]:hover {
                background-color: #fff;
                color: #333;
            }
            nav {
                background-color: #ddd;
                padding: 10px;
            }

            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
            }

            nav li {
                display: inline-block;
                margin-right: 10px;
            }

            nav a {
                color: #333;
                text-decoration: none;
                padding: 5px;
                border-radius: 5px;
            }

            nav a:hover {
                color: #4693A4;
            }

            .form-group {
                margin-bottom: 10px;
            }

            textarea {
                width: 50%;
                height: 30%;
                padding: 40px;
                
                font-size: 18px;
                border: 2px solid #777;
                border-radius: 15px;
                color: #fff;
                background-color: #222;
                box-shadow: 0px 2px 10px #777;
            }

            .text-form {
                margin-left: 3rem;
            }

            input[type=submit] {
                background: linear-gradient(to right, #0ff, #fff);
                padding: 15px 30px;
                border: none;
                border-radius: 25px;
                cursor: pointer;
                font-size: 16px;
                text-transform: uppercase;
                letter-spacing: 2px;
                box-shadow: 0px 5px 10px #888;
                transition: background-color 0.3s ease;
            }

            input[type=submit]:hover {
                background-color: #0097a7;
            }
'''


@app.route('/')
def index():
    ''' display a link to the general query page '''
    return f'''
        <html>
        <head>
        <title>GPT Demo</title>
        <style>{STYLES}</style>
        </head>
        <body>
        <header>
            <h1>GPT Demo</h1>
        </header>
        <nav>
            <ul>
                <li><a href="{url_for('about')}">About</a></li>
                <li><a href="{url_for('team')}">Team</a></li>
                <li><a href="{url_for('form1')}">Demo1: Grammar Error Detection</a></li>
                <li><a href="{url_for('joke')}">Demo2: Keyword-Based Joke Generator</a></li>
                <li><a href="{url_for('horror')}">Demo3: Get a horror story by keywords</a></li>
                <li><a href="{url_for('rap')}">Demo4: Generate a rap battle</a></li>
                <li><a href="{url_for('rap')}">Demo5: Get a movie line by keywords</a></li>
            </ul>
        </nav>
        <div class="container">
            <h2>Welcome to GPT Demo</h2>
            <p>Please choose one of the links above to get started.</p>
        </div>
        </body>
        </html>
    '''


@app.route('/about')
def about():
    ''' explain what the program does '''
    return f'''
        <html>
        <head>
        <title>About</title>
        <style>{STYLES}</style>
        </head>
        <body>
        <header>
            <h1>About the Demos</h1>
        </header>
        <div class="container">
            <h3 class="keyword">Xin Yi Liu</h3>
            <p>Brandeis 23' MS3 CS</p>
            <p>Demo1: Find grammar errors of sentences</p>
            <h3 class="keyword">Hongqian Li</h3>
            <p>Brandeis 24' MS4 CS</p>
            <p>Demo2: Generate a simple joke based on keywords</p>
            <h3 class="keyword">Yixuan He</h3>
            <p>Brandeis 24' MS4 CS</p>
            <p>Demo3: Get a horror story by keywords</p>
            <h3 class="keyword">Ruihao Shen</h3>
            <p>Brandeis 24' MS3 CS</p>
            <p>Demo4: Generate a rap battle</p>
            <h3 class="keyword">Yichun Huang</h3>
            <p>Brandeis 24' MS4 CS</p>
            <p>Demo4: Get a movie line by keywords</p>
        </div>
    '''


@app.route('/team')
def team():
    ''' short bio of each member and role '''
    return f'''
        <html>
        <head>
        <title>Team Introduction</title>
        <style>{STYLES}</style>
        </head>
        <body>
        <header>
            <h1>Our Team Members</h1>
        </header>
        <div class="container">
            <h2 class="keyword">Xin Yi Liu</h2>
            <p>developed a form page to find grammar errors, and modified other pages</p>
            <h2 class="keyword">Hongqian Li</h2>
            <p>developed a form page to generate a joke based on keywords, added some basic UI</p>
            <h2 class="keyword">Yixuan He</h2>
            <p>developed a form page to get a horror story by keywords</p>
            <h2 class="keyword">Ruihao Shen</h2>
            <p>developed a rap battle generator between whoever you want</p>
            <h2 class="keyword">Yichun Huang</h2>
            <p>developed a form page to get a movie line, containing given keywords</p>
        </div>
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
        <html>
        <head>
            <title>Find grammar errors</title>
            <style>
                /* Add the given styles here */
                {STYLES}
            </style>
        </head>
        <body>
            <header>
            <h1>Find grammar errors</h1>
            </header>
            <div class="container">
                <pre>Your sentences: <span class="keyword">{prompt}</span></pre>
                <hr>
            </div>
            <div class="container">
                <pre>{answer}</pre>
            </div>
            <div class="container">
                <a href={url_for('form1')}> Make Another Query</a>
            </div>
        </body>
        </html>
        '''
    else:
        return f'''
        <html>
        <head>
            <title>Find grammar errors</title>
            <style>{STYLES}</style>
        </head>
        <body>
            <header>
            <h1>Find grammar errors</h1>
            </header>
            <div class="front">
                <h2>Find grammar errors</h2>
                <hr>
                <h3>Enter your sentences below</h3>
            </div>
            <div class="text-form">
                <form method="post">
                    <textarea name="prompt"></textarea>
                    <p><input type=submit value="get response">
                </form>
            </div>
        </body>
        </html>
        '''


@app.route('/joke', methods=['GET', 'POST'])
def joke():
    ''' handle a get request by sending a form 
    and a post request by returning the GPT response to generate jokes
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponseJoke(prompt)
        return f'''
        <html>
        <head>
            <title>Joke Generator</title>
            <style>
                /* Add the given styles here */
                {STYLES}
            </style>
        </head>
        <body>
            <header>
            <h1>Joke Generator</h1>
            </header>
            <div class="container">
                <pre>Keywords: <span class="keyword">{prompt}</span></pre>
                <hr>
            </div>
            <div class="container">
                <pre>{answer}</pre>
            </div>
            <div class="container">
                <a href={url_for('joke')}> Make Another Query</a>
            </div>
        </body>
        </html>
        '''
    else:
        return f'''
        <html>
        <head>
            <title>Joke Generator</title>
            <style>{STYLES}</style>
        </head>
        <body>
            <header>
            <h1>Joke Generator</h1>
            </header>
            <div class="front">
                <h2>Generate a joke based on keywords</h2>
                <hr>
                <h3>Type in a few keywords:</h3>
            </div>
            <div class="text-form">
                <form method="post">
                    <textarea name="prompt"></textarea>
                    <p><input type=submit value="get response">
                </form>
            </div>
        </body>
        </html>
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
        <html>
        <head>
            <title>Horror story Generator</title>
            <style>
                /* Add the given styles here */
                {STYLES}
            </style>
        </head>
        <body>
            <header>
            <h1>Horror story Generator</h1>
            </header>
            <div class="container">
                <pre>Keywords: <span class="keyword">{prompt}</span></pre>
                <hr>
            </div>
            <div class="container">
                <pre class="horror-response">{answer}</pre>
            </div>
            <div class="container">
                <a href={url_for('horror')}> Make Another Query</a>
            </div>
        </body>
        </html>
        '''
    else:
        return f'''
        <html>
        <head>
            <title>Horror story Generator</title>
            <style>{STYLES}</style>
        </head>
        <body>
            <header>
            <h1>Horror story Generator</h1>
            </header>
            <div class="front">
                <h2>Get a horror story by keywords</h2>
                <hr>
                <h3>Type in a few keywords:</h3>
            </div>
            <div class="text-form">
                <form method="post">
                    <textarea name="prompt"></textarea>
                    <p><input type=submit value="get response">
                </form>
            </div>
        </body>
        </html>
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
        return f'''
        <h1>Want an EPIC rap battle? You got it!</h1>
        Name your fighters!!!
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/movieline', methods=['GET', 'POST'])
def movieline():
    ''' handle a get request by sending a form
    and a post request by returning the GPT response to generate movie lines
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponseMovieLine(prompt)
        return f'''
        <html>
        <head>
            <title>Movie Line Generator</title>
            <style>
                /* Add the given styles here */
                {STYLES}
            </style>
        </head>
        <body>
            <header>
            <h1>Movie Line Generator</h1>
            </header>
            <div class="container">
                <pre>Keywords: <span class="keyword">{prompt}</span></pre>
                <hr>
            </div>
            <div class="container">
                <pre class="movieline-response">{answer}</pre>
            </div>
            <div class="container">
                <a href={url_for('movieline')}> Make Another Query</a>
            </div>
        </body>
        </html>
        '''
    else:
        return f'''
        <html>
        <head>
            <title>Movie Line Generator</title>
            <style>{STYLES}</style>
        </head>
        <body>
            <header>
            <h1>Movie Line Generator</h1>
            </header>
            <div class="front">
                <h2>Generate a movie line based on keywords</h2>
                <hr>
                <h3>Type in a few keywords:</h3>
            </div>
            <div class="text-form">
                <form method="post">
                    <textarea name="prompt"></textarea>
                    <p><input type=submit value="get response">
                </form>
            </div>
        </body>
        </html>
        '''


if __name__ == '__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True, port=5000)
