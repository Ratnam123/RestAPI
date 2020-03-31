Step1: Create python virutal environment to setup the flask application

	virtualenv /opt/flask
	source /opt/flask/bin/activate

Step2: Install the required softwares as listed below

	aniso8601==8.0.0
	click==7.1.1
	Flask==1.1.1
	Flask-Cors==3.0.8
	Flask-RESTful==0.3.8
	itsdangerous==1.1.0
	Jinja2==2.11.1
	jsonify==0.5
	MarkupSafe==1.1.1
	pytz==2019.3
	six==1.14.0
	Werkzeug==1.0.0

Step3: Check the port availability by using below command

	netstat -anp | grep 9002

Step4: Write  the main.py file to handle the flask app

Step5: Write the another python file to handle the request and response

Step6: Testing the Rest API
