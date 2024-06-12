// Mismo ejercicio pero esta vez sumando el porcentaje del iva (21%)

#include <iostream> 

using namespace std;

int main(){

    int precio, iva = 21;
    float preciofinal = 0;

    cout<<"Ingrese el precio del producto: "; cin>>precio;

    preciofinal = ((iva * 100) / precio) + precio;

    cout<<"El precio final es: " <<preciofinal;

    return 0;
}