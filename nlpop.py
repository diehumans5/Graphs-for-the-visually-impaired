

def nlp(text) :
    import openai
    chatstr= ""
    openai.api_key = "YOUR API KEY"
    chatstr = f"Kill previous History and just give me expression don't explain or try to solve '{text}' it should be parsable by python"
    print(chatstr)

    try :
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        res = response['choices'][0]['text']
        res = res.replace('math.','')
        res = res.replace('Math.','')
        res = res.replace('sign','sin')
        return res.replace('^','**')
    except :
        return "please repeat again"

def nlpdes(text):
    import openai
    chatstr= ""
    openai.api_key = "YOUR API KEY"
    chatstr = f"{text} mention just it's domain and range in words in one line"

    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        res = response['choices'][0]['text']
        return res
    except:
        return "please repeat again"

# print(nlp("sin x plus cos x"))

    
