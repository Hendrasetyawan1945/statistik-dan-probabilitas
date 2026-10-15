# LAPORAN TUGAS STATISTIKA & PROBABILITAS
## ANALISIS VARIABEL RANDOM DISKRIT DAN KONTINU: PMF, PDF, CDF, DAN VALIDASI DENGAN PYTHON

---

### IDENTITAS MAHASISWA & MATA KULIAH
- **Mata Kuliah**       : Statistika & Probabilitas (Minggu 3)
- **Topik**             : Variabel Random Diskrit dan Kontinu, PMF, PDF, CDF, dan Komputasi Python
- **Program Studi**     : S2 Informatika, Fakultas Teknik, Universitas Negeri Surabaya (UNESA)
- **Dosen Pengampu**    : Dr. Wiyli Yustanti, S.Si., M.Kom.
- **Nama Mahasiswa**    : HENDRA CAHYO SETIAWAN
- **NIM**               : 26051905039
- **Tahun Akademik**    : Gasal 2026/2027

---

## DAFTAR ISI
- **COVER**
- **I. PENDAHULUAN**
  - 1.1 Latar Belakang
  - 1.2 Tujuan
- **II. PERMASALAHAN**
  - 2.1 Kasus 1: Variabel Random Diskrit (Pengambilan Sampel Server GPU)
  - 2.2 Kasus 2: Variabel Random Kontinu (Waktu Eksekusi Query Database)
- **III. PEMBAHASAN**
  - 3.1 Perhitungan Manual Kasus Diskrit
  - 3.2 Perhitungan Manual Kasus Kontinu
  - 3.3 Implementasi Kode Program Python
  - 3.4 Visualisasi Grafik PMF/PDF dan CDF
  - 3.5 Perbandingan Hasil Perhitungan Manual dan Python
- **IV. PENUTUP**
  - 4.1 Kesimpulan
- **DAFTAR PUSTAKA**

---

# I. PENDAHULUAN

### 1.1 Latar Belakang
Dalam bidang ilmu komputer dan informatika, banyak kejadian yang memiliki unsur ketidakpastian. Misalnya, dalam pengujian kualitas server, kita sering mengambil sampel perangkat untuk diperiksa. Begitu juga saat memantau kinerja database, waktu eksekusi (latensi) dari query yang masuk bervariasi tergantung beban sistem dan kondisi jaringan.

Untuk memodelkan dan menganalisis kejadian-kejadian tersebut secara matematis, digunakan konsep **variabel random (variabel acak)**. Secara umum, variabel random dibagi menjadi dua jenis:
1. **Variabel Random Diskrit**: Memiliki nilai-nilai yang terpisah dan dapat dihitung (countable). Probabilitas kemunculan tiap nilainya dinyatakan dalam *Probability Mass Function* (PMF) $f(x) = P(X = x)$ dengan syarat $\sum f(x) = 1$. Akumulasi peluang dinyatakan dalam *Cumulative Distribution Function* (CDF) $F(x) = P(X \le x)$ yang grafiknya berbentuk fungsi tangga.
2. **Variabel Random Kontinu**: Memiliki nilai yang berada pada suatu rentang atau interval bilangan riil kontinu. Probabilitasnya dinyatakan dalam *Probability Density Function* (PDF) $f(x)$ dengan syarat total area kurva bernilai 1 ($\int_{-\infty}^{\infty} f(x)dx = 1$). Pada variabel kontinu, peluang pada satu titik tepat selalu bernilai nol ($P(X = c) = 0$), sehingga peluang hanya bisa dihitung pada suatu interval tertentu $[a, b]$ menggunakan integral atau selisih CDF ($F(b) - F(a)$).

Laporan ini disusun untuk memenuhi tugas perkuliahan dengan menyajikan dua studi kasus konkret (satu diskrit dan satu kontinu), melakukan perhitungan analitik manual, membuat visualisasi grafik, serta memvalidasi seluruh hasil perhitungan menggunakan program Python.

### 1.2 Tujuan
Tujuan dari penulisan laporan ini adalah:
1. Menyusun dan menghitung fungsi PMF dan CDF untuk satu studi kasus variabel random diskrit.
2. Menyusun fungsi PDF, membuktikan keabsahan fungsinya, menentukan fungsi CDF, serta membuktikan bahwa peluang pada satu titik bernilai nol untuk satu studi kasus variabel random kontinu.
3. Menghitung peluang kejadian tertentu (Kejadian $A$) pada kedua kasus.
4. Membuat visualisasi grafik PMF, PDF, dan CDF untuk memperjelas bentuk distribusi probabilitas.
5. Menuliskan skrip program Python untuk membuktikan bahwa hasil perhitungan manual sama persis dengan hasil komputasi pemrograman.

---

# II. PERMASALAHAN

### 2.1 Kasus 1: Variabel Random Diskrit (Pengambilan Sampel Server GPU)
Sebuah laboratorium memiliki total $N = 10$ unit server. Di antaranya, terdapat $K = 3$ unit server yang dilengkapi akselerator GPU, sedangkan sisanya ($7$ unit) adalah server standar tanpa GPU.

Untuk keperluan audit teknis, diambil sampel acak sebanyak $n = 3$ unit server secara bersamaan tanpa pengembalian (*sampling without replacement*).

- **Definisi Variabel Acak**:
  $$X = \text{Banyaknya server GPU yang terpilih dalam 3 sampel yang diambil}$$
- **Nilai yang Mungkin**:
  $$X \in \{0, 1, 2, 3\}$$
- **Total Kombinasi Pengambilan (Ruang Sampel)**:
  $$n(\mathcal{S}) = \binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$
- **Kejadian $A$ yang Dipilih**:
  Terpilih **minimal 2 server GPU** dalam sampel:
  $$A = \{X \ge 2\} = \{X = 2, X = 3\}$$

---

### 2.2 Kasus 2: Variabel Random Kontinu (Waktu Eksekusi Query Database)
Waktu eksekusi suatu query database (dalam satuan detik) dimodelkan sebagai variabel random kontinu $X$ pada rentang waktu antara $0$ sampai $2$ detik, dengan fungsi kepadatan peluang (PDF) sebagai berikut:

$$f(x) = \begin{cases} \frac{3}{8}x^2, & 0 \le x \le 2 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$

- **Kejadian $A$ yang Dipilih**:
  Query selesai dalam rentang waktu antara $0.5$ detik sampai $1.5$ detik:
  $$A = \{0.5 \le X \le 1.5\}$$
- **Pengujian Titik Tunggal**:
  Membuktikan bahwa peluang waktu respon tepat $1.0$ detik bernilai nol:
  $$P(X = 1.0) = 0$$

---

# III. PEMBAHASAN

### 3.1 Perhitungan Manual Kasus Diskrit

Pengambilan sampel tanpa pengembalian ini mengikuti pola **Distribusi Hipergeometrik**:

$$f(x) = P(X = x) = \frac{\binom{K}{x} \binom{N - K}{n - x}}{\binom{N}{n}} = \frac{\binom{3}{x} \binom{7}{3 - x}}{\binom{10}{3}}$$

#### A. Perhitungan Fungsi Massa Peluang (PMF)

1. **Untuk $X = 0$ (Tidak ada server GPU yang terpilih):**
   $$f(0) = P(X = 0) = \frac{\binom{3}{0} \binom{7}{3}}{120} = \frac{1 \times 35}{120} = \frac{35}{120} \approx 0.291667$$

2. **Untuk $X = 1$ (Terpilih 1 server GPU dan 2 server standar):**
   $$f(1) = P(X = 1) = \frac{\binom{3}{1} \binom{7}{2}}{120} = \frac{3 \times 21}{120} = \frac{63}{120} \approx 0.525000$$

3. **Untuk $X = 2$ (Terpilih 2 server GPU dan 1 server standar):**
   $$f(2) = P(X = 2) = \frac{\binom{3}{2} \binom{7}{1}}{120} = \frac{3 \times 7}{120} = \frac{21}{120} \approx 0.175000$$

4. **Untuk $X = 3$ (Semua 3 sampel adalah server GPU):**
   $$f(3) = P(X = 3) = \frac{\binom{3}{3} \binom{7}{0}}{120} = \frac{1 \times 1}{120} = \frac{1}{120} \approx 0.008333$$

**Pengecekan Syarat Total Peluang:**
$$\sum_{x=0}^{3} f(x) = \frac{35}{120} + \frac{63}{120} + \frac{21}{120} + \frac{1}{120} = \frac{120}{120} = 1.0 \quad (\text{Syarat Terpenuhi})$$

#### B. Perhitungan Fungsi Distribusi Kumulatif (CDF)

Fungsi distribusi kumulatif $F(x) = P(X \le x)$ dihitung dengan menjumlahkan nilai PMF:

- Untuk $x < 0$: $F(x) = 0$
- Untuk $0 \le x < 1$: $F(x) = f(0) = \frac{35}{120} \approx 0.291667$
- Untuk $1 \le x < 2$: $F(x) = f(0) + f(1) = \frac{35 + 63}{120} = \frac{98}{120} \approx 0.816667$
- Untuk $2 \le x < 3$: $F(x) = f(0) + f(1) + f(2) = \frac{98 + 21}{120} = \frac{119}{120} \approx 0.991667$
- Untuk $x \ge 3$: $F(x) = f(0) + f(1) + f(2) + f(3) = \frac{120}{120} = 1.0$

Bentuk matematis formal CDF:
$$F(x) = \begin{cases} 0, & x < 0 \\ \frac{35}{120}, & 0 \le x < 1 \\ \frac{98}{120}, & 1 \le x < 2 \\ \frac{119}{120}, & 2 \le x < 3 \\ 1, & x \ge 3 \end{cases}$$

#### C. Perhitungan Peluang Kejadian $A$ ($X \ge 2$)

Peluang terpilih minimal 2 server GPU dihitung dengan:
$$P(A) = P(X \ge 2) = P(X = 2) + P(X = 3) = \frac{21}{120} + \frac{1}{120} = \frac{22}{120} = \frac{11}{60} \approx 0.183333$$

---

### 3.2 Perhitungan Manual Kasus Kontinu

Diberikan fungsi $f(x) = \frac{3}{8}x^2$ untuk $0 \le x \le 2$, dan $0$ untuk nilai lainnya.

#### A. Pembuktian Keabsahan Fungsi PDF
Suatu fungsi dikatakan sah sebagai PDF jika memenuhi dua syarat:
1. $f(x) \ge 0$ untuk semua $x \in [0, 2]$. Karena $x^2 \ge 0$, maka $\frac{3}{8}x^2 \ge 0$ (Terbukti).
2. Total luas area di bawah kurva harus sama dengan 1:
   $$\int_{-\infty}^{\infty} f(x)\,dx = \int_{0}^{2} \frac{3}{8}x^2\,dx = \left[ \frac{3}{8} \cdot \frac{x^3}{3} \right]_0^2 = \left[ \frac{x^3}{8} \right]_0^2 = \frac{2^3}{8} - \frac{0^3}{8} = \frac{8}{8} - 0 = 1.0 \quad (\text{Terbukti})$$

#### B. Perhitungan Fungsi Distribusi Kumulatif (CDF)
Untuk $0 \le x \le 2$, fungsi kumulatif $F(x)$ adalah:
$$F(x) = \int_{0}^{x} f(t)\,dt = \int_{0}^{x} \frac{3}{8}t^2\,dt = \left[ \frac{t^3}{8} \right]_0^x = \frac{x^3}{8}$$

Sehingga fungsi CDF lengkap dituliskan sebagai:
$$F(x) = \begin{cases} 0, & x < 0 \\ \frac{x^3}{8}, & 0 \le x \le 2 \\ 1, & x > 2 \end{cases}$$

#### C. Perhitungan Peluang Kejadian $A$ ($0.5 \le X \le 1.5$)
Peluang bahwa query selesai dalam rentang waktu $0.5$ sampai $1.5$ detik dapat dihitung melalui integrasi atau selisih nilai CDF:

- **Menggunakan Integral:**
  $$P(0.5 \le X \le 1.5) = \int_{0.5}^{1.5} \frac{3}{8}x^2\,dx = \left[ \frac{x^3}{8} \right]_{0.5}^{1.5} = \frac{(1.5)^3}{8} - \frac{(0.5)^3}{8} = \frac{3.375 - 0.125}{8} = \frac{3.25}{8} = \frac{13}{32} = 0.406250$$

- **Menggunakan Selisih CDF:**
  $$P(0.5 \le X \le 1.5) = F(1.5) - F(0.5) = \frac{(1.5)^3}{8} - \frac{(0.5)^3}{8} = 0.421875 - 0.015625 = 0.406250$$

Kedua cara memberikan hasil yang sama persis, yaitu $0.406250$.

#### D. Pembuktian Peluang Titik Tunggal $P(X = 1.0) = 0$
Pada variabel kontinu, peluang pada suatu titik tertentu dihitung dengan mengintegrasikan fungsi dari titik tersebut ke titik yang sama:
$$P(X = 1.0) = \int_{1.0}^{1.0} \frac{3}{8}x^2\,dx = \left[ \frac{x^3}{8} \right]_{1.0}^{1.0} = \frac{1^3}{8} - \frac{1^3}{8} = 0.0$$
Hal ini membuktikan secara matematis bahwa peluang variabel acak kontinu pada satu nilai eksak adalah nol.

---

### 3.3 Implementasi Kode Program Python

Berikut adalah skrip Python yang digunakan untuk menghitung seluruh nilai probabilitas dan membandingkannya dengan hasil perhitungan manual:

```python
import numpy as np
from scipy import integrate

print("=== 1. PERHITUNGAN VARIABEL RANDOM DISKRIT ===")
# Parameter kasus diskrit
N, K, n = 10, 3, 3

# Definisi kombinasi
def comb(n_val, r_val):
    if r_val < 0 or r_val > n_val:
        return 0
    return np.math.comb(n_val, r_val)

# Nilai PMF f(x)
pmf_diskrit = {}
for x in range(4):
    pmf_diskrit[x] = (comb(K, x) * comb(N - K, n - x)) / comb(N, n)
    print(f"P(X = {x}) = {pmf_diskrit[x]:.6f}")

# Nilai CDF F(x)
cdf_diskrit = {}
cum = 0.0
for x in range(4):
    cum += pmf_diskrit[x]
    cdf_diskrit[x] = cum
    print(f"F({x}) = P(X <= {x}) = {cdf_diskrit[x]:.6f}")

# Peluang kejadian A (X >= 2)
prob_A_diskrit = pmf_diskrit[2] + pmf_diskrit[3]
print(f"P(A) = P(X >= 2) = {prob_A_diskrit:.6f}")

print("\\n=== 2. PERHITUNGAN VARIABEL RANDOM KONTINU ===")
# Definisi fungsi PDF
def f_kontinu(x):
    return (3/8) * (x**2)

# Pembuktian total area PDF
total_area, _ = integrate.quad(f_kontinu, 0, 2)
print(f"Total Area Kurva PDF (0 sampai 2) = {total_area:.6f}")

# Peluang kejadian A (0.5 <= X <= 1.5)
prob_A_kontinu, _ = integrate.quad(f_kontinu, 0.5, 1.5)
print(f"P(0.5 <= X <= 1.5) = {prob_A_kontinu:.6f}")

# Nilai CDF pada x=0.5 dan x=1.5
cdf_05, _ = integrate.quad(f_kontinu, 0, 0.5)
cdf_15, _ = integrate.quad(f_kontinu, 0, 1.5)
print(f"F(0.5) = {cdf_05:.6f}")
print(f"F(1.5) = {cdf_15:.6f}")
print(f"F(1.5) - F(0.5) = {(cdf_15 - cdf_05):.6f}")

# Peluang titik tunggal P(X = 1.0)
prob_point, _ = integrate.quad(f_kontinu, 1.0, 1.0)
print(f"P(X = 1.0) = {prob_point:.6f}")
```

---

### 3.4 Visualisasi Grafik PMF/PDF dan CDF

Berikut adalah grafik visualisasi untuk kedua kasus yang dihasilkan menggunakan library `matplotlib`:

#### 1. Grafik Kasus Diskrit (PMF dan CDF)
- **Grafik PMF (Kiri)**: Menunjukkan probabilitas pada masing-masing titik $x \in \{0, 1, 2, 3\}$.
- **Grafik CDF (Kanan)**: Berbentuk tangga (*step function*) yang nilainya naik pada setiap titik bilangan bulat.

*(File gambar tersimpan di folder `tugas/assets/pmf_diskrit.png` dan `tugas/assets/cdf_diskrit.png`)*

#### 2. Grafik Kasus Kontinu (PDF dan CDF)
- **Grafik PDF (Kiri)**: Menunjukkan kurva probabilitas $f(x) = \frac{3}{8}x^2$, dengan area arsir pada rentang $[0.5, 1.5]$ yang merepresentasikan peluang kejadian $A$.
- **Grafik CDF (Kanan)**: Berbentuk kurva mulus kontinu $F(x) = \frac{x^3}{8}$.

*(File gambar tersimpan di folder `tugas/assets/pdf_kontinu.png` dan `tugas/assets/cdf_kontinu.png`)*

---

### 3.5 Perbandingan Hasil Perhitungan Manual dan Python

Berikut adalah tabel perbandingan antara perhitungan manual dengan hasil eksekusi program Python:

#### Tabel 1: Perbandingan Kasus Diskrit (Pengambilan Sampel Server GPU)
| Komponen Probabilitas | Perhitungan Manual | Program Python | Selisih | Keterangan |
|---|---|---|---|---|
| $f(0) = P(X = 0)$ | $35/120 \approx 0.291667$ | $0.291667$ | $0.000000$ | Sama (Sesuai) |
| $f(1) = P(X = 1)$ | $63/120 \approx 0.525000$ | $0.525000$ | $0.000000$ | Sama (Sesuai) |
| $f(2) = P(X = 2)$ | $21/120 \approx 0.175000$ | $0.175000$ | $0.000000$ | Sama (Sesuai) |
| $f(3) = P(X = 3)$ | $1/120 \approx 0.008333$ | $0.008333$ | $0.000000$ | Sama (Sesuai) |
| **Total Peluang ($\sum f(x)$)** | $\mathbf{120/120 = 1.000000}$ | $\mathbf{1.000000}$ | $\mathbf{0.000000}$ | **Valid** |
| $F(0) = P(X \le 0)$ | $35/120 \approx 0.291667$ | $0.291667$ | $0.000000$ | Sama (Sesuai) |
| $F(1) = P(X \le 1)$ | $98/120 \approx 0.816667$ | $0.816667$ | $0.000000$ | Sama (Sesuai) |
| $F(2) = P(X \le 2)$ | $119/120 \approx 0.991667$ | $0.991667$ | $0.000000$ | Sama (Sesuai) |
| $F(3) = P(X \le 3)$ | $120/120 = 1.000000$ | $1.000000$ | $0.000000$ | Sama (Sesuai) |
| **Peluang Kejadian $A$ ($P(X \ge 2)$)** | $\mathbf{22/120 \approx 0.183333}$ | $\mathbf{0.183333}$ | $\mathbf{0.000000}$ | **Sama (Sesuai)** |

#### Tabel 2: Perbandingan Kasus Kontinu (Waktu Eksekusi Query)
| Komponen Probabilitas | Perhitungan Manual | Program Python | Selisih | Keterangan |
|---|---|---|---|---|
| Syarat Non-negatif | $f(x) \ge 0, \forall x \in [0, 2]$ | Terverifikasi | $0.0$ | Valid |
| **Total Luas Kurva $\int_0^2 f(x)dx$** | $[x^3/8]_0^2 = \mathbf{1.000000}$ | $\mathbf{1.000000}$ | $< 10^{-15}$ | **Syarat PDF Sah** |
| Formula CDF $F(x)$ | $F(x) = x^3/8$ | $\int_0^x f(t)dt$ | $0.0$ | Sama (Sesuai) |
| $F(0.5)$ | $(0.5)^3/8 = 0.015625$ | $0.015625$ | $< 10^{-15}$ | Sama (Sesuai) |
| $F(1.5)$ | $(1.5)^3/8 = 0.421875$ | $0.421875$ | $< 10^{-15}$ | Sama (Sesuai) |
| **Peluang Kejadian $A$ ($P(0.5 \le X \le 1.5)$)** | $\mathbf{13/32 = 0.406250}$ | $\mathbf{0.406250}$ | $\mathbf{< 10^{-15}}$ | **Sama (Sesuai)** |
| Peluang Titik $P(X = 1.0)$ | $\int_1^1 f(x)dx = 0.000000$ | $0.000000$ | $0.0$ | Terbukti Nol |

---

# IV. PENUTUP

### 4.1 Kesimpulan
Dari hasil pengerjaan tugas ini, dapat disimpulkan beberapa hal sebagai berikut:
1. Seluruh hasil perhitungan manual (analitik) terbukti sama persis dengan hasil perhitungan program Python, baik pada nilai PMF, PDF, CDF, maupun peluang kejadian $A$.
2. Pada kasus variabel random diskrit (pengambilan server GPU), probabilitas bernilai positif pada titik-titik bilangan bulat ($x = 0, 1, 2, 3$). Peluang terpilih minimal 2 server GPU adalah sebesar $\frac{22}{120} \approx 0.183333$. Grafik CDF membentuk fungsi tangga (*step function*).
3. Pada kasus variabel random kontinu (waktu eksekusi query), fungsi $f(x) = \frac{3}{8}x^2$ pada rentang $[0, 2]$ terbukti memenuhi syarat sebagai PDF karena total integralnya bernilai 1. Peluang query selesai antara $0.5$ sampai $1.5$ detik adalah sebesar $\frac{13}{32} = 0.406250$. Peluang pada satu titik waktu tepat ($P(X = 1.0)$) terbukti bernilai 0, dan grafik CDF membentuk kurva mulus $F(x) = \frac{x^3}{8}$.

---

# DAFTAR PUSTAKA

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2012). *Probability & Statistics for Engineers & Scientists* (9th ed.). Boston: Prentice Hall.
2. Ross, S. M. (2014). *Introduction to Probability Models* (11th ed.). Academic Press.
3. Virtanen, P., Gommers, R., Oliphant, T. E., et al. (2020). *SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python*. Nature Methods, 17(3), 261-272.
4. Hunter, J. D. (2007). *Matplotlib: A 2D Graphics Environment*. Computing in Science & Engineering, 9(3), 90-95.
