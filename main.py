with open("books/frankenstein.txt") as f:
    file_contents = f.read()

wordcount = len(file_contents.split())
def lettercount(string):
    letters = {}
    for i in string:
        i = i.casefold()
        if i in letters and i.isalpha():
            letters[i] += 1
        else:
            letters[i] = 1
    return letters
count = lettercount(file_contents)
count = list(count.items())

count.sort(key=lambda x:x[1], reverse=True)

print("Report to see if I'm doing it right:")
print(f"{wordcount} words found in document.\n")
for i in count:
    print(f"The '{i[0]}' character was found {i[1]} times.")
print("\nEnd of report.")