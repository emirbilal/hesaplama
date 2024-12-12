import math

# Noktaların tanımlanması
points = [(0, 0), (1, 1), (2, 2), (3, 3)]

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafenin bulunması
minimum_distance = min(distances)

# Sonuçların yazdırılması
print("Noktalar:", points)
print("Mesafeler:", distances)
print("Minimum Mesafe:", minimum_distance)
