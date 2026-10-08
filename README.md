Xenia is a trainable chatbot made in python.

It has nothing in it's text files, meaning a clean slate for anyone to use.

NOTE: The Context node isn't finished yet, i'm hoping to add it in the next update.

-------------------------------------------------------------------------------------------------

How to train:

(Note: this assumes you haven't put anything inside the "questions" and "answers" files yet.)

1. Ask it a question.
2. It will then say "I'm not too sure what I should respond with."
3. After the "Type:" prompt comes up, type the answer and click enter. (There should be no white space anywhere other than spaces.)
4. It will then load it into the appropriate files, and remember it.
5. Repeat until finished with training, once you're done, you can optionally replace failRespond()'s with this:


```python
def failRespond():
    print("I'm not sure what you mean, sorry!")
```

(This will turn off it's learning capabilities.)

That is all, thank you.


-HalloweenTrickster
