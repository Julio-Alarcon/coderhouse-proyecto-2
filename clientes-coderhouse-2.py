class cliente:
    def __init__(self, nombre = '', apellido = '', email = '',  edad = '', pais  = ''):
        self.nombre_ = nombre
        self.apellido_ = apellido
        self.email_ = email
        self.edad_ = edad
        self.pais_ = pais
    def ingresar_datos(self, nombre, apellido, email, edad, pais):
        self.nombre_ = nombre
        self.apellido_ = apellido
        self.email_ = email
        self.edad_ = edad
        self.pais_ = pais
    def __str__(self):
        return 'Usuario: '+str(self.nombre_)+' '+str(self.apellido_)+'\nEmail: '+str(self.email_)+'\nEdad: '+str(self.edad_)+'\nPais: '+str(self.pais_)
    def datos_dict(self):
        return {'nombre':self.nombre_,'apellido':self.apellido_,'email':self.email_,'edad':self.edad_,'pais':self.pais_}

def agregar_cliente(clientes_list_object, cont):
    cantidad = "1"
    while cantidad == "1":
        nombre = str(input("ingrese su nombre: "))
        apellido = str(input("ingrese su apellido: "))
        email = str(input("ingrese su email: "))
        edad = str(input("ingrese su edad: "))
        pais = str(input("ingrese su pais: "))
        if(email and nombre and apellido and edad and pais):
            clientes_list_object.append(cliente())
            clientes_list_object[cont].ingresar_datos(nombre, apellido, email, edad, pais)
            id_object = cont
            print('Ingresado con el ID: '+str(id_object))
            cont = cont+1
        else:
            print('No se a ingresado el cliente, revise que todos los campos esten con los datos correctos')
        cantidad = str(input("ingresar otro si=1 no=2: "))
    return cont

def print_all_client(clientes_list_object):
    numero_clientes = len(clientes_list_object)
    if numero_clientes >= 1:
        print('========Lista de clientes========')
        for client_obj in clientes_list_object:
            if(client_obj != '0'):
                print('ID: '+str(clientes_list_object.index(client_obj))+'\n'+client_obj.__str__()+'\n-----------------')
        print('================')
    else:
        print('-----No hay clientes ingresados-----')

def edit_one_client(clientes_list_object,id_client):
    numero_clientes = len(clientes_list_object)
    if(numero_clientes >= id_client):
        if(clientes_list_object[id_client] != '0'):
            dict_option = {'1':'nombre','2':'apellido','3':'email','4':'edad','5':'pais'}
            dict_data = clientes_list_object[id_client].datos_dict()
            option_edit = str(input('1: Nombre\n2: Apellido\n3: Email\n4: Edad\n5: Pais\n6: Salir\nNumero: '))
            if(option_edit != '6'):
                cambio = str(input('Ingrese nuevo dato: '))
                dict_data[dict_option[option_edit]] = cambio
                clientes_list_object[id_client].ingresar_datos(dict_data['nombre'],dict_data['apellido'],dict_data['email'],dict_data['edad'],dict_data['pais'])
                print('Cambio exitoso')
        else:
            print('El cliente fue eliminado')
    else:
        print('-----No hay cliente con este ID-----')

def print_one_client(clientes_list_object,id_client):
    numero_clientes = len(clientes_list_object)
    if(numero_clientes >= id_client):
        if(clientes_list_object[id_client] != '0'):
            print('========Cliente========'+'\n'+str(clientes_list_object[id_client].datos_dict())+'\n=======================')
        else:
            print('El cliente fue eliminado')
    else:
        print('-----No hay cliente con este ID-----')

def delete_one_client(clientes_list_object,id_client):
    numero_clientes = len(clientes_list_object)
    if(numero_clientes >= id_client):
        if(clientes_list_object[id_client] != '0'):
            clientes_list_object[id_client] = '0'
            print('Cliente eliminado')
        else:
            print('El cliente ya fue eliminado anteriormente')
            
def __main__():
    clientes_list_object = []
    flag_menu = 0
    cont = 0
    id_client = 0
    while(flag_menu == 0):
        option = '0'
        menu_dict = {'1':'agregar_cliente(clientes_list_object,cont)','2':'print_all_client(clientes_list_object)','3':'print_one_client(clientes_list_object,id_client)','4':'delete_one_client(clientes_list_object,id_client)','5':'edit_one_client(clientes_list_object,id_client)'}
        option = str(input('=========MENU=========\n1: Ingresar clientes\n2: Ver clientes\n3: Ver un cliente\n4: Eliminar clientes\n5: Editar cliente\n6: Salir\n=========MENU=========\nNumero: '))
        try:
            if(option != '6'):
                if(option == '1'):
                    cont = eval(menu_dict[option])
                else:
                    if(option == '3' or option == '4' or option == '5'):
                        id_client = int(input('Ingrese ID del cliente: '))
                    eval(menu_dict[option])
            else:
                flag_menu = 1
                print('Saliendo de la app')
        except:
            print('Opcion no valida')

__main__()
