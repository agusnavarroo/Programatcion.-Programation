// Pedirle a un usuario el precio del producto y mostrar el precio de ese mismo producto mas el impuesto del iva

#include <iostream>

using namespace std;

int main(){

    int precio, preciofinal = 0, iva = 3000;

    cout<<"Ingrese el precio del producto: "; cin>>precio;

    preciofinal = precio + iva;

    cout<<"El precio final es de: "<<preciofinal<<endl;

    return 0;
}