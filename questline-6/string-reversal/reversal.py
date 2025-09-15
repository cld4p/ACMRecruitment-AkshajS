s="Palindrome"
reverser1=""
reverser2=""

#recursive method
reverser1=s[::-1]
print(reverser1)

#iteration method
for i in range(len(s)-1,-1,-1):
    reverser2+=s[i]

print(reverser2)
