# -*- coding: utf8 -*-
import requests
import json

print 'Sending garbabe'
r = requests.post('http://localhost:5000/ru', data = {'nothing': None})
print 'Recv:', r

text = {
    'ru': u'Пролетариат использует свое политическое господство для того, чтобы вырвать у буржуазии шаг за шагом весь капитал, централизовать все орудия производства в руках государства, т. е. пролетариата, организованного как господствующий класс, и возможно более быстро увеличить сумму производительных сил.',
    'nl': u'Een spook waart door Europa – het spook van het communisme. Alle machten van het oude Europa hebben zich tot een heilige drijfjacht tegen dit spook verbonden, de paus en de tsaar, Metternich en Guizot, Franse radicalen en Duitse politiemannen.',
    'en': u'A spectre is haunting Europe – the spectre of communism. All the powers of old Europe have entered into a holy alliance to exorcise this spectre: Pope and Tsar, Metternich and Guizot, French Radicals and German police-spies.',
    'fr': u'Un spectre hante l’Europe : le spectre du communisme. Toutes les puissances de la vieille Europe se sont unies en une Sainte-Alliance pour traquer ce spectre : le pape et le tsar, Metternich et Guizot, les radicaux de France et les policiers d’Allemagne.',
    'sv': u'Ett spöke går runt Europa – kommunismens spöke. Alla det gamla Europas makter har förbundit sig till en helig hetsjakt mot detta spöke: påven och tsaren, Metternich och Guizot, franska radikaler och tyska poliser.',
    'it': u'Uno spettro s’aggira per l’Europa – lo spettro del comunismo. Tutte le potenze della vecchia Europa si sono alleate in una santa battuta di caccia contro questo spettro: papa e zar, Metternich e Guizot, radicali francesi e poliziotti tedeschi.',
    'da': u'Et spøgelse går gennem Europa – kommunismens spøgelse. Alle magter i det gamle Europa har sluttet sig sammen til en hellig klapjagt på dette spøgelse, paven og tsaren, Metternich og Guizot, franske radikale og tysk politi.',
    'de': u'Ein Gespenst geht um in Europa – das Gespenst des Kommunismus. Alle Mächte des alten Europa haben sich zu einer heiligen Hetzjagd gegen dies Gespenst verbündet, der Papst und der Czar, Metternich und Guizot, französische Radikale und deutsche Polizisten.',
    }

for k,v in text.iteritems():
    print
    print 'Sent:', v
    r = requests.post('http://localhost:5000/' + k, data = {'text': v})
    j = r.json()
    print 'Recv:', ' '.join(j['text'])
