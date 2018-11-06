from pykakasi import kakasi,wakati

text = "私たちは、新しい流通のステージに向けて、1日1日少しずつ、地道に確実に、当たり前のことを当たり前に行ってまいります。かけがえのない生涯を、夢ある人生をかけるにふさわしいロマンに向かって、トライする仲間がいる会社が、私たちトライアルカンパニーです。"
kakasi = kakasi()
kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
kakasi.setMode("J","a") # Japanese to ascii, default: no conversion
# kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
# kakasi.setMode("s", True) # add space, default: no separator
# kakasi.setMode("C", True) # capitalize, default: no capitalize
conv = kakasi.getConverter()
result = conv.do(text)
wakati = wakati()
conv = wakati.getConverter()
result = conv.do(text)
str1List = result.split(' ')
for i in str1List:
    print(i)
