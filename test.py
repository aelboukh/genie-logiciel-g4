import codecs
filename = "/home/nas02a/etudiants/inf/uapv1900406/Bureau/t.pdf"
#pdf = codecs.open(filename, "rb", encoding = 'utf-8') 
pdf = codecs.open(filename, "rb", encoding = 'latin1')
for page in pdf:
    print page.encode('utf-8')
