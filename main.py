import numpy as np
import matplotlib.pyplot as plt

# Dane z tabeli dla Taurean Prince
taurean_points = [55, 22, 15, 47, 31, 11, 60, 36, 24, 50]

# Dane z tabeli dla LeBron James
lebron_points = [53, 12, 32, 12, 43, 21, 31, 25, 23, 13]

# Tworzenie histogramu
plt.hist(taurean_points, bins=range(min(lebron_points), max(taurean_points) + 1), edgecolor='black')

# Dodanie tytułu i etykiet
plt.title('Histogram danych')
plt.xlabel('Wartość')
plt.ylabel('Częstość występowania')

# Pokazanie histogramu
plt.show()
# a. Średnia arytmetyczna
taurean_mean = np.mean(taurean_points)
lebron_mean = np.mean(lebron_points)

# b. Średnia geometryczna
taurean_geo_mean = np.sqrt(np.prod(taurean_points))
lebron_geo_mean = np.sqrt(np.prod(lebron_points))

# c. Wartość modalna
taurean_mode = np.argmax(np.bincount(taurean_points))
lebron_mode = np.argmax(np.bincount(lebron_points))

# d. Wartość środkowa
taurean_median = np.median(taurean_points)
lebron_median = np.median(lebron_points)

# e. Wartości ćwiartkowe (Q1 i Q3)
taurean_q1, taurean_q3 = np.percentile(taurean_points, [25, 75])
lebron_q1, lebron_q3 = np.percentile(lebron_points, [25, 75])

# f. Odchylenie przeciętne
taurean_mad = np.mean(np.abs(taurean_points - taurean_mean))
lebron_mad = np.mean(np.abs(lebron_points - lebron_mean))

# g. Wariancja
taurean_variance = np.var(taurean_points)
lebron_variance = np.var(lebron_points)

# h. Odchylenie standardowe
taurean_std_dev = np.std(taurean_points)
lebron_std_dev = np.std(lebron_points)

# i. Typowy obszar zmienności
taurean_range = np.ptp(taurean_points)
lebron_range = np.ptp(lebron_points)

# j. Odchylenie ćwiartkowe
taurean_iqr = taurean_q3 - taurean_q1
lebron_iqr = lebron_q3 - lebron_q1

# k. Wskaźnik skośności
taurean_skewness = np.mean((taurean_points - taurean_mean)**3) / np.power(taurean_std_dev, 3)
lebron_skewness = np.mean((lebron_points - lebron_mean)**3) / np.power(lebron_std_dev, 3)

# l. Klasyczno-pozycyjny wskaźnik asymetrii
taurean_kurtosis = np.mean((taurean_points - taurean_mean)**4) / np.power(taurean_variance, 2) - 3
lebron_kurtosis = np.mean((lebron_points - lebron_mean)**4) / np.power(lebron_variance, 2) - 3

# m. Pozycyjny wskaźnik asymetrii
taurean_kurtosis_pos = taurean_kurtosis + 3
lebron_kurtosis_pos = lebron_kurtosis + 3

# n. Klasyczny współczynnik asymetrii
taurean_asym_coeff = taurean_skewness / np.sqrt(taurean_kurtosis)
lebron_asym_coeff = lebron_skewness / np.sqrt(lebron_kurtosis)

# o. Współczynnik korelacji Pearsona dla dwóch szeregów zmiennych
correlation_coefficient = np.corrcoef(taurean_points, lebron_points)[0, 1]

# Wyświetlanie wyników
print("a. Średnia arytmetyczna - Taurean:", taurean_mean, "LeBron:", lebron_mean)
print("b. Średnia geometryczna - Taurean:", taurean_geo_mean, "LeBron:", lebron_geo_mean)
print("c. Wartość modalna - Taurean:", taurean_mode, "LeBron:", lebron_mode)
print("d. Wartość środkowa - Taurean:", taurean_median, "LeBron:", lebron_median)
print("e. Wartości ćwiartkowe (Q1 i Q3) - Taurean:", taurean_q1, taurean_q3, "LeBron:", lebron_q1, lebron_q3)
print("f. Odchylenie przeciętne - Taurean:", taurean_mad, "LeBron:", lebron_mad)
print("g. Wariancja - Taurean:", taurean_variance, "LeBron:", lebron_variance)
print("h. Odchylenie standardowe - Taurean:", taurean_std_dev, "LeBron:", lebron_std_dev)
print("i. Typowy obszar zmienności - Taurean:", taurean_range, "LeBron:", lebron_range)
print("j. Odchylenie ćwiartkowe - Taurean:", taurean_iqr, "LeBron:", lebron_iqr)
print("k. Wskaźnik skośności - Taurean:", taurean_skewness, "LeBron:", lebron_skewness)
print("l. Klasyczno-pozycyjny wskaźnik asymetrii - Taurean:", taurean_kurtosis, "LeBron:", lebron_kurtosis)
print("m. Pozycyjny wskaźnik asymetrii - Taurean:", taurean_kurtosis_pos, "LeBron:", lebron_kurtosis_pos)
print("n. Klasyczny współczynnik asymetrii - Taurean:", taurean_asym_coeff, "LeBron:", lebron_asym_coeff)
print("o. Współczynnik korelacji Pearsona -", correlation_coefficient)