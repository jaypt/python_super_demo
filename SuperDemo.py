

PRINT_MSG = 'Demo For Super'

class RegularPrinter(object):
    def printer(self, val):
        print 'Regular printer is printing:'
        print 'val is:', val


class Result(RegularPrinter):
    def run_test(self):
        print 'Inside Result'
        print self
        super(Result, self).printer(PRINT_MSG)
        
    def __repr__(self):
        return 'This is based on Class:Result'


class BetterPrinter(RegularPrinter):
    def printer(self, val):
        print 'Better Printer is printing:'
        print '*'*20
        print 'val is:', val
        print 'val reversed is:', ''.join(list(reversed(val)))
        print '*'*20

class BetterResult(Result, BetterPrinter):
    def __repr__(self):
        return 'This is based on Class:BetterResult'


if __name__ == '__main__':
       print '-'*25
       print 'First using regular printer'
       printer = Result()
       printer.run_test()
       print '-'*25
       print '\n'*3
       print '-'*25
       print 'using Better printer'
       printer = BetterResult()
       printer.run_test()
       print '-'*25