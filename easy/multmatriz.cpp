#include <iostream>
#include <stdlib.h>
#include <conio.h>

using namespace std;

int main(){
    int A[3][3], B[3][3],C[3][3], i, j, k;
    cout << "Entre com a primeira matriz: " << "\n";
    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            cin >> A[i][j];
        }
    }

    cout << "Entre com a segunda matriz: " << "\n";
    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            cin >> B[i][j];
        }
    }
    cout << "A multiplicacao desse troco eh: " << "\n";
    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            C[i][j] = 0;
            for (k = 0; k < 3; k++){
                C[i][j] = C[i][j] + (A[i][k])*(B[k][j]);
            }
        }
    }
    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            cout << C[i][j] << " ";
        }
        cout << "\n";
    }



}
