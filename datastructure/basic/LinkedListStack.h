/*
 * Implement stack with linked list
 */

#ifndef LINKED_LIST_STACK_H_
#define LINKED_LIST_STACK_H_

#include "Stack.h"

class LinkedListStack: public Stack {

public:

    LinkedListStack();

    ~LinkedListStack();
    
    virtual void Init();

    virtual void Destroy();

    virtual Stack* Push(void* value);

    virtual void* Pop();
};

#endif
