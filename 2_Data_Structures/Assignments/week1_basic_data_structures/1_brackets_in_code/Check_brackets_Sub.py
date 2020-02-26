# python3
class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
          raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
          raise Empty('Stack is empty')
        return self._data.pop()

S = ArrayStack()
def find_mismatch(expression):
    opening = '({['
    closing = ')}]'
    accum = 0
    sec = 0
    S = ArrayStack()
    for index, x in enumerate(expression, start=1):
        #accum = accum + 1
        if x in opening:
            S.push((index,x))
        elif x in closing:
            if S.is_empty():
                return index
            j, k = S.pop()
            if closing.index(x) != opening.index(k):
                return index
            #if not S.is_empty():
            #   sec += 1
            #    accum = accum - 2
    if S.is_empty():
        return 'Success'
    else:
        index, x = S.pop()
        return index

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)
    return

if __name__ == "__main__":
    main()