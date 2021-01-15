
# StackOverflow Auto Search Tool
 
## It is Intended to findout errors in user python program and comeup with best results in stackoverflow answers

### Flow of the program

** 1 Users writes a python program whose filename is entered during main file execution  **
** 2 if errors occur an automatic GET request is made to the Stackoverflow API finding the best  possible solutions for the given error **
** 3 The program trys to find out best possible results by opening up the browser with the given links **
**  4 if there is no solution user is required to authenticte  before going to ask questionvarious parameters are required from authentication **

### Bonus Feature

*** Maintains a Dict[str:List] which takes in the obtained error type as string and returns back list of urls suitable for the given error ***
 
## Here's a demo of its working
<div style="width:360px;max-width:100%;"><div style="height:0;padding-bottom:56.11%;position:relative;"><iframe width="360" height="202" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameBorder="0" src="https://imgflip.com/embed/4tx2qe"></iframe></div><p><a href="https://imgflip.com/gif/4tx2qe">via Imgflip</a></p></div>

