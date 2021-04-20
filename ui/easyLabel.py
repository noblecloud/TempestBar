from PySide6.QtCore import QObject
from PySide6.QtWidgets import QLabel
from WeatherUnits import Measurement


class EasyLabel(QLabel, QObject):
	value: Measurement

	# def __init__(self, *args, **kwargs):
	# 	super(EasyLabel, self).__init__(*args, **kwargs)

	def setMeasurement(self, value: Measurement):
		self.value = value
		if isinstance(value, Measurement):
			if not QObject.property(self, 'showUnit'):
				self.setText(value.str)
			else:
				self.setText(value.withUnit)
		else:
			self.setText(str(value))

	def __call__(self, value: Measurement):
		self.setEnabled(True)
		self.setMeasurement(value)
