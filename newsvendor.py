import numpy as np

#CONST
rounds = 15
low = 51
high = 150
price = 4
cost = 2
salvage_val = 0.5
A_order = 107

def main():
	i = 0
	A_profits = []
	B_profits = []
	while i < rounds:
		print("\n Round ", i+1)
		demand = np.random.randint(low, high)
		order = int(input('order quantity = '))
		#calculating A_profit
		if A_order <= demand:
			A_profit = A_order*(price-cost)
			A_profits.append(A_profit)
		elif A_order > demand:
			A_profit= demand*(price-cost) - (A_order-demand)*salvage_val
			A_profits.append(A_profit)
		#calculating B_profit
		if order <= demand:
			B_profit = order*(price-cost)
			B_profits.append(B_profit)
		elif order > demand:
			B_profit= demand*(price-cost) - (order-demand)*salvage_val
			B_profits.append(B_profit)

		print('demand is ',demand)
		print('A profit is ',A_profit)
		print('B profit is ',B_profit)
		i+=1

	print('\nFINAL RESULT')
	print('Total profits of Student A= ', sum(A_profits))
	print('Total profits of Student B= ', sum(B_profits))
main()


