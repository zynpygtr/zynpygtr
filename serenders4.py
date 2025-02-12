a = input("Adınız nedir?")     #input verileri string olarak alır
b = (input(f"Merhaba {a}, hangi yılda doğdun?"))
print(f"{a}, demek {2025-int(b)} yaşındasın")

print("Merhaba\
      bugün pep kurallarını\
      öğreniyoruz.")     # \ işareti olmadan alt satıra geçemeyiz

# if 

p1 = 80

if p1>90: print("notun süper")    
elif  p1>80: print("notun güzel")     #üstteki bir if veya elif çalışmış ise alttaki elifler ve else çalışmaz
elif   p1>50: print("geçtin")
else: print("kalmışsın")

#bugüün daha çok git-github inceledik
