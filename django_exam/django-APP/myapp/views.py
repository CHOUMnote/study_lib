'''
생활코딩 django 수업 클론코딩
"https://www.youtube.com/watch?v=pbKhn2ten9I&list=PLuHgQVnccGMDLp4GH-rgQhVKqqZawlNwG&index=1"
urls.py, views.py파일 이해와 라우팅연습
'''
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

#변수를 이용한 템플릿 이용
def HTMLtemplate(articleTag,id=None):
    global topics
    contextUI = ''
    if id is not None:
        contextUI = f'''
                <li>
                    <form action="/delete/" method="post">
                        <input type="hidden" name="id" value={id}>
                        <input type="submit" value="delete">
                    </form>
                    <li><a href="/update/{id}">update</a></li>
                </li>
        '''
    ol = ''
    for topic in topics:
        ol += '<li><a href="/read/{}">{}</a></li>'.format(topic["id"],topic["title"])
    return f'''
        <html>
        <body>
            <h1><a href="/">Django</a></h1>
            <ul>
                {ol}
            </ul>
            {articleTag} 
            <ul>
                <li><a href="/create/">create</a></li> 
                {contextUI}
            </ul>
        </body>
        </html>
        '''
#루트    
def index(request):
    article ='''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLtemplate(article))#일반 html파일 생성

#추가
@csrf_exempt
def create(request):
    '''
    "request" method 변수로 post, get 구분
    -> POST일시 딕셔너리 형태로 데이터 보유 -> 딕셔너리로 데이터 접근
    '''
    global nextId
    article = ''
    if request.method == 'GET': #->GET
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" ></p>
        </form>
        '''
        return HttpResponse(HTMLtemplate(article))
    elif request.method == 'POST': #-> POST
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {'id':nextId, 'title':title, 'body':body}
        url='/read/'+str(nextId)
        nextId+=1
        topics.append(newTopic)
        return redirect(url)    #해당 url 호출 -> urls.py 라우팅을 따라간다!

#목록 
def read(request, id):
    global topics
    article =''
    for i in topics:
        if i['id'] == int(id):
            article = f"<h2>{i['title']}</h2>{i['body']}"
            break
    return HttpResponse(HTMLtemplate(article,id))

#삭제
@csrf_exempt
def delete(request):
    global topics

    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for i in topics:
            if i['id'] != int(id):
                newTopics.append(i)
        topics = newTopics
    return redirect('/')

#업데이트
@csrf_exempt
def update(request,id):
    global topics
    if request.method == 'GET':
        for i in topics:
            if i['id'] == int(id):
                selected = {
                    "title":i['title'],
                    "body":i["body"]
                }
        article = f'''
        <form action="/update/{id}/" method="post">
            <p><input type="text" name="title" placeholder="title" value={selected["title"]}></p>
            <p><textarea name="body" placeholder="body">{selected["body"]}</textarea></p>
            <p><input type="submit" ></p>
        </form>
        '''
        return HttpResponse(HTMLtemplate(article,id))
    elif request.method =='POST':
        title = request.POST["title"]
        body = request.POST["body"]
        for i in topics:
            if i['id'] == int(id):
             i['title'] = title
             i['body'] = body
             
        return redirect(f"/read/{id}/")