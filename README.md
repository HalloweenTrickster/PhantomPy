PhantomPy is a trainable chatbot made in python.

It has nothing in it's text files, meaning a clean slate for anyone to use.

-------------------------------------------------------------------------------------------------

How to train:

(Note: this assumes you haven't put anything inside the "questions" and "answers" files yet.)

1. Ask it a question.
2. It will then say "I'm not too sure what I should respond with."
3. After the "Type:" prompt comes up, type the answer and click enter. (There should be no white space anywhere other than spaces.)
4. It will then load it into the appropriate files, and remember it.
5. Repeat until finished with training, once you're done, you can optionally replace failRespond() with this:


```python
def failRespond():
    print("I'm not sure what you mean, sorry!")
```

(This will turn off its learning capabilities.)

--------------------------------------------------------------------------------------------------

What's next for the project:

1. Static Context - For better language capabilities.
2. Better text mismatch safety.
3. Go from txt to json - For ease of use.
4. Dynamic Context - Much more difficult, much better language capabilities.