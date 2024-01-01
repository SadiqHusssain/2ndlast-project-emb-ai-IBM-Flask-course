# Simple Sentiment Analysis using Embedded Watson AI
### Project Description
#### This simple app deployed in python Flask webframework lets you perform sentiment analysis based on test input. It takes advantage of
embedded Watson Ai NLP library for sentiment prediction.
#
### How it works
Basically the scipt takes text to be analyzed as an input text using the app UI. The scipt sends a POST request to the relevant model with the required text and the model will send the appropriate response.
Through NLP, this scipt categorizes words as positive, negative or neutral. and scores the input text accordingly.
```text
example 1:
input: I like Cricket.
output: The given text has been identified as POSITIVE with a score of 0.957617.

example 2:
input : I don't play Cricket.
output: The given text has been identified as NEGATIVE with a score of -0.789115.

example 3:
input: I watch Cricket often.
output:  The given text has been identified as NEUTRAL with a score of 0.

example 4: a bit of error handling:
input: hkfh jsdfkjsa jsdjfk
output: Invalid input ! Try Agian

```
#
Buiding this app is 2nd last assignment in IBM course: [Developing Ai Applications with Flask and python](https://www.coursera.org/learn/python-project-for-ai-application-development)
The course is part of 9 courses series in [IBM Backend Development Professional Certificate](https://www.coursera.org/professional-certificates/ibm-backend-development).
#
### Tasks done:
```text
Task 1: Clone the base project repository
Task 2: Create a sentiment analysis application using Watson NLP library
Task 3: Format the output of the application
Task 4: Package the application
Task 5: Run Unit tests on your application
Task 6: Deploy as web application using Flask
Task 7: Incorporate Error handling
Task 8: Run static code analysis
```
#
<code>These are demo shots of how the application looks & works:</code>
#
![Postive Analysis Shot](/positive-analysis.PNG)
![Negative Analysis Shot](/negative-analysis.PNG)
![Neutral Analysis Shot](/neutral%20analysis.PNG)
![Invalid Input Erro handling Shot](/error%20-invalid%20input.PNG)
