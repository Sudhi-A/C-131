import csv

rows = []

with open("main.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]
print(headers)
print(planet_data_rows[0])

solar_system_planet_count = {}

for planet_data in planet_data_rows:
  if solar_system_planet_count.get(planet_data[11]):
    solar_system_planet_count[planet_data[11]] += 1
  else:
    solar_system_planet_count[planet_data[11]] = 1

print(solar_system_planet_count)

max_solar_system = max(solar_system_planet_count, key=solar_system_planet_count.get)
print("Solar system name with maximum planets:",  max_solar_system)
print("Number of planets:", solar_system_planet_count[max_solar_system])

#KOI-351
temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
  
  planet_mass = planet_data[3]

  if planet_mass.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue
  else:
    planet_mass_value = planet_mass.split(" ")[0]
    planet_mass_ref = planet_mass.split(" ")[1]
    if planet_mass_ref == "Jupiters":
      planet_mass_value = float(planet_mass_value) * 317.8
    planet_data[3] = planet_mass_value

  planet_radius = planet_data[7]

  if planet_radius.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue
  else:
    planet_radius_value = planet_radius.split(" ")[0]
    planet_radius_ref = planet_radius.split(" ")[2]
    if planet_radius_ref == "Jupiter":
      planet_radius_value = float(planet_radius_value) * 11.2
    planet_data[7] = planet_radius_value

print(len(planet_data_rows))

koi_351_planets = []

for planet_data in planet_data_rows:
  if max_solar_system == planet_data[11]:
    koi_351_planets.append(planet_data)

print(len(koi_351_planets))
print(koi_351_planets)


import plotly.express as px

koi_351_planet_masses = []
koi_351_planet_names = []

for planet_data in koi_351_planets:
  koi_351_planet_masses.append(planet_data[3])
  koi_351_planet_names.append(planet_data[1])

# Adding Earth and its mass 
koi_351_planet_masses.append(1)
koi_351_planet_names.append("Earth")

fig = px.bar(x=koi_351_planet_names, y=koi_351_planet_masses)
fig.show()