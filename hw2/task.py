def multiplication_table():
	for i in range(1, n+1):
		print(1, "*", i, "=", i)
	
n = int(input("Введите число n: "))
result = multiplication_table()		
print(result)

# Здесь присутствует и процедурная и структурная парадигма
# Структурная парадигма, поскольку используется for и нет goto.
# Процедурная парадигма, поскольку код оформлен в виде процедуры multiplication_table().