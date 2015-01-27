#############################################################################
##
##  Copyright (C) 2014 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.wamp import ApplicationSession



class Component(ApplicationSession):
   """
   An application component that subscribes and receives events,
   and stop after having received 5 events.
   """

   @inlineCallbacks
   def onJoin(self, details):
      print("session attached")

      self.received = 0

      def on_event(i):
         print("Got event: {}".format(i))
         self.received += 1
         #if self.received > 5:
         #   self.leave()

      yield self.subscribe(on_event, 'com.myapp.topic1')


   def onDisconnect(self):
      print("disconnected")
      reactor.stop()



if __name__ == '__main__':
   from autobahn.twisted.wamp import ApplicationRunner
   runner = ApplicationRunner("ws://10.81.2.132:8080/ws", "realm1")
   runner.run(Component)


