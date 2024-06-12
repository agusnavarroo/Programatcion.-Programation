// Entrada de datos, se le pide un numero al usuario, se guarda en una variable y se muestra

#include <iostream>

using namespace std;

int main(){

    int numero; // Se define la variable

    cout<<"Ingrese un numero entero: "; // Se le pide el numero al usuario
    cin>>numero; // Se guarda el numero ingresado en la variable que definimos

    cout<<"\nEl numero ingresado fue: "<<numero; // Se muestra el numero ingresado guardado en la variable que definimos

    return 0;
}