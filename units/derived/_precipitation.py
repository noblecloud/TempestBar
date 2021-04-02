from units.length import Length
from units.time import _Time
from . import _Derived


class Precipitation(_Derived):
	_type = 'precipitationRate'
	_numerator: Length
	_denominator: _Time

	@property
	def fth(self):
		return Precipitation(self._numerator.ft, self._denominator.hr)

	@property
	def inh(self):
		return Precipitation(self._numerator.inch, self._denominator.hr)

	@property
	def ins(self):
		return Precipitation(self._numerator.inch, self._denominator.s)

	@property
	def mmh(self):
		return Precipitation(self._numerator.mm, self._denominator.hr)

	@property
	def mms(self):
		return Precipitation(self._numerator.mm, self._denominator.s)

	@property
	def cmh(self):
		return Precipitation(self._numerator.cm, self._denominator.hr)

	@property
	def mh(self):
		return Precipitation(self._numerator.m, self._denominator.hr)
