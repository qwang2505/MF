/*
 * Implement stack with array
 */

#ifndef ARRAY_STACK_H_
#define ARRAY_STACK_H_

#include "Stack.h"

class ArrayStack: public Stack {

public:

    ArrayStack(int maxSize=0);

    ~ArrayStack();
    
    virtual void Init();

    virtual void Destroy();

    virtual Stack* Push(void* value);

    virtual void* Pop();

};

#endif
