# CUSUM New - Formel nach Wikipedia - Orientierung an cusum_felix und test_cusum

import numpy as np
import matplotlib.pyplot as plt
import time as tm



time, event_value = np.loadtxt("Aufgabe7_CUSUM.txt", unpack = True)

print("Der eingelesene Datensatz enthält " + str(len(time)) + " Werte.")

# Eingabe der Teilanzahl des Datensatzes die mit dem Programm getestet werden sollen
number = int(input("Anzahl der zu testenen Daten eingeben: ")) # = len(event_value)
if number > len(time):
    print("Number ist größer als der Datensatz (" + str(len(time)) + " Werte)")
    exit()          # Beendet das Programm, falls _number_ zu groß ist


start = tm.time()

w = np.mean(event_value)                                        # Erwartungswert
print("Der Mittelwert der Messwerte beträgt: " + str(w))


s = [.0] * number
sp = [.0] * number
sn = [.0] * number
time_s = time[:number]
h = 100*w                   # Grenzwert
i = 0
bool = True
boolp = True
booln = True
while i < number:
    if i == 0:
        s[i] = (event_value[i] - w)
        sp[i] = max(0, event_value[i] - w)
        sn[i] = min(0, event_value[i] - w)
    else:
        s[i] = s[i-1] + (event_value[i] - w)
        sp[i] = sp[i-1] + max(0, event_value[i] - w)
        sn[i] = sn[i-1] + min(0, event_value[i] - w)
    if (s[i] < -h or s[i] > h) and bool:
        print("CUSUM an der Stelle  " + str(i) + "  zur Zeit  " + str(time[i]) + "  Minuten ab Start der Sonde.")
        bool = False
    if sp[i] > h and boolp:
        print("CUSUM+ an der Stelle  " + str(i) + "  zur Zeit  " + str(time[i]) + "  Minuten ab Start der Sonde.")
        boolp = False
    if sn[i] < -h and booln:
        print("CUSUM- an der Stelle  " + str(i) + "  zur Zeit  " + str(time[i]) + "  Minuten ab Start der Sonde.")
        booln = False
    i += 1

i -= 1
if bool == True:
    print("Kein CUSUM. s[" + str(i) + "] beträgt: " + str(s[i]))
else:
    print("s[" + str(i) + "] beträgt: " + str(s[i]))
if boolp == True:
    print("Kein CUSUM+. sp[" + str(i) + "] beträgt: " + str(s[i]))
else:
    print("sp[" + str(i) + "] beträgt: " + str(s[i]))
if booln == True:
    print("Kein CUSUM-. sn[" + str(i) + "] beträgt: " + str(s[i]))
else:
    print("sn[" + str(i) + "] beträgt: " + str(s[i]))

# Plotten der Ereignissanzahl (y-Achse) auf die Zeit (x-Achse):
# TODO: Mit Marker und Zeitstempel
plt.plot(time, event_value, "g-",
         time_s, s, "b-",
         time_s, sp, "y-",
         time_s, sn, "r-")
plt.xlabel('Time')
plt.ylabel('Events')


ende = tm.time()
print("Laufzeit: " + '{:5.3f}s'.format(ende-start))

# Zeigen des Plots
plt.show()
