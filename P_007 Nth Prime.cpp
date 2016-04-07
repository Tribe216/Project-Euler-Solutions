#include <iostream>
#include <vector>

using namespace std;

int main () {

    //Assumed upper bound of 10,001st prime is 1000000
    //If this were too small, the counter would not
    //increment up to 10,001 and one could increase the upper bound
    vector<bool> composite_table(1000000,false);

    //First prime is 2
    int prime_seed = 2;

    //finds next prime
    for(int counter = 1; counter < 10001; counter++){

        //Fills index values of table with 1 for each multiple of prime
        for (int multiple = 1; (prime_seed*multiple) < 1000000; multiple++){
            composite_table[prime_seed*multiple] = 1;
        }

        //looks for next prime(next integer whose table index not 1)
        //will increment 10,000th prime before exiting on last leg of outer loop
        while (composite_table[prime_seed] == 1){
            prime_seed++;
        }
    }

    cout << prime_seed << endl;
}
