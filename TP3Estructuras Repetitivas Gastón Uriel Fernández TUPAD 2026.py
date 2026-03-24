# Ejercicio 1— “Caja del Kiosco”/
# Objetivo: Simular una compra con validaciones y cálculo de total.

nombre_cliente = input("Ingrese su nombre de cliente: ").strip()
# Me aseguro de que el nombre contenga solo letras antes de avanzar
while not nombre_cliente.isalpha():
    nombre_cliente = input("Intente con un nombre valido porfavor: ").strip()

cantidad_de_productos = input("Ingrese la cantidad de productos: ").strip()

# Valido que la cantidad sea un número entero positivo para poder iterar
while not cantidad_de_productos.isdigit() or int(cantidad_de_productos) <= 0:
    cantidad_de_productos = input("Intente con un numero entero, porfavor\n"
    "Ingrese la cantidad de productos: ")
cantidad_de_productos = int(cantidad_de_productos)

total_con_descuento = 0
total_sin_descuento = 0

# Recorro uno a uno los productos según la cantidad que me indicaron
for i in range(1, cantidad_de_productos+1):
    precio_producto = input("Ingresa el precio del producto: $").strip()
    while not precio_producto.isdigit():
        precio_producto = input("Ingresa el precio del producto: $")
    
    # Acumulo el precio original para calcular el ahorro más tarde
    total_sin_descuento += int(precio_producto)
    
    descuento_sn = input("El producto tiene descuento? s/n: ").strip().lower()
    # Obligo a que la respuesta sea 's' o 'n'
    while len(descuento_sn) != 1 or descuento_sn not in ["s","n"]:
        print("Opción inválida. Intenta con s/n")
        descuento_sn = input("¿El producto tiene descuento? s/n: ").strip().lower()
    
    if descuento_sn == "s":
        # Aplico un 10% de descuento multiplicando por 0.90
        precio_con_dto = int(precio_producto) * 0.90
        total_con_descuento += precio_con_dto
        print(f"Producto: {i} Precio: ${precio_con_dto} Descuento: {descuento_sn}")
    elif descuento_sn == "n":
        # Sumo el valor íntegro si no hay beneficio aplicado
        total_con_descuento += int(precio_producto)
        print(f"Producto: {i} Precio: ${precio_producto} Descuento: {descuento_sn}")

# Calculo la diferencia final para mostrar cuánto se ahorró el cliente
ahorro_total = total_sin_descuento - total_con_descuento
# Obtengo el valor medio dividiendo el total final por la cantidad de ítems
promedio = total_con_descuento / cantidad_de_productos

print("*"*38)
print(f"Cliente: {nombre_cliente.title()}")
print("*"*38)
print(f"Total con descuento: ${total_con_descuento}")
print(f"Total sin descuento: ${total_sin_descuento}")
print("*"*38)
print(f"Ahorro total: ${ahorro_total}")
print("*"*38)
# Formateo la salida a dos decimales para que parezca un ticket real
print(f"Promedio por producto: ${promedio:.2f}")
print("*"*38)

# Ejercicio 2 — “Acceso al Campus y Menú Seguro”/
# Objetivo: Login con intentos + menú de acciones con validación estricta.

usuario_correcta = "alumno"
clave_correcta = "python123"
intentos = 0
acceder = False

# Controló que el usuario no supere los 3 intentos permitidos
while intentos < 3:
    usuario = input(f"Ingrese su usuario correcto, tiene {3 - intentos} intentos: ").strip()
    clave = input(f"Ingrese su clave correcta, tiene {3 - intentos} intentos: ").strip()
    
    # Verifico que no me dejen los campos en blanco antes de procesar
    if not usuario or not clave:
        print("Error no se permiten campos vacíos")
        continue
    
    # Valido las credenciales y, si coinciden, permito el ingreso rompiendo el bucle
    if usuario == usuario_correcta and clave == clave_correcta:
        print("Ingresando al programa con exito!")
        acceder = True
        break
    
    # Sumo un intento fallido si los datos son incorrectos
    intentos += 1

# Si agoto mis intentos sin éxito, muestro el mensaje de bloqueo
if not acceder:
    print("Su cuenta ha sido bloqueada, contacte a soporte.")

# Solo si logro acceder, despliego el menú principal
if acceder:
    while True:
        print(f"""
        1. Ver estado de inscripción
        2. Cambiar clave
        3. Mostrar mensaje motivacional
        4. Salir"""
        )       
        opcion = input("Ingresa una opción: ").strip()
        
        # Me aseguro de que la opción sea un número válido entre 1 y 4
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            opcion = input("Intenta con una opcion valida.").strip()
        opcion = int(opcion)
        
        if opcion == 1:
            print("-"*40)
            print("Usted está Inscripto!")
            print("-"*40)
        elif opcion == 2:
            print("-"*40)
            nueva_clave = input("Ingresa una nueva clave: ").strip()
            print("-"*40)
            
            # Obligo a que mi nueva clave tenga una extensión mínima de seguridad
            while len(nueva_clave) < 6:
                nueva_clave = input("La clave debe contener minimo 6 caracteres: ").strip()
            
            # Confirmo la clave para evitar errores de escritura del usuario
            confirmar = input("Ingresa nuevamente la clave: ").strip()
            while nueva_clave != confirmar:
                confirmar = input("La clave debe coincidir con la nueva clave: ").strip()
            
            # Actualizo la variable global con la nueva contraseña
            clave_correcta = nueva_clave
            print("-"*40)
            print("Clave correctamente modificada.")
            print("-"*40)
        elif opcion == 3:
            print("-"*70)
            print("""Mensaje motivacional: Sin crisis no hay desafios, sin desafios
la vida es una rutina, una lenta agonía. Albert Einstein.""")
            print("-"*70)
        elif opcion == 4: 
            # Finalizo el programa cerrando el bucle infinito
            print("-"*40)
            print("Saliendo del programa con exito.")
            print("-"*40)
            break

# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

nombre_operador = input("Ingrese su nombre de operador: ").strip()

while not nombre_operador.isalpha():
    nombre_operador = input("Ingrese un nombre valido por favor.").strip()

conteo_lunes = 0
conteo_martes = 0
# Inicio con una coma para que el primer nombre también esté delimitado
nombre_paciente_lunes = ","
nombre_paciente_martes = ","

while True:
    print(f"""
1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema""")
    print("-"*40)
    opcion = (input("Eliga una opcion dentro del menu: ")).strip()
    print("-"*40)
    while not opcion.isdigit() or len(opcion) != 1:
        opcion = input("Eliga una opcion correcta dentro del menu: ")
        print("-"*40)
    if opcion == "5":
        print("Saliendo del programa con exito! ")
        break
    if opcion == "1":
        dia = input(f"Elegir día: presione 1 para Lunes o 2 para Martes.").strip()
        print("-"*40)
        while not dia in ["1","2"]:
            dia = input(f"Elegir día: presione 1 para Lunes o 2 para Martes.").strip()
            print("Intenta con un día entre 1 y 2: ")
            print("-"*40)
        nombre_paciente = input("Ingrese el nombre del paciente: ").strip().title()
        while not nombre_paciente.isalpha():
            nombre_paciente = input("Intente con un nombre valido por favor: ").strip().title()
            print("-"*40)
        
        # Busco ",Nombre," para que sea una coincidencia exacta
        paciente_busqueda = "," + nombre_paciente + ","
        
        if dia == "1":
            if paciente_busqueda in nombre_paciente_lunes:
                # Mantengo la lógica de "tecla para regresar"
                nombre_paciente = input("El paciente ya tiene un turno asignado este día, toca cualquier tecla para regresar al menú principal: ").strip()
            elif conteo_lunes < 4:
                conteo_lunes +=1
                # Guardo el nombre seguido de una coma
                nombre_paciente_lunes += nombre_paciente + ","
                print(f"Turno confirmedo para {nombre_paciente}.")
                print(f"Lunes ya tiene {conteo_lunes} paciente/s anotados.")
                print("-"*40)
            else:
                print(f"Capacidad máxima de turnos para el día Lunes (4 turnos).")
        elif dia == "2":
            if paciente_busqueda in nombre_paciente_martes:
                nombre_paciente = input("El paciente ya tiene un turno asignado este día, toca cualquier tecla para regresar al menú principal: ").strip()
            elif conteo_martes < 3:
                conteo_martes +=1
                nombre_paciente_martes += nombre_paciente + ","
                print(f"Turno confirmado para {nombre_paciente}.")
                print(f"Martes ya tiene {conteo_martes} paciente/s anotados.")
                print("-"*40)
            else:
                print(f"Capacidad máxima de turnos para el día Martes (3 turnos).")
                print("-"*40)
    elif opcion == "2":
        dia_cancelar = input(f"Elegir día para cancelar el turno: presione 1 para Lunes o 2 para Martes: ").strip()
        while not dia_cancelar in ["1","2"]:
            dia_cancelar = input(f"Elegir día: presione 1 para Lunes o 2 para Martes: ").strip()
            print("Intenta con un día entre 1 y 2: ")
            print("-"*40)
        print("-"*40)
        if dia_cancelar == "1":
            if conteo_lunes > 0:
                nombre_paciente = input("Ingrese el nombre del paciente: ").strip().title()
                while not nombre_paciente.isalpha():
                    nombre_paciente = input("Intente con un nombre valido por favor: ").strip().title()
                
                # elimino el nombre exacto usando replace
                p_sacar = "," + nombre_paciente + ","
                if p_sacar in nombre_paciente_lunes:
                    nombre_paciente_lunes = nombre_paciente_lunes.replace(p_sacar, ",")
                    conteo_lunes -= 1
                    print(f"El turno de {nombre_paciente} del día Lunes ha sido cancelado.")
                else:
                    print("El paciente no existe en la lista.")
                print("-"*40)
        elif dia_cancelar == "2":
            if conteo_martes > 0:
                nombre_paciente = input("Ingrese el nombre del paciente: ").strip().title()
                while not nombre_paciente.isalpha():
                    nombre_paciente = input("Intente con un nombre valido por favor: ").strip().title()
                
                # elimino el nombre exacto usando replace
                p_sacar = "," + nombre_paciente + ","
                if p_sacar in nombre_paciente_martes:
                    nombre_paciente_martes = nombre_paciente_martes.replace(p_sacar, ",")
                    conteo_martes -= 1
                    print(f"El turno {nombre_paciente} del día Martes ha sido cancelado.")
                else:
                    print("El paciente no existe en la lista.")
                print("-"*40)
    elif opcion == "3":
        if conteo_lunes == 0:
            print(f"Turno día lunes libre ")
        else:    
            # strip(",") limpia las comas de los bordes para que se vea bien
            print(f"Cantidad de turnos ocupados para el día Lunes: {conteo_lunes}, paciente/s: {nombre_paciente_lunes.strip(',')}.")
            print("-"*40)
        if conteo_martes == 0:
            print(f"Turno día Martes libre ")
        else:    
            print(f"Cantidad de turnos ocupados para el día Martes: {conteo_martes}, paciente/s: {nombre_paciente_martes.strip(',')}.")
            print("-"*40)
    elif opcion == "4":
        # Total de turnos sumo el contador de turnos de los lunes más contador de los martes
        total = conteo_lunes + conteo_martes
        print("############ (Resumen general) #########")
        print("-"*40)
        print(f"Total de turnos ocupados en la semana: {total}")
        print("-"*40)
        if conteo_lunes > conteo_martes:
            print("Dia con mas turnos: Lunes")
            print("-"*40)
        elif conteo_martes > conteo_lunes:
            print("Día con mas turnos: Martes.")
            print("-"*40)
        if conteo_lunes == conteo_martes:
            if total == 0:
                print("No hay turnos registrados.")
                print("-"*40)
            else:
                print(f"Hubo un empate de turnos ({conteo_lunes} cada día).")
                print("-"*40)

# Ejercicio 4 — “Escape Room: La Bóveda” Historia/
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados./
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
opcion = 0 
forzar = 0 

# pido y valido datos ingresados por el usuario
nombre_agente = input("Ingresa tu nombre de Agente: ").strip()
while not nombre_agente.isalpha():
    nombre_agente = input("Ingresa un nombre válido de Agente: ").strip()

# mientras estas condiciones dentro del primer if sean verdaderas el juego continua 

while True:
    if energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:
        print("-" * 40)
        # imprimo una salida que valla dejando un historial de la interaccion con el usuario
        print(f"AGENTE: {nombre_agente} | ENERGÍA: {energia} | TIEMPO: {tiempo}")
        print(f"CERRADURAS: {cerraduras_abiertas} | HACKEO: {codigo_parcial}")
        print("-" * 40)
        print("""1 Forzar cerradura
2 Hackear panel
3 Descansar""")
        print("-" * 40)
        opcion = input("Ingresa una opción del menú: ").strip()
        while not opcion.isdigit() or len(opcion) != 1 or opcion not in ["1","2","3"]:
            opcion = input("Ingresa una opción entre 1, 2 y 3. Escribe un número: ").strip()
        if opcion == "1":
            energia -= 20
            tiempo -= 2
            forzar += 1 
            # Primero evaluo si se bloquea
            if forzar == 3:
                alarma = True
                print("¡Regla Antispam! La cerradura se trabó. NO ABRE y suena la alarma.")
            else:
                # Si NO es el 3er intento, intentamos abrir (una sola vez)
                if energia < 40:
                    print("¡Hay riesgo de alarma!")
                    numero = input("Ingresa un número (1, 2 o 3): ").strip()
                    while not numero.isdigit() or numero not in ["1", "2", "3"]:
                        numero = input("Error. Ingresa solo 1, 2 o 3: ").strip()
                    
                    if numero == "3":
                        alarma = True
                        print("¡Activaste la alarma!")
                    else:
                        cerraduras_abiertas += 1 
                        print(f"Cerradura abierta. Total: {cerraduras_abiertas}")
                else:
                    # Energía alta: abre normalmente
                    cerraduras_abiertas += 1
                    print(f"Cerradura abierta. Total: {cerraduras_abiertas}")
        elif opcion == "2":
            energia -= 10
            tiempo -= 3
            forzar = 0 # corta racha de forzado
            print("Hackeando...")
            for pasos in range(4):
                codigo_parcial += "A"
                print(f"Hackeando el sistema: {codigo_parcial}")
            
            if len(codigo_parcial) >= 8:
                if cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    codigo_parcial = "" # Reset
                    print("¡Código completado, se destrabó una cerradura!")
        elif opcion == "3":
            forzar = 0 # corta racha
            tiempo -= 1
            recuperacion = 15
            if alarma:
                recuperacion -= 10
            energia += recuperacion
            if energia > 100: 
                energia = 100 
            print(f"Descanso completado. Energía actual: {energia}")
    # establezco condiciones de salida y finalizacion del programa
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado, Game over!!. ")
        break
    elif cerraduras_abiertas >= 3:
        print(f"¡Cumpliste la misión, felicidades {nombre_agente}! Abriste todas las cerraduras.")
        break
    elif energia <= 0 or tiempo <= 0 or alarma == True:
        print("La misión falló, te detectaron o agotaste tus recursos.")
        break

# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

vida_del_gladiador = 100
vida_del_enemigo = 100
pociones_de_vida = 3
daño_base_ataque_pesado = 15
daño_base_del_enemigo = 12
turno_gladiador = True

opcion = 0 # Declaro variable para las opciones del menú

# Valido el nombre ingresado que sean solo letras
nombre_gladiador = input("Ingresa tu nombre de Gladiador: ").strip()
while not nombre_gladiador.isalpha():
    nombre_gladiador = input("Error, solo se permiten letras: ").strip()
print("**************BIENVENIDO A LA ARENA****************")
#Inicio un bucle para continuar mostrando las opciones hasta que ambos lleguen a vida 0
while vida_del_gladiador > 0 and vida_del_enemigo > 0:
#imprimo el menú del juego
    
    print(f"""
    Vida actual del gladiador:{nombre_gladiador}: HP: {vida_del_gladiador}
    Vida actual del enemigo: HP: {vida_del_enemigo}
    Pociones restantes de vida: {pociones_de_vida}""")
    print("*"*50)
    print(f"""
*****************ELIGE UNA OPCION*****************
    1. Ataque Pesado
    2. Ráfaga Veloz
    3. Curar""")
    print("*"*50)
    opcion = input("Ingresa una opción para comenzar la batalla: ").strip()#validamos que ingrese una opcion valida
    while not opcion.isdigit() or opcion not in ["1","2","3"]:
        opcion = input("Error, ingresa el número 1, 2 o 3.")
    if opcion == "1":
        if vida_del_enemigo < 20: #utilizo float abajo para convertir en número flotante 
            golpecritico = float(daño_base_ataque_pesado * 1.5)#creo una variable formato float de golpecritico para identificarlo
            vida_del_enemigo -= golpecritico
            vida_del_enemigo = max(0, vida_del_enemigo)
            print("*"*50)
            print(f"""Golpe Crítico!
Vida del enemigo actual: {vida_del_enemigo}, Atacaste al Enemigo! 
por {golpecritico} puntos de daño!!""")
            print("*"*50)
        else:
            vida_del_enemigo -= daño_base_ataque_pesado
            print(f"Atacaste al enemigo por {daño_base_ataque_pesado} puntos")
            print("*"*50)
    elif opcion == "2":
        for rafaga in range(3): # Entro en bucle for para restar la vida del enemigo en cada iteración
            vida_del_enemigo -= 5 #resto la vida del enemigo
            print("Golpe conectado por 5 de daño!")
            print("*"*50)
    elif opcion == "3":
        if pociones_de_vida > 0:
            vida_del_gladiador += 30 #sumo vida al gladiador con pociones
            pociones_de_vida -= 1 #restio pociones usadas
        elif pociones_de_vida == 0:
            print("No te quedan pociones!")
            print("*"*50)
    if vida_del_enemigo > 0:
        vida_del_gladiador -= daño_base_del_enemigo
        print("*"*50)
        print(f"""El enemigo te atacó por 12 puntos de daño!, 
HP Gladiador: {vida_del_gladiador} """)
        print("#################NUEVO TURNO#####################")#se imprime luego de cada acción hasta terminar el juego
if vida_del_gladiador > 0:
    print(f"Victoria!!{nombre_gladiador} has ganado la batalla!! ")
    print("*"*50)
else:
    print(f"Derrota. Has caído en combate.")
    print("*"*50)