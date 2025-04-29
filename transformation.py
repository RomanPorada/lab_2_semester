import gzip

with open("input.txt", "rt") as fin:
    content = fin.read()

with gzip.open("input.txt.gz", "wt") as fout:
    fout.write(content)

print("Файл input.txt.gz успішно створено!")
