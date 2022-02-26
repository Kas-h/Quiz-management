from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio.session import *

app = Flask(__name__)


def exam():
        
    c = 0
  
    put_html("<h1>Quiz</h1>")

    name = input("Please enter your name to start the test", type ="text", validate = validate_name)


    q1 = radio("Q1.Who is the best player of all time?",['Lionel Messi','Cristiano Ronaldo','Pele','Diego Maradona'])
    if q1 =='Lionel Messi':
        c+=1

    q2 = radio("Q2. Which team has the most UCL titles?",['Barcelona','Real Madrid','Bayern Munich','AC Milan'])
    if q2 =='Real Madrid':
        c+=1

    q3 = radio("Q3. Which club has the most premier league titles",['Liverpool','Chelsea','Manchester City','Manchester United'])
    if q3 =='Manchester United':
        c+=1

    q4 = radio("Q4. How much did Neymar Jr cost PSG?",['100M','150M','222M','200M'])
    if q4 == '222M':
        c+=1

    q5 = radio("Q5. Which of these clubs have never won a UCL?",['Chelsea','Arsenal','Juventus','Borrusia Dortmund'])
    if q5 == 'Arsenal':
        c+=1

    if c>3:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Congratulations !! </h1>"+ name + ", your score is <b>"+ str(c) + "</b><br><br>") ,'color:green;'),style(put_html("<p>Result : <b>PASSED</b></p>"),'color:green'), put_html("<b>Thank You for your participation.</b>")]
    	popup("Score", content=message, size='large', implicit_close=True, closable=True)
    else:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Oops! " + "</h1>" + name + ", your score is <b>"+ str(c) + "</b><br><br>"),'color:red'), style(put_html("<p>Result : <b>FAILED</b></p>"), 'color:red') , put_html("<b>Thank You for your participation.</b><br><br>"), style(put_link('Retry ↺',""), 'color:red;align-content: center;border-radius: 5px;color:#f9faf8;padding: 5px 100px;text-align:center;align-items : center;background-color: white;\
            background-image: linear-gradient(270deg, #8cf5f5 1%, #0a43f3 100%);')]
    	popup("Score", content=message, size='large', implicit_close=True, closable=True)
def validate_name(name):
	name = name.replace(" ","")
	if(name == "" or not(name.isalpha())):
		return("Please enter a non empty name consisting of alphabets only")



app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)

from pywebio.session import *

app = Flask(__name__)


def exam():
        
    c = 0
  
    put_html("<h1>Quiz</h1>")

    name = input("Please enter your name to start the test", type ="text", validate = validate_name)


    q1 = radio("Q1.Who is the best player of all time?",['Lionel Messi','Cristiano Ronaldo','Pele','Diego Maradona'])
    if q1 =='Lionel Messi':
        c+=1

    q2 = radio("Q2. Which team has the most UCL titles?",['Barcelona','Real Madrid','Bayern Munich','AC Milan'])
    if q2 =='Real ':
        c+=1

    q3 = radio("Q3. Which club has the most premier league titles",['Liverpool','Chelsea','Manchester City','Manchester United'])
    if q3 =='Manchester United':
        c+=1

    q4 = radio("Q4. How much did Neymar Jr cost PSG?",['100M','150M','222M','200M'])
    if q4 == '222M':
        c+=1

    q5 = radio("Q5. Which of these clubs have never won a UCL?",['Chelsea','Arsenal','Juventus','Borrusia Dortmund'])
    if q5 == 'Arsenal':
        c+=1

    if c>3:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Congratulations !! </h1>"+ name + ", your score is <b>"+ str(c) + "</b><br><br>") ,'color:green;'),style(put_html("<p>Result : <b>PASSED</b></p>"),'color:green'), put_html("<b>Thank You for your participation.</b>")]
    	popup("Score", content=message, size='large', implicit_close=True, closable=True)
    else:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Oops! " + "</h1>" + name + ", your score is <b>"+ str(c) + "</b><br><br>"),'color:red'), style(put_html("<p>Result : <b>FAILED</b></p>"), 'color:red') , put_html("<b>Thank You for your participation.</b><br><br>"), style(put_link('Retry ↺',""), 'color:red;align-content: center;border-radius: 5px;color:#f9faf8;padding: 5px 100px;text-align:center;align-items : center;background-color: white;\
            background-image: linear-gradient(270deg, #8cf5f5 1%, #0a43f3 100%);')]
    	popup("Score", content=message, size='large', implicit_close=True, closable=True)
def validate_name(name):
	name = name.replace(" ","")
	if(name == "" or not(name.isalpha())):
		return("Please enter a non empty name consisting of alphabets only")



app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)

