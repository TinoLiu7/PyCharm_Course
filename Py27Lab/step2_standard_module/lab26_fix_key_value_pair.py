def courseInfo(name, duration, instructor):
    print"course name=", name
    print "duration=", duration
    print 'instructor=', instructor
    pass


courseInfo("BDR", 35, "markHo")
courseInfo(name="BDR", duration=35, instructor="markHo")
a1 = {'duration': 35, 'instructor': 'eric cheng', 'name': 'BDPY'}
courseInfo(**a1)
