__author__ = 'Alexis.Koalla@orange.com'


class Chunk:
    # """ Definition de la classe """

    def __init__(self, id, size, pgid, position):
        self._id = id
        self._size = size
        self._pgid = pgid
        self._position = position


    def getName(self):
        #""" Accesseur """
        return self._name

    def getPgid(self):
        #""" Accesseur """
        return self._pgid

    def getSize(self):
        return self._size

    def getPosition(self):
        return self._position

    def getOsds(self):
        return self._osds

    def addOsd(self, osd):
        self._osds.append(osd);

    def removeOsd(self, osd):
        self._osds.remove(osd)

    def getFirstOsd(self):
        return self._osds[0]

    def getLastOsd(self):
        return self._osds.pop()

        #o1 = Object("/var/lib/ak.txt",20000,["c1","c2","c3"] )
        #print "%s a %s ans" % (o1.getName(),o1.getSize())