// Mismo ejercicio pero esta vez sumando el porcentaje del iva (21%) y el precio en flotante

#include <iostream> 

using namespace std;

int main(){

    int iva = 21;
    float precio, preciofinal = 0;

    cout<<"Ingrese el precio del producto: "; cin>>precio;

    preciofinal = ((iva * 100) / precio) + precio;

    cout<<"El precio final es: " <<preciofinal;

    return 0;
}