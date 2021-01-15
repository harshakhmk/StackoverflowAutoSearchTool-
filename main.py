from subprocess import Popen,PIPE
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
env_path=Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
cache_pages={}


def create_question(error_type):
    
    body=error_type
    access_token=os.environ['ACCESS_TOKEN']
    key=os.environ['key']
    url="https://api.stackexchange.com/docs/create-question/"
    
    data={
        'title':'Python',
        'body':body,
        'tags':'python',
        'key':key,
        'access_token':access_token,
        'preview':'true',
        'filter':'default',
        'site':'stackoverflow',
        }
    resp=requests.post(url=url,data=data)
    return resp.text


def execute_file(command):
  args=command.split()
  process=Popen(args,stdout=PIPE,stderr=PIPE)
  #get output and error
  output,error=process.communicate()
  return [output,error]

def get_error_messages(filename):
    error_message=(execute_file(f"python {filename}.py")[1]).decode('ascii')
    error_type=error_message.strip().split("\n")[-1]
    error_line=error_message.strip().split("\n")[-3].split(',')[1]
    return [error_line,error_type]

def request_json_data(n,error_type):
    url="https://api.stackexchange.com/"+"2.2/search?pagesize={}&order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(n,error_type)
    response=requests.get(url=url)
    return response.json()

def url_list(response):
    urls=[]
    count=0
    for i in response["items"] :
        if i["is_answered"] :
            urls.append(i["link"])
        count+=1    
        if  count==len(i) :
          break    
    return urls

def open_tabs(urls):
    import webbrowser
    for url in urls:
      webbrowser.open(url)

if __name__=='__main__':
    print("Enter file path for checking errors :")
    filepath=input()
    error_line,error_type=get_error_messages(filepath)
    if error_type is None:
        print("Hurray!!There are no error messages\n Happy Coding")
    else :
        print(f"Error type is {error_type} \t error line on {error_line} \n  ")
        print("Enter no. of tabs you want to access for this answer!!")
        n=int(input())
        if error_type in cache_pages : # Already cached result is present
            urls=cache_pages[error_type]
            print(urls)
            print("Opening chrome browser ...  \n")
            open_tabs(urls) 

        
        
        else :
            response=request_json_data(n,error_type)
            if 'items' in response : # Valid request
              
              urls=url_list(response)
              yes=False
              cache_pages[error_type]=urls
              if urls is None or len(urls)<n:
                  print("Only these Links are available")
                  yes=True
              print(urls)
              print("Opening chrome browser ...  \n")
              open_tabs(urls)    
            else :
              print("You are trying to make a bad request,Please check again")
            
           
            if yes:
                print("Would you like to ask a question in StackOverflow")
                print(create_question(error_type))

        




