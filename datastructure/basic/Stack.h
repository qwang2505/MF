/*
 * Implementation of stack with LinkedList and Array
 *
 * Methods:
 *  Init
 *  Destroy
 *  Clean
 *  Push
 *  Pop
 */

#ifndef STACK_H_
#define STACK_H_

enum StackType {
    LINKED_LIST = 0,
    ARRAY = 1,
};

struct StackNode{
    void* value;
    StackNode* next;
};

/*
 * Stack facade, support two types: LinkedList and Array
 */
class Stack {

public:
    
    static Stack* Create(StackType type, int maxSize=0);

    static void Destroy(Stack* stack);

public:

    virtual void Init() = 0;

    virtual void Destroy() = 0;

    virtual Stack* Push(void* value) = 0;

    virtual void* Pop() = 0;

};

#endif
