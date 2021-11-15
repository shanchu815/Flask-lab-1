"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['mean', 'rude', 'horrible', 'untalented', 'ugly', 'terrible', 'stupid']

@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
      Hi! This is the home page.
      <p>
        <a href="http://localhost:5000/hello">Hello.</a>
      </p>
    </html>"""



@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <p>
          To receive a compliment, fill out the form at: <a href="http://localhost:5000/compliment-choices"> Compliment. </a>
        </p>
        <p>
          Or, if you'd rather be insulted, fill out the form at: <a href="http://localhost:5000/insult-choices"> Insult. </a>
        </p>
      </body>
    </html>
    """

@app.route('/compliment-choices')
def compliment_choices():
  """Lets user choose compliment"""
  
  return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <p>
            Choose your favorite compliment:
              <select name="attribute">
                <option value="Your hair looks very nice.">Your hair looks very nice.</option>
                <option value="You're a very kind person.">You're a very kind person.</option>
                <option value="You're a very skilled person.">You're a very skilled person.</option>
              </select>  
          </p>
          <input type="submit" value="Submit">
        </form>
        </p>
      </body>
    </html>
    """

@app.route('/insult-choices')
def insult_choices():
  """Lets user choose insult"""
  
  return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <p>
            Choose your favorite non-compliment:
              <select name="insult">
                <option value="Your hair looks like a rat's nest.">Your hair looks like a rat's nest.</option>
                <option value="You're a really rude person.">You're a really rude person.</option>
                <option value="You suck at everything you do.">You suck at everything you do.</option>
              </select>  
            </p>
          <input type="submit" value="Submit">
        </form>
        </p>
      </body>
    </html>
    """



# DONE - first web page should be greeting the person & takes you to hello
# DONE - hello should let you submit your [name] & [choose if you want insult or compliment]
# DONE - insult level page = dropdown menu of insults to pick from
# NEED TO MAKE - display the [name] + chosen insult + randomly generated insult 
# DONE - compliment level page = dropdown menu of compliment to pick from
# NEED TO MAKE - display the [name] + chosen compliment + randomly generated compliment


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = choice(AWESOMENESS)
    new_compliment = request.args.get("attribute")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}! {new_compliment}
        <p>
          <a href="http://localhost:5000/">Return to the start</a>
        </p>
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    insult = choice(INSULTS)
    new_diss = request.args.get("insult")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}! {new_diss}
        <p>
          <a href="http://localhost:5000/">Return to the start</a>
        </p>
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
