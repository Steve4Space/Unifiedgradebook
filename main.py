import requests, os, codecs

#page to download
requestpage = "https://courses.projectstem.org/courses/75980/grades" #should be changed later, perhaps through input. 

#parameters for the URL, downloading.
#accesses parameter 
PARAMS = os.environ['S4SProjectSTEM API'] #enviormental variable only in repl, should be changed to users api key

r = requests.get(url = requestpage, params = PARAMS)

#file = open("response.html", "a") #remove comment when we work on downloading webpage

#display it, to ensure it looader properly
file = codecs.open("response.html", 'r') #prints out html like C++ prints out errors

print(file.read())

#parse html
os.system('python parse.py')
