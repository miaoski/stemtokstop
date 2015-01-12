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
    'no': u'Et spøkelse er på ferde i Europa - kommunismens spøkelse. Alle makter i det gamle Europa har forent seg til en hellig hetsjakt motdette spøkelse - paven og tsaren, Metternich og Guizot, franske radikale og tysk politi.',
    'it': u'Uno spettro s’aggira per l’Europa – lo spettro del comunismo. Tutte le potenze della vecchia Europa si sono alleate in una santa battuta di caccia contro questo spettro: papa e zar, Metternich e Guizot, radicali francesi e poliziotti tedeschi.',
    'da': u'Et spøgelse går gennem Europa – kommunismens spøgelse. Alle magter i det gamle Europa har sluttet sig sammen til en hellig klapjagt på dette spøgelse, paven og tsaren, Metternich og Guizot, franske radikale og tysk politi.',
    'de': u'Ein Gespenst geht um in Europa – das Gespenst des Kommunismus. Alle Mächte des alten Europa haben sich zu einer heiligen Hetzjagd gegen dies Gespenst verbündet, der Papst und der Czar, Metternich und Guizot, französische Radikale und deutsche Polizisten.',
    'hu': u'Kísértet járja be Európát – a kommunizmus kísértete. Szent hajszára szövetkezett e kísértet ellen a régi Európának minden hatalma: a pápa és a cár, Metternich és Guizot, francia radikálisok és német rendőrök.',
    'fi': u'Aave kummittelee Euroopassa, kommunismin aave. Kaikki vanhan Euroopan mahdit ovat liittoutuneet pyhään ajojahtiin tätä aavetta vastaan: paavi ja tsaari, Metternich ja Guizot, Ranskan radikaalit ja Saksan poliisit.',
    'pt': u'Anda um espectro pela Europa — o espectro do Comunismo. Todos os poderes da velha Europa se aliaram para uma santa caçada a este espectro, o papa e o tsar, Metternich e Guizot, radicais franceses e polícias alemães.',
    'es': u'Un espectro se cierne sobre Europa: el espectro del comunismo. Contra este espectro se han conjurado en santa jauría todas las potencias de la vieja Europa, el Papa y el zar, Metternich y Guizot, los radicales franceses y los polizontes alemanes.',
    'tr': u"Avrupa'da bir hayalet dolaşıyor - Komünizm hayaleti. Avrupa'nın tüm eski güçleri bu hayalete karşı kutsal bir sürgün avı için ittifak halindeler, Papa ile Çar, Metternich ile Guizot, Fransız radikalleri ile Alman polisleri.",
    'ja': u'ヨーロッパにはお化けが出ます。共産主義というお化けが。古きヨーロッパのすべての権力が、このお化けを祓うため、神聖な同盟に加わっています。教皇とツァー、メッテルニヒとギゾー、フランスの急進派とドイツの密偵。',
    #'cht': u'一個幽靈，共產主義的幽靈，在歐洲遊盪。為了對這個幽靈進行神聖的圍剿，舊歐洲的一切勢力，教皇和沙皇、梅特涅和基佐、法國的激進派和德國的警察，都聯合起來了。',
    #'chs': u'一个幽灵，共产主义的幽灵，在欧洲游荡。为了对这个幽灵进行神圣的围剿，旧欧洲的一切势力，教皇和沙皇、梅特涅和基佐、法国的激进派和德国的警察，都联合起来了。',
    }

for k,v in text.iteritems():
    print
    print 'Sent:', v
    r = requests.post('http://localhost:5000/' + k, data = {'text': v})
    j = r.json()
    print 'Recv:', ' '.join(j['text'])
