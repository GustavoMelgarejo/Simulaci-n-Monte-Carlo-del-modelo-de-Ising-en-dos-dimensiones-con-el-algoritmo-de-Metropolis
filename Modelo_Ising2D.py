import numpy
from collections import defaultdict
from matplotlib import pyplot
import itertools

Longitud_red = 16
J = 1.0e-23
kB = 1.38e-23

sitios = list()
espínes = dict()
nb = defaultdict(list)

for x, y in itertools.product(range(Longitud_red), range(Longitud_red)):
    sitios.append((x,y))
print(sitios)

def configuración_aleatoria():
    for espín in sitios:
        espínes[espín] = numpy.random.choice([-1, 1])

configuración_aleatoria()
print(espínes)

nb = defaultdict(list)
for site in espínes:
    x, y = site
    if x + 1 < Longitud_red:
        nb[site].append(((x + 1) % Longitud_red, y))
    if x - 1 >= 0:
        nb[site].append(((x - 1) % Longitud_red, y))
    if y + 1 < Longitud_red:
        nb[site].append((x, (y + 1) % Longitud_red))
    if y - 1 >= 0:
        nb[site].append((x, (y - 1) % Longitud_red))

def energía_por_sitio(site):
    energía = 0.0
    for nbh in nb[site]:
        energía += espínes[site] * espínes[nbh]
    return -J * energía

def energía_total():
    energía = 0.0
    for site in sitios:
        energía += energía_por_sitio(site)
    return 0.5 * energía

def magnetización():
    mag = 0.0
    for espín in espínes.values():
        mag += espín
    return mag

print("magnetización = ", magnetización())

def metropolis(site, T):
    espín2 = espínes[site]
    Energía2 = energía_por_sitio(site)
    espínes[site] *= -1
    Energía1 = energía_por_sitio(site)
    deltaE = Energía1 - Energía2
    if deltaE <= 0:
        pass
    else:
        if numpy.random.uniform(0, 1) <= numpy.exp(-deltaE/(kB*T)):
            pass
        else:
            espínes[site] *= -1

def monte_carlo(T):
    for i in range(len(sitios)):
        int_rand_site = numpy.random.randint(0, len(sitios))
        rand_site = sitios[int_rand_site]
        metropolis(rand_site, T)

pasos_mc = 2050
T_f = 15.0
T_i = 0.01
pasos_T = 0.1

temps = numpy.arange(T_i, T_f, pasos_T)
energías = numpy.zeros(shape=(len(temps), pasos_mc))
magnetizaciones = numpy.zeros(shape=(len(temps), pasos_mc))
configuración_aleatoria()
for n, T in enumerate(temps):
    for i in range(pasos_mc):
        monte_carlo(T)
        energías[n, i] = energía_total()
        magnetizaciones[n, i] = magnetización()

tau = pasos_mc // 2
energía_media = numpy.mean(energías[:, tau:], axis=1)
magnetización_media = abs(numpy.mean(magnetizaciones[:, tau:], axis=1))

pyplot.figure()
pyplot.plot(energía_media, label="Energía", linestyle=':', color='DarkMagenta', marker='o')
pyplot.legend()
pyplot.xlabel(r"Tiempo ($s$)")
pyplot.ylabel(r"Energía (J)")
pyplot.grid()
pyplot.show()

pyplot.figure()
pyplot.plot(temps, magnetización_media, label="Magnetización", linestyle=':', color='DarkRed', marker='o')
pyplot.legend()
pyplot.xlabel(r"Temperatura ($K$)")
pyplot.ylabel(r"Magnetización ($A/m$)")
pyplot.grid()
pyplot.show()
