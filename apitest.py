<<<<<<< HEAD
import requests

url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
token = "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"

prompt = """
Summarize this text, and list all the important dates below:
The siege of Bukhara took place in February 1220, during the Mongol conquest of the Khwarazmian Empire. Genghis Khan, ruler of the Mongol Empire, had launched a multi-pronged assault on the Khwarazmian Empire ruled by Shah Muhammad II. 
While the Shah planned to defend his major cities individually, the Mongols laid siege to the border town of Otrar and struck further into Khwarazmia. The city of Bukhara was a major centre of trade and culture in the Khwarazmian Empire, but was located far from the border with the Mongol Empire, and so the Shah allocated fewer than 20,000 soldiers to defend it. 
A Mongol force, estimated to number between 30,000 and 50,000 men and commanded by Genghis himself, traversed the Kyzylkum Desert, previously considered impassable for large armies. Bukhara's defenders were caught by surprise and, after a failed sortie, the outer city surrendered within three days on 10 February. Khwarazmian loyalists continued to defend the citadel for less than two weeks, before it was breached and taken. 
The Mongol army killed everybody in the citadel and enslaved most of the city's population. The Mongols appropriated the work of skilled craftsmen and artisans, conscripting other inhabitants into their armies. Although Bukhara was then destroyed by fire, the destruction was relatively mild compared to elsewhere; within a short space of time the city was once again a centre of trade and learning, and it profited greatly from the Pax Mongolica.
"""

headers = {
    'Authorization': f'Bearer {token}'
}

def query(payload):
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": prompt,
    "parameters": {"do_sample": True},
    #"parameters": {"max_new_tokens": 50},
    "options": {"wait_for_model": True, "use_gpu": True},
})

print(output)
=======
print("Hello World")
>>>>>>> 5256d48 (message)
