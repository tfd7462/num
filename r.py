import random 
r = random.randint(1,100)
count = 0
while True:
	count += 1 
	num = input("請輸入數字:")
	num = int(num)
	if num == r:
		print("終於猜對了")
		break
	elif num > r:
		print("答錯了,比答案還大")
	else:
		print("答錯了,比答案還小")
	print("這是你猜的第",count,"次")