import random

first_names_male = {'Luka': 79455, 'David': 60072, 'Jakov': 48525, 'Filip': 41778, 'Leon': 40696, 'Marko': 39818, 'Damir': 38340, 'Andrej': 38135, 'Mateo': 33541, 'Alen': 33468, 'Ivan': 31799, 'Nikola': 31763, 'Matej': 31734, 'Isak': 31447, 'Matija': 31390, 'Milan': 28911, 'Maksim': 28768, 'Aleksej': 28436, 'Aleksandar': 27174, 'Jan': 26872, 'Andrija': 26861, 'Borna': 26845, 'Arian': 26644, 'Damjan': 26304, 'Noa': 25199, 'Viktor': 24192, 'Petar': 23729, 'Karlo': 23601, 'Mihael': 22665, 'Ante': 22611, 'Dragan': 21565, 'Josip': 21345, 'Davor': 21131, 'Jovan': 20855, 'Vid': 20838, 'Roko': 20788, 'Goran': 20689, 'Boris': 20663, 'Igor': 20444, 'Dejan': 19714, 'Denis': 19615, 'Fran': 19414, 'Emil': 19401, 'Dario': 19395, 'Arijan': 19152, 'Darko': 18609, 'Lovro': 18607, 'Kristijan': 17913, 'Tadej': 17758, 'Martin': 17721, 'Željko': 17694, 'Pavle': 17664, 'Danijel': 17487, 'Lav': 17160, 'Domagoj': 17052, 'Marin': 16814, 'Ilija': 16804, 'Bojan': 16661, 'Robert': 16346, 'Tomislav': 16084, 'Dalibor': 15396, 'Vito': 15375, 'Sanjin': 15144, 'Toma': 15088, 'Veljko': 15086, 'Mateja': 15024, 'Vedran': 14695, 'Niko': 14548, 'Mirko': 14139, 'Mladen': 14073, 'Adam': 13789, 'Toni': 13758, 'Daniel': 13705, 'Branko': 13426, 'Srđan': 13368, 'Vladimir': 13218, 'Zlatan': 12627, 'Stjepan': 12568, 'Vigo': 12362, 'Jasmin': 12008, 'Hrvoje': 11872, 'Janko': 11807, 'Bartol': 11734, 'Erik': 11150, 'Ignjat': 10851, 'Vladan': 10780, 'Božidar': 10732, 'Ivica': 10620, 'Oleg': 10392, 'Ivor': 10229, 'Dražen': 10089, 'Nestor': 9607, 'Lovre': 9447, 'Jakob': 9181, 'Duje': 9155, 'Krešimir': 8868, 'Boško': 8861, 'Zlatko': 8641, 'Miran': 8532, 'Nadežda': 8266, 'Jure': 8237, 'Fabijan': 8182, 'Maks': 8158, 'Boban': 8149, 'Mate': 8046, 'Branislav': 8028, 'Maro': 7908, 'Slavko': 7905, 'Nino': 7881, 'Žarko': 7868, 'Neven': 7731, 'Zdravko': 7650, 'Uglješa': 7646, 'Vinko': 7563, 'Ivo': 7544, 'Marijan': 7543, 'Bartul': 7525, 'Pavel': 7292, 'Željana': 7211, 'Jordan': 7141, 'Šimun': 7113, 'Franjo': 7100, 'Pavao': 7055, 'Adel': 6990, 'Juraj': 6954, 'Stipe': 6915, 'Mislav': 6768, 'Maksimilijan': 6648, 'Zvonimir': 6625, 'Leonid': 6624, 'Frane': 6530, 'Antun': 6526, 'Predrag': 6232, 'Bepo': 6222, 'Aleks': 6210, 'Komnen': 6129, 'Šime': 6049, 'Joakim': 6008, 'Cvita': 5983, 'Mile': 5975, 'Tihomir': 5937, 'Manda': 5873, 'Renato': 5853, 'Vlado': 5821, 'Đuro': 5795, 'Branimir': 5720, 'Matko': 5717, 'Slaven': 5703, 'Jovica': 5676, 'Miron': 5598, 'Velimir': 5544, 'Srećko': 5435, 'Leontina': 5435, 'Andro': 5382, 'Istok': 5336, 'Tomo': 5308, 'Dinko': 5226, 'Ozren': 5177, 'Stanko': 5138, 'Filipa': 5113, 'Dmitar': 5093, 'Rusmir': 5088, 'Danko': 5066, 'Mika': 5061, 'Teofil': 5041, 'Frano': 5009, 'Sandro': 4978, 'Julijan': 4974, 'Drago': 4964, 'Mato': 4959, 'Gordan': 4949, 'Anđelo': 4868, 'Darin': 4867, 'Borislav': 4852, 'Milo': 4836, 'Lucijan': 4830, 'Vjekoslav': 4764, 'Kiril': 4714, 'Valentin': 4709, 'Dorijan': 4708, 'Grigorije': 4683, 'Miro': 4683, 'Irinej': 4660, 'Zdenko': 4652, 'Vlatko': 4597, 'Vitomir': 4563, 'Nađa': 4539, 'Gašpar': 4497, 'Dragoslav': 4478, 'Rino': 4466, 'Grgur': 4462, 'Metodije': 4430, 'Zvonko': 4423, 'Jasenka': 4417, 'Jevrem': 4406, 'Dragoljub': 4348, 'Grga': 4325, 'Krunoslav': 4309, 'Borko': 4260, 'Emilijan': 4221, 'Antonije': 4196, 'Anto': 4189, 'Gvozden': 4175, 'Dositej': 4122, 'Andi': 4110, 'Leonida': 4100, 'Davorin': 4082, 'Arjan': 4058, 'Cvijeta': 4026, 'Jela': 4000, 'Baltazar': 3967, 'Neno': 3946, 'Blaž': 3924, 'Tvrtko': 3886, 'Donat': 3877, 'Alek': 3843, 'Dane': 3826, 'Josif': 3816, 'Veselin': 3765, 'Aksentije': 3733, 'Bratislav': 3721, 'Joško': 3657, 'Jugoslav': 3628, 'Jere': 3592, 'Agaton': 3585, 'Kozma': 3568, 'Isidor': 3555, 'Filimon': 3550, 'Dubravko': 3539, 'Časlav': 3538, 'Obrad': 3530, 'Makarije': 3522, 'Lado': 3508, 'Zoltan': 3471, 'Izidor': 3464, 'Dragomir': 3458, 'Evgenije': 3416, 'Vladislav': 3412, 'Grgo': 3402, 'Tonči': 3387, 'Sotir': 3342, 'Ninoslav': 3297, 'Amfilohije': 3293, 'Kuzma': 3256, 'Jeronim': 3254, 'Anđelko': 3250, 'Sisoje': 3247, 'Miljenko': 3230, 'Romano': 3225, 'Rudi': 3224, 'Georgije': 3200, 'Oto': 3188, 'Teofan': 3181, 'Melkior': 3172, 'Mojmir': 3137, 'Zlatka': 3075, 'Spiridon': 3068, 'Iv': 3049, 'Spasoje': 3021, 'Zrinko': 3005, 'Maroje': 2998, 'Ilarion': 2984, 'Zamfir': 2969, 'Porfirije': 2961, 'Jaroslav': 2948,
                    'Bogoljub': 2926, 'Kuzman': 2925, 'Jadran': 2916, 'Tonći': 2907, 'Haralampije': 2900, 'Jasenko': 2898, 'Vlaho': 2846, 'Oton': 2832, 'Manojlo': 2818, 'Hristodul': 2806, 'Bora': 2790, 'Budimir': 2788, 'Dima': 2787, 'Gaj': 2776, 'Izak': 2741, 'Florijana': 2728, 'Sergije': 2712, 'Milivoj': 2704, 'Tomislava': 2690, 'Šima': 2690, 'Kir': 2642, 'Vela': 2632, 'Jozo': 2632, 'Gorčilo': 2603, 'Tihon': 2590, 'Joksim': 2571, 'Jasen': 2555, 'Zdeslav': 2532, 'Duka': 2524, 'Mio': 2523, 'Matan': 2516, 'Angel': 2515, 'Timotije': 2499, 'Aranđel': 2455, 'Stipan': 2451, 'Javor': 2431, 'Nikodim': 2424, 'Antoni': 2421, 'Jadranko': 2415, 'Gerasim': 2411, 'Dimitar': 2379, 'Darije': 2373, 'Svebor': 2352, 'Prokopije': 2339, 'Vjeko': 2329, 'Tonko': 2310, 'Krsta': 2286, 'Trandafil': 2280, 'Ladislav': 2279, 'Ljudevit': 2278, 'Hariton': 2276, 'Alojz': 2256, 'Vjeran': 2224, 'Vićentije': 2214, 'Trpimir': 2201, 'Mlađan': 2177, 'Prohor': 2169, 'Vatroslav': 2124, 'Gradimir': 2122, 'Kliment': 2104, 'Bisa': 2097, 'Kirilo': 2049, 'Plamen': 2048, 'Zosim': 2042, 'Aleksije': 2010, 'Ljubinko': 2008, 'Apostol': 1986, 'Ninko': 1976, 'Ivko': 1967, 'Smiljan': 1964, 'Đura': 1961, 'Alimpije': 1949, 'Joso': 1938, 'Đuzepe': 1702, 'Apolon': 1922, 'Leontije': 1910, 'Mavro': 1906, 'Nedjeljko': 1892, 'Filotej': 1891, 'Nikifor': 1888, 'Deja': 1883, 'Rodion': 1876, 'Blažen': 1874, 'Filaret': 1871, 'Jasminko': 1870, 'Joanikije': 1855, 'Đurđe': 1831, 'Željan': 1827, 'Damljan': 1809, 'Ban': 1807, 'Fotije': 1793, 'Izvor': 1759, 'Ivša': 1755, 'Stavra': 1744, 'Andras': 1741, 'Milko': 1741, 'Teoktist': 1732, 'Boža': 1720, 'Senko': 1717, 'Nevenko': 1708, 'Pantelejmon': 1705, 'Janićije': 1704, 'Blaženko': 1691, 'Pajsije': 1686, 'Evsevije': 1682, 'Danimir': 1670, 'Epifanije': 1615, 'Damil': 1613, 'Pepo': 1610, 'Visarion': 1605, 'Risim': 1598, 'Hval': 1578, 'Julije': 1573, 'Ive': 1569, 'Stamenko': 1552, 'Svetlan': 1548, 'Karanfil': 1548, 'Gordijan': 1546, 'Hristivoje': 1541, 'Pimen': 1540, 'Vjenčeslav': 1536, 'Tona': 1528, 'Evlogije': 1524, 'Raka': 1520, 'Pahomije': 1509, 'Đenadije': 1498, 'Đunisije': 1492, 'Alenko': 1485, 'Hristifor': 1483, 'Đerasim': 1482, 'Nikanor': 1477, 'Mlađen': 1476, 'Jevrosim': 1471, 'Jaromir': 1462, 'Srd': 1459, 'Dobrivoj': 1459, 'Vijeko': 1456, 'Evstatije': 1448, 'Antonijo': 1447, 'Zlatomir': 1443, 'Trpko': 1439, 'Daroslav': 1438, 'Svemil': 1434, 'Strahimir': 1424, 'Hristoslav': 1419, 'Valera': 1416, 'Je': 1416, 'Ksenofon': 1416, 'Krasimir': 1414, 'Kornelije': 1413, 'Pravoslav': 1398, 'Mitrofan': 1398, 'Anatolije': 1391, 'Hristo': 1391, 'Iraklije': 1384, 'Titos': 1379, 'Srebren': 1369, 'Antek': 1368, 'Valtazar': 1365, 'Uglje': 1362, 'Joža': 1359, 'Pelagije': 1349, 'Svetoslav': 1348, 'Ognje': 1346, 'Tome': 1345, 'Budiša': 1341, 'Jevtimije': 1337, 'Hvaloje': 1334, 'Vaskrsije': 1333, 'Jeftimije': 1331, 'Đurisav': 1329, 'Risantije': 1322, 'Evtimij': 1318, 'Kirik': 1317, 'Hrvoj': 1314, 'Teohar': 1306, 'Danislav': 1299, 'Dragislav': 1298, 'Leposav': 1286, 'Tvrdislav': 1285, 'Stanisav': 1284, 'Hranislavka': 1283, 'Partenije': 1280, 'Ivek': 1271, 'Budislav': 1267, 'Kre': 1264, 'Andel': 1261, 'Budi': 1260, 'Hristofor': 1257, 'Trofim': 1254, 'Držislav': 1246, 'Sevastijan': 1244, 'Jože': 1243, 'Pankratije': 1242, 'Agatonik': 1240, 'Jugoljub': 1239, 'Dobrilo': 1239, 'Gradislav': 1238, 'Krajislav': 1235, 'Anđel': 1232, 'Anko': 1231, 'Perunko': 1230, 'Anastasije': 1227, 'Inokentije': 1225, 'Andelko': 1221, 'Ješa': 1220, 'Časlava': 1219, 'Putislav': 1218, 'Zlatoslav': 1213, 'Dobroljub': 1208, 'Rodislav': 1204, 'Vikentije': 1201, 'Sanjo': 1200, 'Hranisav': 1200, 'Gregur': 1199, 'Bogoboj': 1198, 'Veleslav': 1198, 'Pravdan': 1198, 'Evstratije': 1196, 'Davorko': 1193, 'Bosiljko': 1190, 'Arandel': 1189, 'Vukol': 1189, 'Atanacko': 1188, 'Ljuboslav': 1187, 'Blaža': 1175, 'Ivček': 1171, 'Mateša': 1168, 'Meletije': 1157, 'Hrastimir': 1156, 'Dobromil': 1152, 'Žiroslav': 1140, 'Dimo': 1131, 'Jevstratije': 1124, 'Pribisav': 1118, 'Tonček': 1112, 'Belimir': 1106, 'Držimir': 1105, 'Dmitrofan': 1103, 'Sozont': 1102, 'Zrinislav': 1095, 'Svanislav': 1091, 'Leposlav': 1075, 'Anđelin': 1069, 'Trifon': 1068, 'Javorko': 1064, 'Jevlogije': 1064, 'Bosilj': 1048, 'Jevdokim': 1047, 'Zvjezdoslav': 1035, 'Zvjezdodrag': 1027, 'Predisav': 1019, 'Jugosav': 993, 'Zvezdoslav': 992, 'Jugosavka': 966}

first_names_female = {
    'Ema': 78266,
    'Ana': 68358,
    'Lana': 64460,
    'Mia': 55796,
    'Marija': 53602
}

last_names = {
    'Horvat': 21618,
    'Kovačević': 15160,
    'Babić': 12840,
    'Marić': 11555,
    'Jurić': 11163
}

# kada generiramo djecu, ona mogu biti i muška i ženska
all_first_names = {**first_names_male, **first_names_female}


def choose_random(dct):
    # nasumični odabir imena/prezimena prema težinama, koje su zapravo popularnost imena, odnosno učestalost prezimena
    # što je veća popularnost/učestalost, to je veća šansa za pojavu
    return random.choices(list(dct.keys()), weights=list(dct.values()))[0]


number_of_children = {
    1: 20,
    2: 40,
    3: 30,
    4: 10
}

families = []
k = 100    # generirat ćemo k obitelji
for i in range(k):
    # odabrati nasumično prezime, koje će biti zajedničko prezime obitelji
    last_name = choose_random(last_names)
    fnm = choose_random(first_names_male)    # odabrati nasumično ime oca
    fnf = choose_random(first_names_female)    # odabrati nasumično ime majke
    nc = choose_random(number_of_children)    # odabrati nasumično broj djece
    children = []
    for j in range(nc):
        # odabrati nasumično ime djeteta
        child = choose_random(all_first_names)
        # dok je ime djeteta jednako nekom imenu roditelja ili bratu ili sestri, ponavljati
        while child == fnm or child == fnf or child in children:
            child = choose_random(all_first_names)
        children.append(child)    # dodati u listu djece
    # konstruirati listu imena obitelji, prva dva elementa su roditelji, ostalo djeca
    family = [fnm, fnf] + children
    family = ['%s %s' % (member, last_name)
              for member in family]    # dodati prezime na svako ime
    families.append(family)    # dodati u listu generiranih obitelji

for family in families:
    # svaki element liste families je lista kojoj su na indeksima 0 i 1 roditelji, a na ostalim djeca
    print(family)
