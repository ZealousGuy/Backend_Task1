# Imports
from flask import Flask,render_template,request
import re

# Object creation
flask=Flask(__name__)

# EndPoints/Routes
@flask.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        regex=request.form.get('Regex')
        matchingString=request.form.get('StringToMatch')

        # If the text boxes are Empty 
        if (not regex.strip()) or (not matchingString.strip):   # type: ignore
            return "Please enter something"

        result=re.findall(regex,matchingString)                 # type: ignore
        return render_template('result.html', result=result)
        # return str(len(result)) + " matches" + str(result)

    else:
        return render_template('home.html')


# Run the app
if __name__=='__main__':
    flask.run(debug=True)