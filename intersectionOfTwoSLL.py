class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.nextnode

    def set_data(self, newData):
        self.data = newData

    def set_next(self, newNext):
        self.nextnode = newNext


def getintersection(start1, start2):
    len1 = 0
    len2 = 0
    head1 = temp1 = start1
    head2 = temp2 = start2
    while temp1 != None:
        len1 = len1 + 1
        temp1 = temp1.get_next()
    print "len 1", len1
    while temp2 != None:
        len2 = len2 + 1
        temp2 = temp2.get_next()
    print "len 2", len2
    diff = len1 - len2
    print "diff:", diff
    if diff >= 0:
        tr = head1
        while diff > 0:
            diff = diff - 1
            tr = tr.get_next()
        curr1 = tr
        curr2 = head2
        while curr1.get_data() != curr2.get_data():
            curr1 = curr1.get_next()
            curr2 = curr2.get_next()
        print curr1.get_data()
    else:
        tr = head2
        while diff < 0:
            diff = diff + 1
            tr = tr.get_next()
        curr1 = tr
        curr2 = head1
        while curr1.get_data() != curr2.get_data():
            curr1 = curr1.get_next()
            curr2 = curr2.get_next()
        print curr1.get_data()


if __name__ == '__main__':

    n1 = Node(12)
    n2 = Node(13)
    n3 = Node(14)
    n4 = Node(15)
    n5 = Node(16)
    n6 = Node(17)
    n7 = Node(18)
    n8 = Node(19)
    n9 = Node(20)
    n10 = Node(21)
    n11 = Node(22)
    n12 = Node(23)

    n1.set_next(n2)
    n2.set_next(n3)
    n3.set_next(n4)
    n4.set_next(n5)
    n5.set_next(n6)
    n6.set_next(n7)

    n8.set_next(n9)
    n9.set_next(n10)
    n10.set_next(n5)

    getintersection(n1, n8)