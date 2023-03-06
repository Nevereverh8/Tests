def distribution(a:list):
    b = {1: 0}
    for i in a:
        k = i.split()
        if len(k) in b.keys():
            b[len(k)] += 1
        if len(k) not in b.keys():
            b[len(k)] = 1
    total = 0
    for i in b:
        total += b[i]
    for i in b:
        b[i] = round(b[i]/total*100)
    return b


search_queries = ["watch new movies", "coffee near me", "how to find the determinant", "python", "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing","foreign exchange rates USD/BYN", "Netflix movies watch online free",  "Statistics courses online from top universities"]

distr = distribution(search_queries)
for i in sorted(list(distr.keys())):
    if i == 1:
        print(f"{i} слово: {distr[i]}%")
    elif 2 <= i <= 4:
        print(f"{i} слова: {distr[i]}%")
    else:
        print(f"{i} слов: {distr[i]}%")
