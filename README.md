# Federated Learning - Server

# Deploy to AWS 
Beanstalk to zip File  

# install
1. install Python 3.7<br> 
2. pip install --user virtualenv<br>
3. python -m venv ./venv<br>
4. .\venv\Scripts\activate<br>
5. pip install -r requirements.txt<br>

# run
1. python manage.py runserver
2. http://127.0.0.1:8000/
3. show "index ok"
 
# make zip file 
include file & folder
<ol>
<li>.ebextensions</li>
<li>requirements.txt</li>
</ol>


exclude file & folder
<ol>
<li>.git</li>
<li>.idea</li>
<li>venv (auto make from requirements.txt)</li> 
<li>.gitignore</li>
</ol>

# API
<ol>
<li>[get] / <br>
- status check</li>
<li>[get] /weight <br>
- request global weight</li>
<li>[put] /weight <br>
- update local weight</li>
</ol>