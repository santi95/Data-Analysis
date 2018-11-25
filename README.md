# Explicación Tarea

## Santiago Muñoz Venezian; santi95

28 de agosto, 2017

Para que sea más facil de corregir, lo que no me funcionó fue:

    1. El testing está a medias
    2. La función gemelo_genetico

Todo el resto funciona super bien y eficientemente gracias al uso
de la materia de funcional

Mi tarea tiene 7 modulos.

    1. datos
    2. proceso
    3. parentesco
    4. consultas
    5. errores
    6. testing
    7. main

Se procesan en este orden: datos < proceso < parentesco < consultas < main < errores < main - testing

#### 1. datos
Podemos ver arriba los namedtuples que vamos a usar
para poder ver los datos de una forma más ordenada.

Luego más adelante podemos ver una serie de funciones.

a. leer_listas(), lee las listas para poder ordenar el codigo geético
y las almacena en un namedtuple

b. obtener_numero_jnicial y obtener_numero_secundario, hacen cosas parecidas. Estas
2 funcionas toman toda una fila de genoma.txt y retorna la posición donde se debe cortar para
extraer el nombre y apellido de la persona.

c. Esta función extrae todos los números del genoma y guarda sus posiciones en el string,
con esas posiciones ordeno el genoma, y creo la namedtuple Person. Esta namedtuple tiene
la siguiente estructura.
Person(numero_unico_persona, nombre, apellido, [gen1, gen2, gen3 ... gen.N]
De esa lista de genes es donde más adelante sacamos los genes que corresponden a cada
atributo.

d. arreglar_lista_asociados agarra la lista leida anteriormente y la deja en formato
de namedtuple lista_datos, separa el id de la lista con una lista de posiciones del genoma.

e. generador_lista_genes. Toma la lista de genes de la namedTuple anterior y
la lista de posiciones para dejarla con el siguiente formato.
Person2(numero_unico_persona, nombre, apellido, [{'AAG' : [gen1, gen2]}, {'GCT' : [...}, ... ]
lista para ser leida y transformada en fenotipo.

f.leer_datos es la que va iterando sobre el generador lector de genomas y
hace que todo se mueva en orden, es una función recursiva

#### 2. proceso
Es bastante simple, no creo que valga la pena revisarla función por función.
Simplemente toma el resultado final de el modulo datos y con simples ifs
lo convierte caracteristicas del fenotipo. Estas características luego son guardadas
en una lista de namedtuples, con toda la información de todas las personas de genomas.txt

#### 3. parentesco
Esta podría requerir un poco más de explicación.

a. carac_iguales: crea 2 listas con las caracteristicas fenotipicas de 2 individuos
'x' e 'y', para poder compararlas con mayor facilidad y hacer los próximos pasos más
eficientes. Retorna una lista de las caracteristicas iguales entre las 2 personas

b. par_neg: si es pariente de grado -1. pedimos la lista de la función anterior, si
su len = 0, no tienen nada igual y retorna True

c. par_0: similar a la anterior solo que el len de la lista tiene que ser igual a la
cantidad de caracteristicas fenotipicas del programa (9)

d. par_1: pariente de grado 1, comparo de manera similar a la primera, pero un poco
más especifico

e. par_2: lo mismo que la anterior, pero con las posiciones pertinentes a la consulta

f. par_n: parecido a lo anterior nuevamente, pero con las nuevas caracteristicas

#### 4. consultas
La mayoría de mis funciones en este modulo pide el id de la persona en vez de su nombre
completo, por facilidad de probar el codigo. Por eso existe la función id_getter(nombre),
que retorna el id de la persona a partir del nombre

a. ascendencia simplemente compara las caracteristicas fenotipcas para las primeras
opciones de ascendencia y luego ve con el genotipo de la persona si es posible que se albino
retorna una lista con todas sus ascendencias

b. indice_de_tamaño: lee el counter de cada uno de los genes y mediante la formula puesta
en el return calcula el número

c. pariente_de: recibe un grado y un id, a partir de un for y una condición de un ciclo anidado
crea la lista de parientes con respecto a si se cumplen las condiciones del modulo anterior

d. vemos el id_getter

e. get_counter era para crear el gemelo_genético, no estaba muy lejos :(

f. gemelo_genético: bu

g. valor_caracteristica: a partir del gen de una persona retornamos su fenotipo.

h. solo_carac: crea una lista de solamente los caracteres de una persona, sin su nombre
ni datos, para compararlo con mayor facilidad. es usado en las proximas funciones

i. min: se me ocurrió hacerlo así para no tener que hacer 2 funciones distitnas
dependiendo de lo que buscaran el minimo para. Si la caracteristica es 0 o 5 quiere
decir que estamos buscando el mínimo de tamaño, y no la menor cantidad de veces
que se repite un fenotipo. El else de luego, se preocupa de sumar la cantidad de
cada uno de los tipos de fenotipos y ver cual es el menor con una lista.

j. max es muy muy parecida a min, pero con el orden invertido del min

k. prom, hago un generador uso una función reduce y lo divido por el len de personas

#### 5. Testing

Es nuevo para mi :( me salió solo la parte de chequear las funciones que estaban bien,
pero no pude arreglarmelas para los errores.

#### 6. Errores

Funcionan bien ahora!

#### 7. Tiene el manejo de errores bastante básico pero funciona bien.
¡¡Se podía usar fors!! un agrado.
Esta función separa los comandos, entra a la condición e intenta llevarla a cabo.
Si es que funciona, la imprime en el gui y además las apenda a un alista que diseñe para
después poder escribir el archivo de texto con facilidad.

Sorry el eterno ReadMe, pero espero que te sirva!
Faltan un par de formalidades, pero la parte de lectura de datos eficientemente funciona.
Tuve que borrar todo el modulo de datos cuando subieron el test1, porque me tiraba un lindo
error de StackOverflow. Tuve que usar mucho más funcional de lo que lo estaba usando y
me terminaron gustando mucho.

Gracias por la paciencia de corregir mi tarea!!


