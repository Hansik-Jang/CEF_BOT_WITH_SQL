class TeamA:
    def __init__(self):
        self.cap = []
        self.teamlist = []      #멘션으로 저장
        self.st = []
        self.lw = []
        self.rw = []
        self.cam = []
        self.cm = []
        self.cdm = []
        self.lb = []
        self.cb = []
        self.rb = []
        self.gk = []
        self.li = []

    def setCapData(self, member):
        self.cap.append(member)

    def setTeamData(self, member):
        self.teamlist.append(member)

    def getCapData(self):
        return self.cap[0]

    def getTeamData(self):

        return self.teamlist

    '''def setData(self, pos, nickname):
        pos = pos.lower()
        if pos == 'st':
            self.st.append(nickname)
        elif pos == 'lw':
            self.lw.append(nickname)
        elif pos == 'rw':
            self.rw.append(nickname)
        elif pos == 'cam':
            self.cam.append(nickname)
        elif pos == 'cm':
            self.cm.append(nickname)
        elif pos == 'cdm':
            self.cdm.append(nickname)
        elif pos == 'lb':
            self.lb.append(nickname)
        elif pos == 'cb':
            self.cb.append(nickname)
        elif pos == 'rb':
            self.rb.append(nickname)
        elif pos == 'gk':
            self.rb.append(nickname)
        elif pos == 'cap':
            self.cap.append(nickname)'''


    def getData(self, pos):
        pos = pos.lower()
        if pos == 'st':
            return self.st
        elif pos == 'lw':
            return self.st
        elif pos == 'rw':
            return self.st
        elif pos == 'cam':
            return self.st
        elif pos == 'cm':
            return self.st
        elif pos == 'cdm':
            return self.st
        elif pos == 'lb':
            return self.st
        elif pos == 'cb':
            return self.st
        elif pos == 'rb':
            return self.st
        elif pos == 'gk':
            return self.st
        elif pos == 'cap':
            return self.cap[0]

    def printdata(self, form):
        if form == '433':
            text = "내전 A팀 명단\n" + \
                self.lw[0] + "\t\t\t\t" + self.st[0] + "\t\t\t\t" + self.rw[0] + \
                "\t\t" + self.cm[0] + "\t\t" + self.cm[1] + "\n" + \
                self.lb + "\t" + self.cb[0] + "\t" + self.cb[1] + "\t" + self.rb[0] + "\n" + \
                "\t\t\t\t\t" + self.gk[0]
            text2 = "내전 A팀 명단\n" + \
                    "ST - " + self.st[0] + "\n" + \
                    "LW - " + self.lw[0] + "\n" + \
                    "RW - " + self.rw[0] + "\n" + \
                    "CM - " + self.cm[0] + ", " + self.cm[1] + "\n" + \
                    "CDM - " + self.cdm[0] + "\n" + \
                    "LB - " + self.lb[0] + "\n" + \
                    "CB - " + self.cb[0] + ", " + self.cb[1] + "\n" + \
                    "RB - " + self.rb[0] + "\n" + \
                    "GK - " + self.gk[0] + "\n"
            return text

    def resetdata(self):
        self.cap.clear()
        self.teamlist.clear()
        #self.li.append(self.cap, self.st, self.lw, self.rw, self.cam, self.cm, self.cdm, self.lb, self.cb, self.rb, self.gk)
        #for l in self.li:
        #    l.clear()
        #self.li.clear()

class TeamB:
    def __init__(self):
        self.cap = []
        self.teamlist = []
        self.st = []
        self.lw = []
        self.rw = []
        self.cam = []
        self.cm = []
        self.cdm = []
        self.lb = []
        self.cb = []
        self.rb = []
        self.gk = []

    def setCapData(self, member) :
        self.cap.append(member)

    def setTeamData(self, member) :
        self.teamlist.append(member)

    def getCapData(self):
        return self.cap[0]

    def getTeamData(self):
        return self.teamlist

    def setdata(self, pos, nickname):
        pos = pos.lower()
        if pos == 'st':
            self.st.append(nickname)
        elif pos == 'lw':
            self.lw.append(nickname)
        elif pos == 'rw':
            self.rw.append(nickname)
        elif pos == 'cam':
            self.cam.append(nickname)
        elif pos == 'cm':
            self.cm.append(nickname)
        elif pos == 'cdm':
            self.cdm.append(nickname)
        elif pos == 'lb':
            self.lb.append(nickname)
        elif pos == 'cb':
            self.cb.append(nickname)
        elif pos == 'rb':
            self.rb.append(nickname)
        elif pos == 'gk':
            self.rb.append(nickname)

    def resetdata(self):
        self.cap.clear()
        self.teamlist.clear()


class TeamC:
    def __init__(self):
        self.cap = []
        self.teamlist = []
        self.st = []
        self.lw = []
        self.rw = []
        self.cam = []
        self.cm = []
        self.cdm = []
        self.lb = []
        self.cb = []
        self.rb = []
        self.gk = []

    def setCapData(self, member) :
        self.cap.append(member)

    def setTeamData(self, member) :
        self.teamlist.append(member)

    def getCapData(self):
        return self.cap[0]

    def getTeamData(self):
        return self.teamlist

    def resetdata(self) :
        self.cap.clear()
        self.teamlist.clear()

class TeamD:
    def __init__(self):
        self.cap = []
        self.teamlist = []
        self.st = []
        self.lw = []
        self.rw = []
        self.cam = []
        self.cm = []
        self.cdm = []
        self.lb = []
        self.cb = []
        self.rb = []
        self.gk = []

    def setCapData(self, member) :
        self.cap.append(member)

    def setTeamData(self, member) :
        self.teamlist.append(member)

    def getCapData(self):
        return self.cap[0]

    def getTeamData(self):
        return self.teamlist

    def resetdata(self) :
        self.cap.clear()
        self.teamlist.clear()