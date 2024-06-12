// Le pedimos al usuario dos numeros y mostramos la suma, resta, multiplicacion y division de esos dos numeros

#include <iostream>

using namespace std;

int main(){
    int numero1, numero2, suma = 0, resta = 0, multiplicacion = 0, division = 0; // Declaro todas las variables, y lo hago seguido para ahorrar espacio
    cout<<"Ingrese un numero: "; cin>>numero1; // Le pido al usuario ingresar un numero y lo guardo en la variable numero 1
    cout<<"Ingrese otro numero: "; cin>>numero2; // Lo mismo, pero lo guardo el la variable numero 2

    suma = numero1 + numero2;
    resta = numero1 - numero2;
    multiplicacion = numero1 * numero2;
    division = numero1 / numero2;

    cout<<"La suma de los numeros ingresados es: "<<suma<<endl;
    cout<<"La resta de los numeros ingresados es: "<<resta<<endl;
    cout<<"La multiplicacion de los numeros ingresados es: "<<multiplicacion<<endl;
    cout<<"La division de los numeros ingresados es: "<<division<<endl;

    return 0;
}
