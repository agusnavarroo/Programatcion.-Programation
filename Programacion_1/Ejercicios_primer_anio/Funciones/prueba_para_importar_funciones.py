def encontrar_maximo_de_tres_numeros(numero_uno:int,numero_dos:int,numero_tres:int) :
            if numero_uno > numero_dos and numero_uno > numero_tres :
                numero_mas_grande = numero_uno

            elif numero_dos > numero_uno and numero_dos > numero_tres :
                numero_mas_grande = numero_dos

            else :
                numero_mas_grande = numero_tres

            return numero_mas_grande