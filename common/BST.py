#!encoding=utf-8
'''
Created on: Mar 26, 2014

@author: qwang

Implement binary search tree.

如何将树打印出来？
问题根本：如何根据一些规则，将树中的元素合理的放在数组内？
'''

class Node(object):
    '''
    Implement tree node
    '''

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        # store some extra information for debug or test
        self.extra = {}

class BST(object):
    '''
    Implement binary search tree
    '''

    def __init__(self, values):
        self.root = None
        self.count = 0
        for value in values:
            self.insert(value)

    def insert(self, value):
        # TODO if already in tree, do not add count
        self.count += 1
        node = Node(value)
        self.root = self._insert(node, self.root)

    def _insert(self, node, root):
        if root is None:
            return node
        if node.value < root.value:
            root.left = self._insert(node, root.left)
            if root.left == node:
                node.parent = root
        elif node.value > root.value:
            root.right = self._insert(node, root.right)
            if root.right == node:
                node.parent = root
        return root

    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return 0
        return max(self._height(root.left), self._height(root.right)) + 1

    def display(self):
        height = self.height()
        if height == 0:
            return
        print 'Tree View: '
        if height == 1:
            print self.root.value
            return
        rows = height * 2 - 1
        columns = self.count * 2 - 1
        output = []
        for _ in range(rows):
            row = [' '] * columns
            output.append(row)
        self._fill_node(self.root, output, 0, 2)
        '''
        i = 0
        j = 0
        for row in output:
            j = 0
            for e in row:
                if len(e.strip()) == 1:
                    output[i][j] = ' ' + e
                j += 1
            i += 1
        '''
        print '\n'.join([''.join(row) for row in output])

    def _fill_node(self, node, output, row, column):
        if node is None:
            return
        children_row = row + 2
        # really fill
        output[row][column] = '%s' % node.value
        node.extra['row'] = row
        node.extra['column'] = column
        if node.left is not None:
            left_column = column - 2
            while left_column < 0:
                print 'left column: %s, need move, value: %s' % (left_column, node.left.value)
                # move nodes
                self._move(node.left, output)
                left_column += 1
            while output[row+1][left_column-1] != ' ':
                # already occupied, move nodes
                print 'symbol occupied, need move, value: %s' % node.left.value
                self._move(node.left, output)
                left_column += 1
            while output[children_row][left_column-1] != ' ':
                # already occupied, move nodes
                print 'value occupied, need move, value: %s' % node.left.value
                self._move(node.left, output)
                left_column += 1
            while output[children_row][left_column-2] != ' ':
                # already occupied, move nodes
                print 'value occupied, need move, value: %s' % node.left.value
                self._move(node.left, output)
                left_column += 1
            while output[children_row][left_column+1] != ' ':
                # already occupied, move nodes
                print 'value occupied, need move, value: %s' % node.left.value
                self._move(node.left, output)
                left_column += 1
            while output[children_row][left_column+2] != ' ':
                # already occupied, move nodes
                print 'value occupied, need move, value: %s' % node.left.value
                self._move(node.left, output)
                left_column += 1
            while output[children_row][left_column] != ' ':
                # already occupied, move nodes
                print 'value occupied, need move, value: %s' % node.left.value
                self._move(node.left, output)
                left_column += 1
            output[row+1][left_column+1] = '/'
            output[children_row][left_column] = '%s' % node.left.value
            node.left.extra['row'] = children_row
            node.left.extra['column'] = left_column
            self._fill_node(node.left, output, children_row, left_column)
        if node.right is not None:
            column = node.extra['column']
            right_column = column + 2
            output[row+1][column+1] = '\\'
            output[children_row][right_column] = '%s' % node.right.value
            node.right.extra['row'] = children_row
            node.right.extra['column'] = right_column
            self._fill_node(node.right, output, children_row, right_column)

    def _move(self, node, output):
        if node == self.root:
            #row = self.root.extra['row']
            #col = self.root.extra['column']
            #output[row][col], output[row][col+1] = output[row][col+1], output[row][col]
            #self.root.extra['column'] = col + 1
            return
        parent = node.parent
        print 'move %s' % parent.value
        if parent.value < node.value:
            # move node to right
            self._move_right(parent, output, 'right')
        elif parent.value > node.value:
            # move node to right
            self._move_right(parent, output, 'left')
            self._move(parent, output)

    def _move_right(self, node, output, direction):
        print 'move right: %s, direction: %s' % (node.value, direction)
        row = node.extra['row']
        col = node.extra['column']
        # move value
        output[row][col], output[row][col+1] = output[row][col+1], output[row][col]
        node.extra['column'] = col + 1
        # move direction symbol
        if direction == 'left':
            d_col = col - 1
        elif direction == 'right':
            d_col = col + 1
        output[row+1][d_col], output[row+1][d_col+1] = output[row+1][d_col+1], output[row+1][d_col]

if __name__ == '__main__':
    #bst = BST([7, 2, 1, 5, 4, 3, 6, 12, 9, 13, 8, 11, 10, 15, 14, 16])
    bst = BST([17, 12, 11, 15, 14, 13, 16, 112, 19, 113, 18, 111, 110, 115, 114, 116])
    #bst = BST([7, 2, 1, 5, 4, 3, 6, 9, 8])
    #bst = BST([7])
    print bst.count
    print bst.height()
    bst.display()
