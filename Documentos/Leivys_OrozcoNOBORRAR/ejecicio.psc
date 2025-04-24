Algoritmo sin_titulo
	// crea un algoritmo que calcule el imc de una persona
	
	//Pedimos la estatura y el peso de la persona
	
	
	Escribir "*****BIENVENIDO*****"
	
	Escribir "¿Quiere calcular su indice de masa muscular?"
	Escribir "Escribe 1 si es si, escribe 2 si es no"
	Leer cal_indice
	
	
	
	
	si cal_indice =1 Entonces
		Escribir "Ingresa tu estatura en M"
		Leer estatura
		
		Escribir "Ingresa tu peso en KG"
		Leer peso
		
		indice= peso/(estatura * estatura)
		
		Escribir "Su indice de masa muscular es: ", indice
	SiNo
		Escribir "Gracias por su visita"
	FinSi
	
FinAlgoritmo
