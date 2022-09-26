import matplotlib.pyplot as plt

x0 = 2  # Populasjon i år 0
M = 300  # Maksimal populasjon
r = 1.2  # Parameter
N = 50  # Antall år

populasjon = [x0]  # Liste til populasjonen
x_gml = x0

for i in range(N):
    x_ny = r * x_gml * (M - x_gml) / M  # Regner ut ny populasjon
    populasjon.append(x_ny)  # Legger til i lista
    print(f"I år {i} er populasjonen {x_ny}.")  # Skriver ut resultatene
    x_gml = x_ny  # Oppdaterer hva som er i fjor

# Plotting
plt.plot(populasjon)
plt.xlabel("År")
plt.ylabel("Populasjon")
plt.show()