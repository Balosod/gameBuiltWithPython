st = 'Print only the words that start with s in this Sentence'
for list in st.split():
    if list[0].lower() == 's':
        print(list)
