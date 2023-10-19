#include <iostream>
#include <math.h>
using namespace std;


int suma(int veces, int extra)
{
    int valores[5] = {1, 3, 5, 7, 9};
    int Resultado;
    for (int i = 0; i < veces; i++)
    {
        Resultado =+ 25;
    }
    for (int i = 0; i < extra; i++)
    {
        Resultado = Resultado + valores[i];
    }
    return Resultado;
}



int main()
{
    int numero;
    cin >> numero;
    int valor_E = numero / 5;
    double valor_D = round((((numero / 5.0) - valor_E) * 10)/2);

    cout <<suma(valor_E, valor_D) << endl;
}

