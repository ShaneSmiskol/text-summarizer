# text-summarizer
Just a quick text summarizer algorithm I thought up. Definitely isn't perfect, but it's something.

`SentenceSplitter.py` is required to split the sentences in the input automatically, only that code is by TennisVisuals from StackExchange, not me.

How to use:
``` python
In [41]: start("This is a test paragraph! Woah, cool, test paragraphs, amazing! I'm just trying to fill in the void here with meaningless nonsense, so please bear with me. Haha, I made a bear joke, get it? Wait...I need to talk about something relating to actual bears before I do that, hmm. Oh, well, I thought it was funny, and that's all that matters. Haha, ha, ha...ha...")
Out[41]: 
("I'm just trying to fill in the void here with meaningless nonsense, so please bear with me. Wait...I need to talk about something relating to actual bears before I do that, hmm. Oh, well, I thought it was funny, and that's all that matters.",
 'Reduced by: 33.15%.')
 ```
