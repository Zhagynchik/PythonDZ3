#*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
#В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
#D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
#      А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
#Напишите программу, которая вычисляет стоимость введенного пользователем слова.  Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#*Пример:*
#ноутбук
#12

Slovo=input('Введите слово: ')
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
for i in Slovo:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="l" or i=="n" or i=="s" or i=="t" or i=="r" or i=="а" or i=="в" or i=="е" or i=="и" or i=="н" or i=="о" or i=="р" or i=="с" or i=="т":
        count1+=1
resalt1=count1*1
for i in Slovo:
    if i=="d" or i=="g" or i=="д" or i=="к" or i=="л" or i=="м" or i=="п" or i=="у":
        count2+=1
resalt2=count2*2
for i in Slovo:
    if i=="b" or i=="c" or i=="m" or i=="p" or i=="б" or i=="г" or i=="ё" or i=="ь" or i=="я":
        count3+=1
resalt3=count3*3
for i in Slovo:
    if i=="f" or i=="h" or i=="v" or i=="w" or i=="y" or i=="й" or i=="ы":
        count4+=1
resalt4=count4*4
for i in Slovo:
    if i=="k" or i=="ж" or i=="з" or i=="х" or i=="ц" or i=="ч" :
        count5+=1
resalt5=count5*5
for i in Slovo:
    if i=="j" or i=="x" or i=="ш" or i=="э" or i=="ю":
        count6+=1
resalt6=count6*8
for i in Slovo:
    if i=="q" or i=="z" or i=="ф" or i=="щ" or i=="ъ":
        count7+=1
resalt7=count7*10
print((resalt1+resalt2+resalt3+resalt4+resalt5+resalt6+resalt7), end=' ')
