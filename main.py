from gui.Gui import MyWindow
from PyQt5 import QtWidgets
import sys
import consultas
from errores import NotFound, NotAcceptable, GenomeError, BadRequest

lista_escritura = []
class T03Window(MyWindow):
    def __init__(self):
        super().__init__()

    def process_query(self, query_array):
        # Agrega en pantalla la solucion. Muestra los graficos!!
        for i in range(len(query_array)):
            text = "-------------------- Consulta " + str(i + 1) + \
                   " --------------------" +  "\n"
            lista_escritura.append(text)
            self.add_answer(text)
            if query_array[i][0] == 'pariente_de':
                try:
                    nombre = query_array[i][2]
                    id = consultas.id_getter(nombre)
                    grado = query_array[i][1]
                    lista = consultas.pariente_de(grado, id)
                    for j in range(len(lista)):
                        self.add_answer(lista[j] + '\n')
                        lista_escritura.append((lista[j] + '\n'))
                    if len(lista) == 0:
                        self.add_answer("Error: Not Acceptable" + '\n')
                        self.add_answer(NotFound("Falta Respuesta #NotFound") + '\n')
                        lista_escritura.append(("Falta Respuesta #NotFound" + '\n'))
                except:
                    print(NotFound("No tiene parientes de grado{}".format(query_array[0])))


            elif query_array[i][0] == 'índice_de_tamaño':
                try:
                    id = consultas.id_getter(query_array[i][1])
                    ans = consultas.índice_de_tamaño(id)
                    self.add_answer(ans + '\n')
                    lista_escritura.append((ans + '\n'))
                except:
                    print(NotFound("Error: Not Acceptable"))

            elif query_array[i][0] == 'ascendencia':
                try:
                    nombre = query_array[i][1]
                    id = consultas.id_getter(nombre)
                    lista = consultas.ascendencia(id)
                    lista[0]
                    for j in range(len(lista)):
                        self.add_answer(lista[j] + '\n')
                        lista_escritura.append((lista[j] + '\n'))
                except:
                    print(NotFound("No tiene ascendencia"))
                    self.add_answer('Error: Not Acceptable' + '\n')
                    lista_escritura.append(('Error: Not Acceptable' + '\n'))

            elif query_array[i][0] == 'gemelo_genético':
                self.add_answer('No alcancé a hacerla' + '\n')
                lista_escritura.append(('No alcancé a hacerla' + '\n'))


            elif query_array[i][0] == 'valor_característica':
                try:
                    ans = consultas.valor_característica(query_array[i][1], query_array[i][2])
                    if isinstance(ans, tuple):
                        ans = ans[0]
                    #Convierte la tupla de la guata en un string
                    if type(ans) != list:
                        ans = [ans]
                    for j in range(len(ans)):
                        self.add_answer(str(ans[j]))
                        lista_escritura.append((str(ans[j])))
                        if j < len(ans) -1 :
                            self.add_answer(', ')
                            lista_escritura.append(', ')

                    self.add_answer('\n')
                    lista_escritura.append('\n')
                except:
                    print(NotFound(query_array[i][0], query_array[i][1]))

            elif query_array[i][0] == 'min':
                try:
                    ans = consultas.min(query_array[i][1])
                    self.add_answer(ans + '\n')
                    lista_escritura.append(ans + '\n')
                except:
                    print(NotFound(query_array[i][0], query_array[i][1]))

            elif query_array[i][0] == 'max':
                try:
                    ans = consultas.max(query_array[1])
                    self.add_answer(ans + '\n')
                    lista_escritura.append(ans + '\n')
                except:
                    NotFound("máximo no se puede entregar")

            elif query_array[i][0] == 'prom':
                    ans = consultas.prom(query_array[1])
                    self.add_answer(ans + '\n')
                    lista_escritura.append('\n')
            else:
                print(BadRequest(query_array[i]))


    def save_file(self, query_array):
        # Crea un archivo con la solucion. NO muestra los graficos!!
        file = open('resultados.txt', 'w')
        print("".join(lista_escritura), file = file)
        file.close()

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(value)
        print(traceback)


    sys.__excepthook__ = hook

    app = QtWidgets.QApplication(sys.argv)
    window = T03Window()
    sys.exit(app.exec_())
