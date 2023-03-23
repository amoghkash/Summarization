import os
import openai


class Model():
  def __init__(self, key):
    self.key = key
    pass

  def summarize(self, text:str):
    openai.api_key = self.key

    text = text + "\ngive me a summary of the text above in four sentences"

    print(text)
    
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=text,
      temperature=0.4,
      max_tokens=200,
      top_p=1.0,      
      frequency_penalty=0.0,
      presence_penalty=1
    )
    return(response.get("choices")[0]["text"])
  
