import proceso
feno_final = proceso.feno_final
feno = proceso.feno

def carac_iguales(x,y):
    car_x = [i for i in feno_final[x]]
    car_y = [i for i in feno_final[y]]
    car_x = car_x[3:]
    car_y = car_y[3:]
    igual = [car_x[i] for i in range(len(car_x)) if car_x[i] == car_y[i]]
    return car_x, car_y, igual

def par_neg(x,y):
    lista = carac_iguales(x,y)[2]
    if len(lista) == 0:
        return True

def par_0(x,y):
    lista = carac_iguales(x,y)[2]
    if len(lista) == 9:
        return True

def par_1(x,y):
    tupla = carac_iguales(x,y)
    carx = tupla[0] #Solo las caracteristicas de la persona del id x y id y
    cary = tupla[1]
    if abs(carx[0] - cary[0]) <= 0.2 and carx[1:5] == cary[1:5] and abs(carx[5] - cary[5]) <= 2 and carx[8] == cary[8]:
        return True

def par_2(x,y):
    tupla = carac_iguales(x,y)
    carx = tupla[0]
    cary = tupla[1]
    if abs(carx[0] - cary[0]) <= 0.5:
        if carx[2:4] == cary[2:4]:
            if abs(carx[5] - cary[5]) <= 4:
                if carx[8] == cary[8]:
                    return True

def par_n(x,y):
    tupla = carac_iguales(x,y)
    carx = tupla[0]
    cary = tupla[1]
    if abs(carx[0] - cary[0]) <= 0.7:
        if carx[3] == cary[3]:
            if abs(carx[5] - cary[5]) <= 6:
                if carx[6][1] - cary[6][1] <= 1:
                    return True
