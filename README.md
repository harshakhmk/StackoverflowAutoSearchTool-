
# StackOverflow Auto Search Tool
 
## It is Intended to findout errors in user python program and comeup with best results in stackoverflow answers

### Flow of the program

 1 Users writes a python program whose filename is entered during main file execution  
 2 if errors occur an automatic GET request is made to the Stackoverflow API finding the best  possible solutions for the given error 
 3 The program trys to find out best possible results by opening up the browser with the given links 
 4 if there is no solution user is required to authenticte  before going to ask questionvarious parameters are required from authentication 

### Bonus Feature

*** Maintains a Dict[str:List] which takes in the obtained error type as string and returns back list of urls suitable for the given error ***
 
## Here's a demo of its working

<a href="https://imgflip.com/gif/4tx2qe"> <img src="https://imgflip.com/gif/4tx2qe" alt="Demo Video">  </a>

