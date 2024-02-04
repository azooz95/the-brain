from googlesearch import search

a = search("الوكالات المتحدة", advanced=True, num_results=5)

for i in a: 
    print(i)