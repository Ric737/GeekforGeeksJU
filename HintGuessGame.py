import random

wordlist= ['Rome','Mumbai','Orange','Kerala']

dic= {'Rome':'Capital City of Italy', 
      'Mumbai':'Capital city of Maharashtra', 
      'Orange':'Fruit which has its name same as its color',
      'Kerala':'State in India known as "Gods own country"'}

word= random.choice(wordlist)
print("Hint: ",dic[word],end="\n\n")

flag=[0 for i in range(len(word))]

while(True):
  f=0
  if f!=0:
    break

  guess=input("\n\nEnter the guess: ");
  guess= guess.capitalize()
  if word==guess:
    print("\n -----You win!-----")
    break

  else: 
    for i in range(len(word)):
      if guess[i]==word[i]:
        flag[i]=1
        print(word[i],end='')
      else:
        print("_" if flag[i]==0 else word[i],end='')
    if all(i==1 for i in flag):
      f=1;
      print("\n\nYou guessed all the letters already!\n -----You win!-----")
      break