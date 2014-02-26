from Queue import Queue
import random  ##Usage: random.randrange()
import agents

nationalities = ["United Sates","United Kingdom","Australia"]

## Create queues 
License_q = Queue()
Translation_q = Queue()
Eyetest_q = Queue()
Fail_q = Queue()


## Number of each agent and printer(testing)
printer_num = 5
license_agent = 5
translation_agent = 5
eyetest_agent = 5

##printers = [agents.printer() for i in range(printer_num)]



