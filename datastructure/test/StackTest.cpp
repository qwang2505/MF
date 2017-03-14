/*
 * Test for stack
 */

#include <iostream>

#include "../basic/Stack.h"

using namespace std;

int main(int argc, char* argv[]){
    cout << "hello" << endl;

    Stack* stack = Stack::Create(ARRAY);
    cout << stack << endl;
    return 0;
}
