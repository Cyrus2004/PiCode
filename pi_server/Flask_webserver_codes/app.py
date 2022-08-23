from flask import Flask, render_template, request, url_for, redirect 
import time
 
app = Flask(__name__) #_name_ tells flask to use files from current directory, and gives it functionality.
 
led1 = 21
led2 = 20
DHT11_pin = 23 #Sensor (not in use).

# app.config["SERVER_NAME"] = "localhost:80"

@app.route("/") #Runs server functionality when a given URL is specified.


@app.route("/") 
def main():
   return render_template('main.html')

number = "5"
buzzerStatus = 0

templateData = {}
templateData["number"] = number
 
#Python program detects HTML URL, and stores the string in "pin" and "action", separated by "/".
@app.route("/<pin>/<action>") #URL names stored in variables "pin" and "action".
def action(pin, action):
   
   if pin == "pin1" and action == "on":
      print("LED 1 is on")
 
   if pin == "pin1" and action == "off":
      print("LED 1 is off")
 
   if pin == "pin2" and action == "on":
      print("LED 2 is on")

   if pin == "pin2" and action == "off":
      print("LED 2 is off")

   return render_template('main.html', **templateData)

@app.route("/", methods = ["GET", "POST"])
def lcdGet():
   
   if request.method == "POST":
      text = request.form.get("Text")
      templateData["text"] = text
      templateData["buzzerStatus"] = buzzerStatus

   return render_template('main.html', **templateData)



@app.route("/buzzerStat")
def buzzerToggler():
   global buzzerStatus
   buzzerStatus = 1 - buzzerStatus
   templateData["buzzerStatus"] = buzzerStatus
   
   return render_template("main.html", **templateData)


 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)