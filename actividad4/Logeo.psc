Algoritmo sin_titulo
	Definir dia, mes, ano como entero
	Definir dia_act, mes_act, ano_act Como Entero
	dia_act = 22
	mes_act = 4
	ano_act = 2025
	Leer dia
	Leer mes
	Leer ano
	
	Definir dia_transc como entero
	Definir mes_transc Como Entero
	Definir ano_transc Como Entero
	definir suma_dias Como entero
	ano_transc = ano_act - ano
	mes_transc = mes_act - mes
	dia_transc = dia_act -  dia
	
	si ano_transc > 0 Entonces
		suma_dias = 365 * ano_transc
	FinSi
	
	si mes_transc > 0 Entonces
		suma_dias = suma_dias + (30*mes_transc)
	FinSi
	
	Si dia_transc>0 Entonces
		suma_dias = suma_dias + dia_transc
	FinSi
	
	Escribir dia_transc
	Escribir mes_transc
	Escribir ano_transc
	
	si suma_dias<=30
		Entonces
		Escribir "Ok"
	FinSi
FinAlgoritmo
