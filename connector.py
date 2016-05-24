
#  Copyright 2016 by Dai Trying
#
#  This file is part of daixmms2client.
#
#     daixmms2client is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     daixmms2client is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with daixmms2client.  If not, see <http://www.gnu.org/licenses/>.


from PyQt5.QtCore import QObject, QSocketNotifier


# noinspection PyPep8Naming
class XMMSConnector(QObject):

    def __init__(self, xmms):
        QObject.__init__(self)
        fd = xmms.get_fd()
        self.xmms = xmms
        self.xmms.set_need_out_fun(self.checkWrite)

        self.rSock = QSocketNotifier(fd, QSocketNotifier.Read, self)
        # noinspection PyUnresolvedReferences
        self.rSock.activated.connect(self.handleRead)
        self.rSock.setEnabled(True)

        self.wSock = QSocketNotifier(fd, QSocketNotifier.Write, self)
        # noinspection PyUnresolvedReferences
        self.wSock.activated.connect(self.handleWrite)
        self.wSock.setEnabled(False)

    # noinspection PyUnusedLocal
    def checkWrite(self, i):
        if self.xmms.want_ioout():
            self.toggleWrite(True)
        else:
            self.toggleWrite(False)

    def toggleRead(self, bool_val):
        # print("toggleRead " + str(bool_val))
        self.rSock.setEnabled(bool_val)

    def toggleWrite(self, bool_val):
        # print("toggleWrite " + str(bool_val))
        self.wSock.setEnabled(bool_val)

    # noinspection PyUnusedLocal
    def handleRead(self, i):
        # print("HandleRead " + str(i))
        self.xmms.ioin()

    # noinspection PyUnusedLocal
    def handleWrite(self, i):
        # print("HandleWrite " + str(i))
        self.xmms.ioout()
