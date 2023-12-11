### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  Python can be written in "plain English."  For example, a variable in Python doesn't require the writer to put "let" in front of the variable.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
  You can put a catch in the code that says if the user is trying to get something that does not exist respond with "Does not exist"

- What is a unit test?

  A unit test is testing a small amount of code

- What is an integration test?
  
  An integration test is where code is tested as a grop

- What is the role of web application framework, like Flask?

  It enables coders to create web apps quickly

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  predefined vs serach based

- How do you collect data from a URL placeholder parameter using Flask?

  request.args()

- How do you collect data from the query string using Flask?

  request.url()

- How do you collect data from the body of the request using Flask?

  request.args.get

- What is a cookie and what kinds of things are they commonly used for?

   A cookie is data that a website will access when a user visits a website, like their viewing preferences.

- What is the session object in Flask?

   A session is also data that is used on a website but is gone after a user closes the browser.

- What does Flask's `jsonify()` do?

   it will turn your code into json for your api
