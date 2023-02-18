words = set()
news = '''The young woman rifles through a fridge of popsicles, pulling out several to show the camera.
“This is milk flavor – the picture is so cute,” she says in English, pointing to the cartoon packaging with a smile. “And this is peach flavor.”
After finally selecting an ice cream cone, she bites into it, declaring: “The biscuit is very delicious.”
The four-minute video has racked up more than 41,000 views on YouTube, but this is no ordinary vlog. The woman, who calls herself YuMi, lives in North Korea, perhaps the world’s most isolated and secretive nation.
Her YouTube channel, created last June, is one of several social media accounts that have popped up across the internet in the past year or two, in which North Korean residents claim to share their everyday lives.'''
news_list = news.split()
for i in news_list:
    words.add(i)
print(words)