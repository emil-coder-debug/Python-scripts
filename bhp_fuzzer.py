from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator

from java.util import List , ArrayList
import random

class BurpExtender(IBurpExtender,IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self,callbacks):
        self._callbacks=callbacks
        self._helpers=callbacks.getHelpers()
        callbacks.registerIntruderPayloadGeneratirFactory(self)
        return
    
    def getGeneratorName(self):
        return "BHP Payload Generator"
    def createNewInstance(self,attack):
        return BHPFuzzer(self,attack)
class BHPFuzzer(IIntruderPayloadGenerator):
    def __init__(self,extender,attack):
        self.extender=extender
        self.helpers=extender._helpers
        self.attack=attack
        self.max_payloads=10
        self.num_iterations=0
        return
    def hasMorePayloads(self):
        if self.num_iterations==self.max_payloads:
            return False
        else:
            return True
    def getNextPayload(self,current_payload):
        #convert into a string
        payload="".join(chr(x) for x in current_payload)
        
        #call our simple mutator to fuzz the POST
        payload=self.mutator_payload(payload)

        #increase the number of fuzzing attempts
        self.num_iterations+=1

        return payload
    def reset(self):
        self.num_iterations=0
        return
    