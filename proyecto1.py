#proyecto 1
proyecto = input("Ingrese el nombre del proyecto: ")
horas_estimadas = int(input("Ingrese las horas estimadas para el proyecto: "))
valor_hora = float(input("Ingrese el valor por hora trabajada: "))
plazo_estimado = int(input("Ingrese el plazo estimado en días: "))

print("El nombre del proyecto es: ", proyecto)
print("Las horas estimadas para el proyecto son: ", horas_estimadas)
print("El valor por hora trabajada es: ", valor_hora)
print("El plazo estimado en días es: ", plazo_estimado)

valor_total = int(horas_estimadas) * int(valor_hora)
print("El costo total del proyecto es: ", valor_total)

#generar el pdf del proyecto
#crear un pdf con el nombre del proyecto y el costo total del proyecto
#definir el tipo de letra y el tamaño del texto
#llenar el pdf con el nombre del proyecto y el costo total del proyecto
#guardar el pdf con el nombre del proyecto

#libreria para instalar la libreria para generar el pdf
#"pip install fpdf"

from fpdf import FPDF #importa la clase FPDF de la libreria fpdf para generar el pdf
pdf = FPDF() #crea un objeto pdf
pdf.add_page() #agrega una pagina al pdf
pdf.set_font("Arial", size=12) #define el tipo de letra y el tamaño del texto

##para agragar el template al pdf: para que queda mas bonito el pdf
pdf.image("template.png", x=0, y=0) #agrega una imagen al pdf, en este caso el template, con las coordenadas x e y y el ancho w

#agrega el texto al pdf, con las coordenadas x e y, y el texto a agregar
pdf.text(115, 145, "Nombre del proyecto: " + proyecto)  
pdf.text(115, 160, "horas estimadas: " + str(horas_estimadas))
pdf.text(115, 175, "Valor por hora trabajada: " + str(valor_hora))
pdf.text(115, 190, "Plazo estimado en días: " + str(plazo_estimado))
pdf.text(115, 205, "Valor total: " + str(valor_total))
pdf.text(115, 250, "Gracias por su confianza en nuestro servicio")
pdf.output("presupuesto.pdf") #guarda el pdf con el nombre presupuesto.pdf

