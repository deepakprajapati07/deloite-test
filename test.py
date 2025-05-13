# Python functions

from collections import deque

class BaggageSystem:
    def __init__(self):
        self.gates = {}
        
    def bagScanned(self, bagId, destinationGate):
        if destinationGate not in self.gates:
            self.gates[destinationGate] = deque()
        self.gates[destinationGate].append(bagId)
        
    def getNextBagForGate(self, gateNumber):
        if gateNumber in self.gates and self.gates[gateNumber]:
            return self.gates[gateNumber].popleft()
        return None
    
    def getBagsWaitingForGate(self, gateNumber):
        return len(self.gates.get(gateNumber, []))
    
system = BaggageSystem()
system.bagScanned("BAG123", "GATE1")
system.bagScanned("BAG124", "GATE2")
system.bagScanned("BAG125", "GATE3")

print(system.getNextBagForGate("GATE1"))
print(system.getNextBagForGate("GATE1"))
print(system.getNextBagForGate("GATE2"))
print(system.getNextBagForGate("GATE3"))