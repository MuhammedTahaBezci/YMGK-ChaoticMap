import numpy as np
import matplotlib.pyplot as plt

def tent_map(x, r):
    """Tent map fonksiyonu"""
    return r * np.minimum(x, 1-x)

def generate_tent_map_sequence(x0, r, n):
    """Tent map dizisi üreten fonksiyon başlangıç değerinden başlayarak tent mapin n adım hesaplar."""
    sequence = [x0]  # Tent map dizisini saklamak için başlangıç değeri ekleme.
    for _ in range(n-1):  # n-1 kadar iterasyon yapılır. başlangıç değeri zaten eklendi.
        x0 = tent_map(x0, r)  # Tent map fonk kullanılarak yeni değer hesapla.
        sequence.append(x0)  # Yeni değer tent map dizisine ekle.
    return sequence

def plot_tent_map(sequence):
    """Tent map grafiğini çizen fonksiyon"""
    plt.plot(sequence, 'b-', linewidth=0.5)  #
    plt.title('Tent Map')  
    plt.xlabel('İterasyon')  
    plt.ylabel('Değer')  
    plt.show()  

def main():
    """Kullanıcıdan girdi alır ve tent map'ı hesaplar ve çizer."""
    x0 = float(input("Başlangıç değerini girin (0 ile 1 arasında bir sayı): ")) 
    r = float(input("r parametresini girin (örn: 2.5): "))
    n = int(input("İterasyon sayısını girin: ")) 

    # Tent map dizisini oluştur
    sequence = generate_tent_map_sequence(x0, r, n)  # Tent map dizisini hesaplar.

    # Tent map grafiğini çiz
    plot_tent_map(sequence)  # Tent map dizisini bir grafikte gösterir.

if __name__ == "__main__":
    main() 