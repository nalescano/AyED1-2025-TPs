ptes_de_urgencia = []
ptes_con_turno = []


def validar_afiliado(nro_afiliado):
    return nro_afiliado >= 1000 and nro_afiliado <= 9999


def validar_motivo(urgencia_o_turno):
    return urgencia_o_turno == 0 or urgencia_o_turno == 1


def registrar_paciente(nro_afiliado, urgencia_o_turno):
    if urgencia_o_turno == 0:
        ptes_de_urgencia.append(nro_afiliado)
    else:
        ptes_con_turno.append(nro_afiliado)

    return ptes_de_urgencia, ptes_con_turno


def administrar_pacientes():
    continuar = True
    
    while continuar:
        nro_afiliado = int(input('ingrese su nro de afiliado (4 digitos) o -1 para terminar: '))

        if nro_afiliado == -1:
            continuar = False

        else:
            if validar_afiliado(nro_afiliado):
                urgencia_o_turno = int(input('0. URGENCIA | 1. TURNO: '))

                if validar_motivo(urgencia_o_turno):
                    registrar_paciente(nro_afiliado, urgencia_o_turno)
                else:
                    print('MOTIVO DE CONSULTA INCORRECTO')
            else: 
                print('ERROR NRO DE AFILIADO!!') 

    return ptes_de_urgencia, ptes_con_turno      


def buscar_afiliadoAtendido(nro_afiliado_buscar, ptes_con_turno, ptes_de_urgencia):
    
    nro_consultas = 0

    for conTurno in ptes_con_turno:
        if conTurno == nro_afiliado_buscar:
            nro_consultas += 1
        
    for deUrgencia in ptes_de_urgencia:
        if deUrgencia == nro_afiliado_buscar:
            nro_consultas += 1
    
    return nro_consultas

        

def main() -> None:

    print('registrar | buscar | salir')
    opciones = input('que accion desea realizar?: ')

    while True:

        if opciones == 'registrar':
            ptes_con_turno, ptes_de_urgencia =  administrar_pacientes()
            print(f'Pacientes con turnos: {ptes_con_turno}')
            print(f'Pacientes atendidos de urgencia: {ptes_de_urgencia}')
        

        elif opciones == 'buscar':
            nro_afiliado_buscar = int('ingrese el nro del afiliado que quiere buscar: ')
            resultado_busqueda = buscar_afiliadoAtendido(nro_afiliado_buscar, ptes_con_turno, ptes_de_urgencia)
            print(f'el paciente {nro_afiliado_buscar} hizo {resultado_busqueda} en total')
        
        elif opciones == 'salir':
            print('saliendo del programa...')
            break
        
        else:
            print('opcion no valida, intente de nuevo.')
        

if __name__ == '__main__':
    main()