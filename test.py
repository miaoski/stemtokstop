# -*- coding: utf8 -*-
import requests
import json

print 'Sending garbabe'
r = requests.post('http://localhost:5000/ru', data = {'nothing': None})
print 'Recv:', r

text = u'Пролетариат использует свое политическое господство для того, чтобы вырвать у буржуазии шаг за шагом весь капитал, централизовать все орудия производства в руках государства, т. е. пролетариата, организованного как господствующий класс, и возможно более быстро увеличить сумму производительных сил.'

print 'Sent:', text
r = requests.post('http://localhost:5000/ru', data = {'text': text})
j = r.json()
print 'Recv:', ' '.join(j['text'])

text = u'Een spook waart door Europa – het spook van het communisme. Alle machten van het oude Europa hebben zich tot een heilige drijfjacht tegen dit spook verbonden, de paus en de tsaar, Metternich en Guizot, Franse radicalen en Duitse politiemannen.'

print 'Sent:', text
r = requests.post('http://localhost:5000/nl', data = {'text': text})
j = r.json()
print 'Recv:', ' '.join(j['text'])

text = u'A spectre is haunting Europe – the spectre of communism. All the powers of old Europe have entered into a holy alliance to exorcise this spectre: Pope and Tsar, Metternich and Guizot, French Radicals and German police-spies.'

print 'Sent:', text
r = requests.post('http://localhost:5000/en', data = {'text': text})
j = r.json()
print 'Recv:', ' '.join(j['text'])

