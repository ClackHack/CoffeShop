import random as ran, time
print('Welcome to coffee shop simulator infinity challange\n')
print('How many days can you last without going under $5\n')
good = True
coffee = 0
cup = 0
price = 7
day = 0
saletax = 0
comp = 1
end = 14
lose = False


		
		
		
money = ran.uniform(14,35)
money = round(money, 2)
print('You have', money, 'dollars')

def shop(money, cupe, coff):

	lose = False
	mone = money
	print('You have:')
	print(coffee, 'pounds of coffee')
	print(cup, 'cups')
	
	while 1==1:
		mone = round(mone, 2)
		print('\n')
		while 1==1:
			try:
				print('You have', mone, 'dollars')
				if money < 7 + saletax and coffee <= 0:
					lose = True
					print('You Cant buy coffee')
				if money < 5 + saletax and cup <= 0:
					lose = True
					print('You Cant buy cups')
				if lose:
					action = 'l'
					break
				action = input('Press B to buy coffee Beans: $7 per Pound\nPress C to buy cups: 10 for $5\nPress L to leave:\n')
				break
			except EOFError:
			
				print('Try again\n')
				
				
		if action in 'lL':
			break
		elif action in 'bB':
		
			amo = int(input('How many pounds do you want to buy: '))
			if (amo * 7) + saletax > mone:
				print('You dont have that much money')
			else:
				coff = coff + amo
				mone = mone - (7 * amo)
				mone = mone - saletax
				mone = round(mone, 2)
		elif action in 'cC':
		
			amo = int(input('How many sets of 10 cups do you want to buy: '))
			if (amo * 5) + saletax > mone:
				print('You dont have that much money')
				
			else:
				cupam = (amo * 10)
				
				cupe = cupe + cupam
				
				moneam = (5 * amo)
				mone = mone - moneam
				mone = mone - saletax
				mone = round(mone, 2)
		else:
			print('Invalid response')
			
			
	lis = [coff, cupe, mone]
	return lis
	if money < 7 + saletax and coffee <= 0:
		lose = True
		print('You Cant buy coffee')
	if money < 5 + saletax and cup <= 0:
		lose = True
		print('You Cant buy cups')
	if lose:
		lis = [coff, cupe, mone]
	return lis
	
def daysim(temptype, price, mone, coffe, cup,end):
	coff = coffe * 5
	
	if 'l' in temptype:
		tempfact = 1
	elif 'm' in temptype:
		tempfact = 2
	else:
		tempfact = 3
		
		
		
	for i in range(6, end):
		print('\n')
		print('Its' ,i, 'oClock')
		
		print('waiting...')
		time.sleep(3)
		facto = int(tempfact * price * 10 * comp)
		coff = round(coff, 2)
		cup = round(cup, 2)
		
		
		cha = ran.randint(1, facto)
		if cha <= 37:
			print('Someone Bought a cup of coffee!')
			cup = (cup) - 1
			coff = (coff) - 1
			coff = coff
			mone = mone + (price)
		elif cha <= 43:
			print('Someone Bought a cup of coffee!')
			time.sleep(1)
			print('Someone Bought another cup of coffee!')
			mone = mone + (price * 2)
			cup = (cup) - 2
			coff = (coff) - 2
			coff = coff
		else:
			print('No one bought anything')
			
		bre = False
		if coff <= 0:
			coff = 0
			bre = True
			print('You ran out of coffee!')
		if cup <= 0:
			cup = 0
			bre = True
			print('You ran out of Cups!')
		if bre:
			break
			
			
	coff = coff / 5.0
	
	print('\n')
	print('The day ended')
	
	return list([mone, coff, cup])
	
while money > 5:
	day = day + 1
	print('day',day)
	while 1 == 1:
		if lose:
			break
		while 1==1:
			if money < 7 + saletax and coffee <= 0:
				lose = True
				print('You Cant buy coffee')
			if money < 5 + saletax and cup <= 0:
				lose = True
				print('You Cant buy cups')
			if lose:
				break
			try:
			
				print('\n')
				opt = (input('Press S to start day:\nPress B to Buy items:\nPress C to change price of one cup of coffee:\n'))
				break
			except EOFError:
				print('Try again')
				
		print('\n')
		if opt in 'sS':
			if coffee <= 0 or cup <=0:
				print('You need to visit the shop.')
			else:
				break
		elif opt in 'bB':
			set = shop(money, cup, coffee)
			if money < 7 + saletax and coffee <= 0:
				lose = True
				print('You Cant buy coffee')
			if money < 5 + saletax and cup <= 0:
				lose = True
				print('You Cant buy cups')
			if lose:
				break
			coffee = set[0]
			cup = set[1]
			money = set[2]
		elif opt in 'cC':
		
			price = float(input('What do you want your price to be: '))
			
			
		else:
		
			print('Invalid response')
		if lose:
			break
	if lose:
		break
	print('\n')
	temp = ran.randint(20,70)
	print('its' ,temp,'degrees out')
	if temp <= 40:
		tempt = 'l'
	elif temp <= 60:
		tempt = 'm'
	else:
		tempt = 'h'
	setda = [0,0,0]
	setda = list(daysim(tempt, price, money, coffee, cup,end))
	money = setda[0]
	facto = int(day / 2)
	factsal = int(day / 3)
	if facto <= 4:
		facto = 1
	if factsal <= 6:
		factsal = 1
	if money < 25 and day <= 4:
		monloss = int(money/ 20.0) * facto
		saletax = factsal
	elif money < 45 and day <= 8:
		monloss = int(money / 15.0) * facto
		saletax = 2 * factsal
	elif money < 55:
		monloss = (int(money / 10.0) * facto) + 4
		saletax = ((int(money / 10.0) - 1) * factsal)
	else:
		monloss = (int(money / 7.0) * facto) + 5
		saletax = int(money / 10.0) * factsal
	money = money - monloss
	print('\n')
	print('You paid', monloss, 'In property taxes')
	print('You pay', saletax, 'in sales tax!')
	
	
	coffee = setda[1]
	cup = setda[2]
	misfo = ran.randint(1,20)
	if cup >= 1 and misfo <= 3:
		cup = 0
		print('You misplaced your cups and lost all of them!')
	elif coffee >=1 and misfo ==3:
		coffee = 0
		print('Rats ate all your coffee')
	rich = int(250 - money)
	if money > 50 or day > 6:
		push = day - 6
		if push <= 0:
			push = 0
		rich = rich - (10 * push)
		if rich <= 130:
			rich = 130
		cham = ran.randint(1,rich)
		if cham < 30:
			money = money - int(money / 2.0)
			print('The government took 1/2 of your money')
		elif cham < 65:
			print('A new competitor began taking your customers')
			comp = comp + ran.randint(1,2)
		elif cham < 75 and comp!= 1:
			comp = 1
			print('You drove out your competition')
		elif cham < 100:
			end = 10
			print('Labor Unions force you to work a 4 hour day')
		elif cham < 125:
			end = 18
			print('Government forces you to work a 12 hour day')
			
		if day == 9:
			comp = comp + ran.randint(2,4)
			print('A great amount of competition is beginning to arise')
			
	print('\n')
	money = round(money,2)
	print('You have: ')
	print(money,'dollars')
	print('\n')
	coffee = round(coffee, 2)
	cup = round(cup, 2)
	print(coffee,'pounds of coffee')
	print(cup,'cups left')
	print('\n')
print('\n')
print('Game over')
print('You lasted', day,'days')
