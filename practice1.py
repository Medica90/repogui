prince =99
print(prince)
type(3.5)

def convert_to_preferred_format(sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   min = sec // 60
   sec %= 60
   print("seconds value in hours:",hour)
   print("seconds value in minutes:",min)
   return "%02d:%02d:%02d" % (hour, min, sec)

n = 45000
print("Time in preferred format :-",convert_to_preferred_format(n))


b =4
bb =44
bbb =444
print(b+bb+bbb)

guess_me =18946:
number =9
while True:
   if number <guess_me:
      print('too low')
   elif number ==guess_me:
      print('found it!')
      break
   elif number >guess_me:
      print('oops')
      break
   number +=9

   #5 задание мне непонятны условия, соответственно решить не смогла


   a =4
   b =6
   n =value in [1,2,3,4,5,6,7,8,9,10,11]
   c =a+a*0,1**n-1
   while True:
      if c >=b:
         print('found it!')
         break

