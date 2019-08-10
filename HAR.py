import json
import urllib.request
class MyError(Exception):
    def __init__(self, value):
            self.value = value
    def __str__(self):
            return repr(self.value)
class HARobject:
    def __init__(self, url,cookies,headers,postData,content,i):
        self.url = url
        self.cookies = cookies
        self.headers = headers
        self.postData = postData
        self.content = content
        self.i=i
    
    def sendandcompare(self):
        if(self.postData == ''):
            request=urllib.request.Request(url=self.url,headers=self.headers,method='GET')            
        else:
            request=urllib.request.Request(url=self.url,data=self.data,headers=self.headers,method='POST')
        response = urllib.request.urlopen(request)
        htmltmp = response.read()
        try:
            html=htmltmp.decode('utf8')
        except:
            html=htmltmp
        '''
        if(html==''):
            try:
                html=html.decode('gbk')
            except:
                print("无法使用gbk解码,下面使用base64")
                html=''
        if(html==''):
            try:
                html=html.decode('base64')
            except:
                print("无法使用base解码")
                html=''
        if(html==''):
            print('无法解码')
            return 0
        '''
        content= self.content
        i=self.i
        if(len(html)!=len(content)):
            print('第%d个请求不一致' % i)
        else:
            for char in range(len(html)):
                if html[char]!=content[char]:
                    print('第%d个请求不一致' % i)
                    break
                if char ==(len(html)-1):
                    print('第%d个请求一致' % i)
def numbers(str):
    f = open(str,"r",encoding='utf8')
    jsonData=f.read()
    if jsonData.startswith(u'\ufeff'):
        jsonData = jsonData.encode('utf8')[3:].decode('utf8')#如果是带bom的，就去掉bom
    text = json.loads(jsonData)
    numbers=len(text['log']['entries'])
    return numbers
def readhar(str,i):
    f = open(str,"r",encoding='utf8')
    jsonData=f.read()
    #print(jsonData)
 
    if jsonData.startswith(u'\ufeff'):
        jsonData = jsonData.encode('utf8')[3:].decode('utf8')#如果是带bom的，就去掉bom
    text = json.loads(jsonData)
    numbers=len(text['log']['entries'])
    #print(numbers)
    url=text['log']['entries'][i]['request']['url']
    cookies=text['log']['entries'][i]['request']['cookies']
    fakeheaders=text['log']['entries'][i]['request']['headers']
    content=text['log']['entries'][i]['response']['content']['text']
    headers={}
    for a in fakeheaders:
        name=a['name']
        value=a['value']
        headers[name]=value
    if 'Accept-Encoding' in headers:
        headers.pop('Accept-Encoding')
    try:
        postData=text['log']['entries'][i]['request']['postData']
    except:
        postData=''
    
    return HARobject(url,cookies,headers,postData,content,i)
    

#print((a.headers)['Accept-Encoding'])

