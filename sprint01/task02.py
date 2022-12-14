def filterBible(scripture, book, chapter):
    s = []
    for i in scripture:
        if i.startswith(book) and chapter == i[2:5]:
            s.append(i)
    return s
