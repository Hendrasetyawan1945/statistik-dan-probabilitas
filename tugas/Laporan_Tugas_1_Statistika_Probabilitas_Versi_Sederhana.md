# LAPORAN TUGAS 1 - INDIVIDU (VERSI SEDERHANA: 2 KOIN & UNIFORM)
## PEMBUKTIAN VARIABEL RANDOM DISKRIT & KONTINU (MANUAL VS PYTHON)

- **Mata Kuliah** : Statistika & Probabilitas (Minggu ke-3)
- **Topik**       : Pembuktian PDF, CDF, dan Peluang Kejadian Menggunakan Perhitungan Manual dan Pemrograman Python
- **Program Studi**: S2 Informatika, Fakultas Teknik, Universitas Negeri Surabaya (UNESA)
- **Dosen Pengampu**: Dr. Wiyli Yustanti, S.Si., M.Kom.
- **Nama Mahasiswa**: HENDRA CAHYO SETIAWAN
- **NIPD / NIM**   : 26051905039

---

## 1. PENDAHULUAN
Laporan ini disusun untuk memenuhi Tugas 1 Individu mata kuliah Statistika & Probabilitas pada materi Pembelajaran Minggu ke-3. Tujuan tugas ini adalah membuktikan konsep dasar Variabel Random Diskrit dan Kontinu melalui perhitungan manual analitik matematis serta memvalidasinya dengan simulasi komputasi numerik menggunakan bahasa pemrograman Python.

Untuk memberikan model matematika yang paling sederhana, intuitif, dan mudah dipahami, dipilih dua studi kasus:
1. **Kasus Diskrit**: Eksperimen Pelemparan 2 Koin Uang Logam Seimbang.
2. **Kasus Kontinu**: Model Waktu Tunggu Paket Data dengan Fungsi Konstan/Uniform $f(x) = 1$ pada interval $[0, 1]$.

---

## 2. STUDI KASUS 1: VARIABEL RANDOM DISKRIT (PELEMPARAN 2 KOIN)

### A. Deskripsi Kasus
Sebuah eksperimen dilakukan dengan melempar **2 koin uang logam yang seimbang** secara bersamaan. Setiap koin memiliki dua sisi: **Gambar ($G$)** dan **Angka ($A$)**.  
Variabel random $X$ didefinisikan sebagai:
$$\boldsymbol{X} = \text{Banyaknya sisi Gambar } (G) \text{ yang muncul}$$

### B. Ruang Sampel ($S$)
Karena ada 2 koin dan masing-masing memiliki 2 kemungkinan sisi, total titik sampel adalah $2^2 = 4$:
$$S = \{AA, AG, GA, GG\}$$

Nilai yang mungkin diambil oleh variabel acak $X$ adalah:
$$X \in \{0, 1, 2\}$$

---

### C. Perhitungan Manual PMF (*Probability Mass Function*)
Probabilitas untuk setiap titik nilai $x$ dihitung dengan rumus:
$$f(x) = P(X = x) = \frac{n(X = x)}{n(S)}$$

1. **Untuk $X = 0$** (Tidak ada Gambar, hanya $\{AA\}$):
   $$n(X = 0) = 1 \implies P(X = 0) = \frac{1}{4} = \mathbf{0.25}$$

2. **Untuk $X = 1$** (Tepat 1 Gambar, yaitu $\{AG, GA\}$):
   $$n(X = 1) = 2 \implies P(X = 1) = \frac{2}{4} = \mathbf{0.50}$$

3. **Untuk $X = 2$** (Semua Gambar, hanya $\{GG\}$):
   $$n(X = 2) = 1 \implies P(X = 2) = \frac{1}{4} = \mathbf{0.25}$$

#### Pembuktian Syarat Sah Fungsi Peluang PMF:
1. **Non-negatif**: $f(x) \ge 0$ untuk setiap $x \in \{0, 1, 2\}$ $\implies$ **Terbukti** (nilainya $0.25$ dan $0.50$).
2. **Total Probabilitas = 1**:
   $$\sum_{x=0}^2 f(x) = f(0) + f(1) + f(2) = 0.25 + 0.50 + 0.25 = \mathbf{1.0}$$
   $\implies$ **Terbukti sah 100%!**

---

### D. Perhitungan Manual CDF (*Cumulative Distribution Function*)
Fungsi distribusi kumulatif $F(x) = P(X \le x) = \sum_{t \le x} f(t)$:
- **Untuk $x < 0$**: $F(x) = 0$
- **Untuk $0 \le x < 1$**: $F(x) = f(0) = \mathbf{0.25}$
- **Untuk $1 \le x < 2$**: $F(x) = f(0) + f(1) = 0.25 + 0.50 = \mathbf{0.75}$
- **Untuk $x \ge 2$**: $F(x) = f(0) + f(1) + f(2) = 0.25 + 0.50 + 0.25 = \mathbf{1.00}$

Grafik CDF diskrit ini membentuk **fungsi tangga (*step function*)** yang melompat naik di titik $x = 0, 1,$ dan $2$.

---

### E. Perhitungan Peluang Kejadian Tertentu
**Pertanyaan**: Berapakah peluang mendapatkan **minimal 1 sisi Gambar** ($P(X \ge 1)$)?

* **Metode Langsung**:
  $$P(X \ge 1) = P(X = 1) + P(X = 2) = 0.50 + 0.25 = \mathbf{0.75}$$

* **Metode Komplemen (menggunakan CDF)**:
  $$P(X \ge 1) = 1 - P(X < 1) = 1 - P(X = 0) = 1 - 0.25 = \mathbf{0.75}$$

Kedua cara perhitungan manual menghasilkan nilai yang sama persis: **$0.75$ (atau $75\%$)**.

---

### F. Implementasi Pemrograman Python (Diskrit 2 Koin)
```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Parameter: 2 koin seimbang (n=2, p=0.5)
n_koin = 2
p_koin = 0.5
x_diskrit = np.array([0, 1, 2])

# 1. Menghitung PMF Binomial: C(n, k) * p^k * (1-p)^(n-k)
pmf_koin = np.array([comb(n_koin, k) * (p_koin**k) * ((1 - p_koin)**(n_koin - k)) for k in x_diskrit])

# 2. Menghitung CDF Kumulatif
cdf_koin = np.cumsum(pmf_koin)

# 3. Menghitung Peluang Minimal 1 Gambar P(X >= 1)
prob_ge_1 = np.sum(pmf_koin[x_diskrit >= 1])

# Visualisasi Grafik PMF dan CDF
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].stem(x_diskrit, pmf_koin, basefmt=" ")
ax[0].set_title('PMF: Pelemparan 2 Koin', fontsize=12)
ax[0].set_xlabel('Banyak Sisi Gambar (X)')
ax[0].set_ylabel('Probabilitas f(x)')
ax[0].set_xticks(x_diskrit)
ax[0].grid(True, linestyle='--', alpha=0.6)

ax[1].step(x_diskrit, cdf_koin, where='mid', color='green', linewidth=2)
ax[1].set_title('CDF: Pelemparan 2 Koin (Fungsi Tangga)', fontsize=12)
ax[1].set_xlabel('Banyak Sisi Gambar (X)')
ax[1].set_ylabel('F(x)')
ax[1].set_xticks(x_diskrit)
ax[1].grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Output Validasi
print("Hasil Komputasi Python (2 Koin):")
for x, p, c in zip(x_diskrit, pmf_koin, cdf_koin):
    print(f"X = {x} | PMF = {p:.4f} | CDF = {c:.4f}")
print(f"Peluang P(X >= 1) = {prob_ge_1:.4f}")
```

---

## 3. STUDI KASUS 2: VARIABEL RANDOM KONTINU (FUNGSI UNIFORM $f(x) = 1$)

### A. Deskripsi Kasus
Sebuah sistem antrian jaringan transmisi mencatat waktu tunggu kedatangan sinyal paket data ($X$, dalam menit) pada interval skala normalisasi antara $0$ hingga $1$ menit. Sinyal memiliki peluang yang sama rata di setiap interval waktu, sehingga dimodelkan dengan fungsi kepadatan peluang konstan (Distribusi Uniform):

$$f(x) = \begin{cases} 1, & 0 \le x \le 1 \\ 0, & \text{di tempat lain} \end{cases}$$

---

### B. Pembuktian Syarat Sah Fungsi Densitas (PDF)
Fungsi $f(x)$ sah menjadi PDF jika memenuhi 2 syarat mutlak:
1. **Non-negatif**:  
   Untuk interval $0 \le x \le 1$, nilai $f(x) = 1 \ge 0$. Untuk di luar interval, $f(x) = 0 \ge 0$.  
   $\implies$ **Syarat 1 Terpenuhi ($f(x) \ge 0, \forall x$)**.

2. **Total Luas Area di Bawah Kurva = 1**:  
   $$\int_{-\infty}^{\infty} f(x)\,dx = \int_{0}^{1} 1\,dx = \left[ x \right]_0^1 = 1 - 0 = \mathbf{1.0}$$
   *(Secara geometri: bidang berbentuk persegi panjang berukuran panjang $1$ dan tinggi $1$, Luas = $1 \times 1 = \mathbf{1.0}$).*  
   $\implies$ **Syarat 2 Terpenuhi (Total Peluang = 1.0)**.

Maka, fungsi $f(x) = 1$ terbukti sah sebagai PDF!

---

### C. Perhitungan Manual CDF (*Cumulative Distribution Function*)
Rumus CDF untuk variabel acak kontinu adalah $F(x) = \int_{-\infty}^{x} f(t)\,dt$:
- **Untuk $x < 0$**: $F(x) = 0$
- **Untuk $0 \le x \le 1$**:
  $$F(x) = \int_{0}^{x} 1\,dt = \left[ t \right]_0^x = \boldsymbol{x}$$
- **Untuk $x > 1$**: $F(x) = 1.0$

Sehingga fungsi distribusi kumulatifnya sangat sederhana dan linier:
$$F(x) = \begin{cases} 0, & x < 0 \\ x, & 0 \le x \le 1 \\ 1, & x > 1 \end{cases}$$

---

### D. Perhitungan Peluang Kejadian Tertentu
**Pertanyaan**: Berapakah peluang waktu tunggu sinyal berada di antara **$0.3$ menit hingga $0.7$ menit** ($P(0.3 \le X \le 0.7)$)?

* **Metode 1: Menggunakan Integral Langsung terhadap PDF**:
  $$P(0.3 \le X \le 0.7) = \int_{0.3}^{0.7} 1\,dx = \left[ x \right]_{0.3}^{0.7} = 0.7 - 0.3 = \mathbf{0.4000}$$

* **Metode 2: Menggunakan Fungsi Kumulatif CDF**:
  $$P(0.3 \le X \le 0.7) = F(0.7) - F(0.3) = 0.7 - 0.3 = \mathbf{0.4000}$$

Kedua metode manual menghasilkan angka yang sama persis: **$0.40$ (atau $40\%$)**.

---

### E. Implementasi Pemrograman Python (Kontinu Uniform)
```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 1. Definisikan fungsi PDF f(x) = 1
def pdf_uniform(x):
    if 0 <= x <= 1:
        return 1.0
    return 0.0

pdf_uniform_vec = np.vectorize(pdf_uniform)

# 2. Definisikan fungsi CDF F(x) = x
def cdf_uniform(x):
    if x < 0: return 0.0
    if x > 1: return 1.0
    res, _ = quad(pdf_uniform, 0, x)
    return res

cdf_uniform_vec = np.vectorize(cdf_uniform)

# 3. Hitung integral numerik
total_luas, _ = quad(pdf_uniform, 0, 1)
prob_interval, _ = quad(pdf_uniform, 0.3, 0.7)

# Visualisasi Grafik PDF dan CDF
x_grid = np.linspace(-0.2, 1.2, 400)
fig, ax = plt.subplots(1, 2, figsize=(11, 4))

ax[0].plot(x_grid, pdf_uniform_vec(x_grid), 'b-', linewidth=2, label='f(x) = 1')
x_fill = np.linspace(0.3, 0.7, 100)
ax[0].fill_between(x_fill, pdf_uniform_vec(x_fill), color='orange', alpha=0.5, label='P(0.3 <= X <= 0.7) = 0.40')
ax[0].set_title('PDF: Distribusi Uniform f(x)=1', fontsize=12)
ax[0].set_xlabel('x (Menit)')
ax[0].set_ylabel('f(x)')
ax[0].set_ylim(-0.1, 1.3)
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].legend()

ax[1].plot(x_grid, cdf_uniform_vec(x_grid), 'g-', linewidth=2, label='F(x) = x')
ax[1].set_title('CDF: Fungsi Kumulatif F(x)=x', fontsize=12)
ax[1].set_xlabel('x (Menit)')
ax[1].set_ylabel('F(x)')
ax[1].set_ylim(-0.1, 1.3)
ax[1].grid(True, linestyle='--', alpha=0.6)
ax[1].legend()
plt.tight_layout()
plt.show()

# Output Validasi
print(f"Total Luas Area Kurva (0 sd 1) = {total_luas:.6f} (Valid = 1.0)")
print(f"Peluang P(0.3 <= X <= 0.7)     = {prob_interval:.6f} (Teori: 0.4000)")
```

---

## 4. TABEL PERBANDINGAN: MANUAL VS PYTHON

### Tabel Perbandingan Kasus Diskrit (2 Koin)
| Parameter / Notasi | Nilai Perhitungan Manual | Nilai Komputasi Python | Selisih (Error) | Kesimpulan |
|---|---|---|---|---|
| $f(0) = P(X = 0)$ | $1/4 = 0.2500$ | $0.2500$ | $0.0000$ | **Identik** |
| $f(1) = P(X = 1)$ | $2/4 = 0.5000$ | $0.5000$ | $0.0000$ | **Identik** |
| $f(2) = P(X = 2)$ | $1/4 = 0.2500$ | $0.2500$ | $0.0000$ | **Identik** |
| **Total Probabilitas** | $\sum f(x) = 1.0000$ | $1.0000$ | $0.0000$ | **Valid** |
| $F(0)$ | $0.2500$ | $0.2500$ | $0.0000$ | **Identik** |
| $F(1)$ | $0.7500$ | $0.7500$ | $0.0000$ | **Identik** |
| $F(2)$ | $1.0000$ | $1.0000$ | $0.0000$ | **Identik** |
| **Peluang $P(X \ge 1)$** | $\mathbf{0.7500}$ | $\mathbf{0.7500}$ | $\mathbf{0.0000}$ | **Identik (100%)** |

### Tabel Perbandingan Kasus Kontinu ($f(x) = 1$)
| Parameter / Notasi | Nilai Perhitungan Manual | Nilai Komputasi Python (`scipy.quad`) | Selisih (Error) | Kesimpulan |
|---|---|---|---|---|
| Syarat 1 ($f(x) \ge 0$) | Terpenuhi ($1 \ge 0$ pada $[0, 1]$) | Terverifikasi | $0$ | **Valid** |
| Syarat 2 ($\int_0^1 1\,dx$) | $[x]_0^1 = 1.0000$ | $1.000000$ | $< 10^{-14}$ | **Valid** |
| Rumus CDF $F(x)$ | $F(x) = x$ | Vektorisasi integrasi numerik | $0$ | **Identik** |
| Nilai $F(0.3)$ | $0.3000$ | $0.300000$ | $< 10^{-14}$ | **Identik** |
| Nilai $F(0.7)$ | $0.7000$ | $0.700000$ | $< 10^{-14}$ | **Identik** |
| **Peluang $P(0.3 \le X \le 0.7)$** | $\mathbf{0.4000}$ | $\mathbf{0.400000}$ | $\mathbf{0.0000}$ | **Identik (100%)** |

---

## 5. KESIMPULAN
1. Pada variabel acak diskrit (pelemparan 2 koin), seluruh probabilitas manual ($1/4, 2/4, 1/4$) terbukti **sama persis 100%** dengan hasil komputasi binomial Python.
2. Pada variabel acak kontinu ($f(x) = 1$), luas area kurva total terbukti bernilai $1.0$, dan peluang interval $P(0.3 \le X \le 0.7)$ menghasilkan nilai $0.4000$ baik secara analitik maupun numerik Python.
3. Bentuk CDF diskrit berupa **fungsi tangga (*step function*)**, sedangkan CDF kontinu berupa **garis lurus miring sempurna ($F(x) = x$)**.

---

## 💡 CHEAT SHEET SUPER SANTAI: CARA MENJAWAB KE DOSEN

Jika Dosen (Dr. Wiyli Yustanti) bertanya tentang tugas ini, jawab dengan 3 kalimat santai berikut:

### 1. Dosen: *"Jelaskan kasus diskrit Anda!"*
> *"Saya memilih kasus pelemparan 2 koin seimbang, Bu. Ruang sampelnya sangat ringkas, hanya ada 4 kemungkinan: AA, AG, GA, dan GG. Variabel acak X adalah jumlah Gambar yang muncul ($0, 1,$ atau $2$). Peluangnya adalah $1/4$ untuk 0 Gambar, $2/4$ untuk 1 Gambar, dan $1/4$ untuk 2 Gambar. Peluang muncul minimal 1 Gambar adalah $0.50 + 0.25 = 0.75$, terbukti identik dengan hasil Python."*

### 2. Dosen: *"Jelaskan kasus kontinu Anda!"*
> *"Untuk kontinu, saya memilih model paling mendasar yaitu fungsi uniform konstan $f(x) = 1$ pada rentang $[0, 1]$. Fungsi ini terbukti sah sebagai PDF karena nilainya selalu positif dan luas area perseginya adalah $1 \times 1 = 1$. Rumus CDF-nya linier $F(x) = x$. Peluang interval $0.3 \le X \le 0.7$ tinggal dihitung dari selisih batas atas dan batas bawah: $0.7 - 0.3 = 0.40$, terbukti persis sama dengan integrasi numerik Python."*

### 3. Dosen: *"Apa bedanya CDF diskrit dan kontinu di tugas Anda?"*
> *"Pada 2 koin, CDF-nya berbentuk **tangga** yang melompat naik di titik integer 0, 1, dan 2. Sedangkan pada kontinu, CDF-nya berbentuk **garis lurus mulus miring** dari titik 0 ke 1."*
