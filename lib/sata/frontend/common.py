from lib.sata.common import *

class SATAMasterPort:
	def __init__(self, dw):
		self.source = Source(command_tx_description(dw))
		self.sink = Sink(command_rx_description(dw))

	def connect(self, slave):
		return [
			Record.connect(self.source, slave.sink),
			Record.connect(slave.source, self.sink)
		]

class SATASlavePort:
	def __init__(self, dw):
		self.sink = Sink(command_tx_description(dw))
		self.source = Source(command_rx_description(dw))

	def connect(self, master):
		return [
			Record.connect(self.sink, master.source),
			Record.connect(master.sink, self.source)
		]
