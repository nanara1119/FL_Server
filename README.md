# Federated Learning - Server

# 배포방법
Beanstalk, zip파일 배포 

# install
1. install Python 3.7<br> 
2. pip install --user virtualenv<br>
3. python -m venv ./venv<br>
4. .\venv\Scripts\activate<br>
5. pip install -r requirements.txt<br>

# 실행
1. python manage.py runserver
2. http://127.0.0.1:8000/
3. show "index ok"
 
# zip 파일 생성
포함 파일
<ol>
<li>.ebextensions</li>
<li>requirements.txt</li>
</ol>


미포함
<ol>
<li>.git</li>
<li>.idea</li>
<li>venv (requirements.txt에 의해 자동 생성 됨 )</li> 
<li>.gitignore</li>
</ol>

# API
<ol>
<li>[get] / <br>
status 확인 용 </li>
<li>[get] /weight <br>
global weight를 요청 </li>
<li>[put] /weight <br>
local weight를 서버에 전송</li>
</ol>