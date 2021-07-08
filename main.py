import logging
from flask import Flask


app = Flask(__name__)


@app.route('/')
print("THIS IS A CALCULATOR:")
a = int(input("ENTER THE FIRST NUMBER:"))
b = int(input("ENTER THE SECOND NUMBER:"))
print("OPTIONS: ADD, SUBSTRACT, MULTIPLY, DIVIDE")
c = input("CHOOSE YOUR OPTION:")
if c == "ADD":
  m = a+b
  print"THE ANSWER IS:", m)
elif c =="SUBSTRACT":
  n = a-b
  print("THE ANSWER IS:", n)
elif c =="MULTIPLY":
  o = a*b
  print("THE ANSWER IS:", o)
elif c =="DIVIDE":
  p = a/b
  print("THE ANSWER IS:", p)
print("THANK YOU!")

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500   
    
if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]      
  
    
  
