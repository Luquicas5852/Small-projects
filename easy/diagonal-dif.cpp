#include <iostream>
#include <conio.h>
#include <cstdlib>

using namespace std;

int main(){
    int i, j, a[3][3];
    cout << "Enter with the matrix: \n" << endl;
    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
                cin >> a[i][j];
        }
    }

    //Take the sum of the primary diagonal
    int pd = 0;
    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            if (i == j){
                pd = pd + a[i][j];
            }
        }
    }
    //Take the sum of the secondary diagonal
    int sd = 0;
    j = 2;
    for (i = 0; i < 3; i++){
        sd = sd + a[i][j];
        j = j - 1;
    }

    cout << "\n" << "The matrix is: " << "\n";

    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            cout << a[i][j] << " ";
        }
        cout << "\n";
    }

    cout << "\n" << "The absolute difference between the sum of the primary diagonal and the secondary diagonal is: " << "\n";
    cout << abs(pd - sd);
}
