# -*- coding: utf8 -*-
import requests
import json

rus_text = u'Пролетариат использует свое политическое господство для того, чтобы вырвать у буржуазии шаг за шагом весь капитал, централизовать все орудия производства в руках государства, т. е. пролетариата, организованного как господствующий класс, и возможно более быстро увеличить сумму производительных сил.'

print 'Sent:', rus_text
r = requests.post('http://localhost:5000/ru', data = {'text': rus_text})
j = r.json()
print 'Recv:', ' '.join(j['text'])

print 'Sending garbabe'
r = requests.post('http://localhost:5000/ru', data = {'nothing': None})
print 'Recv:', r
