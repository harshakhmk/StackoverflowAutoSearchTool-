
# StackOverflow Auto Search Tool
 
## It is Intended to findout errors in user python program and comeup with best results in stackoverflow answers

### Flow of the program

 1 Users writes a python program whose filename is entered during main file execution  
 2 if errors occur an automatic GET request is made to the Stackoverflow API finding the best  possible solutions for the given error 
 3 The program trys to find out best possible results by opening up the browser with the given links 
 4 if there is no solution user is required to authenticte  before going to ask questionvarious parameters are required from authentication 

### Bonus Feature

####  Maintains a Dict[str:List] which takes in the obtained error type as string and returns back list of urls suitable for the given error 
 
## Here's a demo of its working

<a href="https://user-images.githubusercontent.com/56113657/104712192-444b9d00-5748-11eb-9e6c-383fd3e2dbdc.mp4"> <video controls src="https://user-images.githubusercontent.com/56113657/104712192-444b9d00-5748-11eb-9e6c-383fd3e2dbdc.mp4" width="320" height="240" alt="Demo Video"> </video> </a>
