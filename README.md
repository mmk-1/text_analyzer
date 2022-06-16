# Text Analyzer
A REST API which can respond to POST requests and will return the analysis result of a given text (with/without filters):  
Word count  
Number of Letters  
Longest word  
Average word length  
Reading Duration in Seconds  
Median word length  
Median word when all words sorted by length  
Top 5 most common words  
Guess the text language (english and turkish only)  

It can have filtering options as well:
```
PATH: /analyze
METHOD: POST
BODY: JSON

SAMPLE: 
POST http://localhost:8080/analyze
REQUEST BODY:
{
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."
    "analysis": ["wordCount", "language"]
}

RESPONSE:
{
    "wordCount": 94,
    "language": "en"
}

```
or get filtering options from URL:
```
http://localhost:8080/analyze?analysis=wordCount,language
```
Based on this task:  
https://gitlab.com/-/snippets/2078938
This was a task 

To start the server run  
``
py main.py
``

 
