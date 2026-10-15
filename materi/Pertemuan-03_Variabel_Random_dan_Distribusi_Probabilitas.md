# Modul Kuliah: Statistika & Probabilitas (Pertemuan Minggu ke-3)

- **Mata Kuliah**: Statistika & Probabilitas
- **Topik**: Variabel Random dan Distribusi Probabilitas
- **Program Studi**: S2 Informatika, Fakultas Teknik, Universitas Negeri Surabaya (UNESA)
- **Semester**: Gasal 2026/2027
- **Dosen Pengampu**: Dr. Wiyli Yustanti, S.Si., M.Kom.
- **File Slide Asli (PDF)**: [Pertemuan-03_Variabel_Random_dan_Distribusi_Probabilitas.pdf](file:///var/www/html/statistik-dan-probabilitas/materi/Pertemuan-03_Variabel_Random_dan_Distribusi_Probabilitas.pdf)
- **Buku Referensi**: *Probability & Statistics for Engineers & Scientists* (Walpole, Myers, Myers, Ye – 9th Edition), Chapter 3 (hal. 81–114).

---

## DAFTAR ISI
1. [Filosofi Ilmu & Konsep Dasar](#1-filosofi-ilmu--konsep-dasar)
2. [Definisi & Klasifikasi Variabel Random](#2-definisi--klasifikasi-variabel-random)
3. [Fungsi Distribusi Probabilitas (PMF & PDF)](#3-fungsi-distribusi-probabilitas-pmf--pdf)
4. [Tabel Rumus Diferensial & Integral Penting](#4-tabel-rumus-diferensial--integral-penting)
5. [Contoh Soal & Pembahasan (1 Variabel)](#5-contoh-soal--pembahasan-1-variabel)
6. [Fungsi Distribusi Kumulatif (CDF)](#6-fungsi-distribusi-kumulatif-cdf)
7. [Distribusi Probabilitas Gabungan (Joint Distribution)](#7-distribusi-probabilitas-gabungan-joint-distribution)
8. [Distribusi Probabilitas Marginal](#8-distribusi-probabilitas-marginal)
9. [Distribusi Probabilitas Bersyarat (Conditional)](#9-distribusi-probabilitas-bersyarat-conditional)
10. [Independensi Statistik (Statistical Independence)](#10-independensi-statistik-statistical-independence)
11. [Karakteristik Distribusi Probabilitas (Preview Minggu ke-4)](#11-karakteristik-distribusi-probabilitas-preview-minggu-ke-4)
12. [Praktikum Python (Google Colab / Jupyter)](#12-praktikum-python-google-colab--jupyter)
13. [Instruksi Tugas 1 - Individu](#13-instruksi-tugas-1---individu)

---

## 1. Filosofi Ilmu & Konsep Dasar
* **Mengapa Variabel Random Dibutuhkan?**  
  Dalam fenomena sains, komputasi, dan teknik, selalu terdapat faktor ketidakpastian (*uncertainty*). Konsep variabel random hadir untuk memodelkan ketidakpastian tersebut ke dalam bentuk matematis.
* **Definisi Sederhana**:  
  Variabel random adalah variabel yang nilainya bergantung pada hasil suatu kejadian acak. Nilai pastinya belum diketahui sebelum percobaan dilakukan, namun seluruh kemungkinan nilai yang dapat terjadi dapat dirumuskan dan dianalisis.
* **Peran Distribusi Probabilitas**:  
  Menjelaskan aturan atau fungsi probabilitas seberapa besar kemungkinan setiap nilai tersebut muncul.

---

## 2. Definisi & Klasifikasi Variabel Random

### Definisi 3.1 (Variabel Random)
> Variabel random adalah suatu fungsi yang mengaitkan suatu bilangan riil pada setiap unsur dalam ruang sampel $S$ dari suatu eksperimen statistik.

Prinsip utama menentukan variabel random:
1. Menetapkan eksperimen statistik.
2. Mendefinisikan ruang sampel ($S$).
3. Mengasosiasikan setiap hasil (*outcome*) dengan nilai numerik ($X$).
4. Menentukan apakah variabel tersebut **diskrit** atau **kontinu**.

### A. Variabel Random Diskrit (Definisi 3.2)
Ruang sampel disebut diskrit jika mengandung sejumlah kemungkinan yang berhingga (*finite*) atau urutan tak berujung dengan elemen sebanyak bilangan bulat (*countably infinite*).
- **Contoh Kasus**:
  - Jumlah barang cacat dalam satu batch pengiriman.
  - Jumlah mahasiswa yang hadir di kelas setiap pertemuan.
  - Banyaknya lemparan koin hingga muncul sisi Gambar.
  - Jumlah pengunjung/pelanggan restoran per jam.
  - Jumlah mobil yang melintas atau berhenti di lampu merah per siklus.
  - Jumlah panggilan telepon yang diterima call center per hari.
- **Contoh Pelemparan 2 Dadu**:
  - Eksperimen: Melempar 2 dadu bermata 1–6.
  - Ruang sampel: $S = \{(1,1), (1,2), \dots, (6,6)\}$, total $6 \times 6 = 36$ titik sampel.
  - Variabel random $X$: Jumlah mata dadu yang muncul.
  - Himpunan nilai $X = \{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$.

### B. Variabel Random Kontinu (Definisi 3.3)
Ruang sampel disebut kontinu jika mengandung kemungkinan tak terbatas yang sama dengan jumlah titik pada suatu segmen garis (interval bilangan riil).
- **Contoh Kasus**:
  - Waktu yang dibutuhkan untuk menyelesaikan ujian ($t \in [0, 120]$ menit).
  - Berat badan dan tinggi badan seseorang.
  - Ketinggian permukaan air bendungan pada waktu tertentu.
  - Suhu udara di laboratorium atau kota sepanjang hari.
  - Jarak tempuh kendaraan sampai bahan bakar habis.
  - Kecepatan angin pada waktu tertentu.
- **Contoh Waktu Tunggu Bus**:
  - Eksperimen: Mengukur waktu tunggu hingga bus tiba.
  - Ruang sampel: Rentang waktu $S = [0, 60]$ menit.
  - Nilai $X$ dapat berupa sembarang bilangan riil kontinu: $5.2$ menit, $10.51$ menit, dsb.

---

## 3. Fungsi Distribusi Probabilitas (PMF & PDF)

### A. Distribusi Probabilitas Diskrit: Probability Mass Function (PMF) - Definisi 3.4
Himpunan pasangan terurut $(x, f(x))$ merupakan fungsi peluang atau *probability mass function* (pmf) dari variabel random diskrit $X$ jika memenuhi:
1. $f(x) \ge 0$ untuk setiap nilai $x$.
2. $\sum_x f(x) = 1$.
3. $P(X = x) = f(x)$.

### B. Distribusi Probabilitas Kontinu: Probability Density Function (PDF) - Definisi 3.6
Fungsi $f(x)$ adalah fungsi kepadatan peluang atau *probability density function* (pdf) dari variabel random kontinu $X$ yang didefinisikan pada himpunan bilangan riil $\mathbb{R}$ jika memenuhi:
1. $f(x) \ge 0, \quad \forall x \in \mathbb{R}$.
2. $\int_{-\infty}^{\infty} f(x)\,dx = 1$.
3. $P(a < X < b) = \int_a^b f(x)\,dx$.

> **Catatan Kunci**:  
> Untuk variabel random kontinu, probabilitas pada nilai tunggal adalah nol ($P(X = c) = 0$). Oleh karena itu, $P(a \le X \le b) = P(a < X < b)$.

---

## 4. Tabel Rumus Diferensial & Integral Penting

### Rumus Diferensial
1. $\frac{d}{dx}(x) = 1$
2. $\frac{d}{dx}(ax) = a$
3. $\frac{d}{dx}(x^n) = n x^{n-1}$
4. $\frac{d}{dx}(\cos x) = -\sin x$
5. $\frac{d}{dx}(\sin x) = \cos x$
6. $\frac{d}{dx}(\tan x) = \sec^2 x$
7. $\frac{d}{dx}(\cot x) = -\csc^2 x$
8. $\frac{d}{dx}(\sec x) = \sec x \tan x$
9. $\frac{d}{dx}(\csc x) = -\csc x \cot x$
10. $\frac{d}{dx}(\ln x) = \frac{1}{x}$
11. $\frac{d}{dx}(\sin^{-1} x) = \frac{1}{\sqrt{1 - x^2}}$
12. $\frac{d}{dx}(\tan^{-1} x) = \frac{1}{1 + x^2}$
13. $\frac{d}{dx}(\sec^{-1} x) = \frac{1}{|x|\sqrt{x^2 - 1}}$

### Rumus Integral
1. $\int 1\,dx = x + c$
2. $\int a\,dx = ax + c$
3. $\int x^n\,dx = \frac{x^{n+1}}{n+1} + c, \quad n \ne -1$
4. $\int \sin x\,dx = -\cos x + c$
5. $\int \cos x\,dx = \sin x + c$
6. $\int \sec^2 x\,dx = \tan x + c$
7. $\int \csc^2 x\,dx = -\cot x + c$
8. $\int \sec x \tan x\,dx = \sec x + c$
9. $\int \csc x \cot x\,dx = -\csc x + c$
10. $\int \frac{1}{x}\,dx = \ln |x| + c$
11. $\int \frac{1}{\sqrt{1 - x^2}}\,dx = \sin^{-1} x + c$
12. $\int \frac{1}{1 + x^2}\,dx = \tan^{-1} x + c$

### Sifat-Sifat Integral Tentu
1. $\int_a^b f(x)\,dx = F(x)\big|_a^b = F(b) - F(a)$
2. $\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$
3. $\int_a^a f(x)\,dx = 0$
4. $\int_a^b c\,dx = c(b - a)$
5. $\int_a^b c f(x)\,dx = c \int_a^b f(x)\,dx$
6. $\int_a^b [f(x) + g(x)]\,dx = \int_a^b f(x)\,dx + \int_a^b g(x)\,dx$
7. $\int_a^b [f(x) - g(x)]\,dx = \int_a^b f(x)\,dx - \int_a^b g(x)\,dx$

---

## 5. Contoh Soal & Pembahasan (1 Variabel)

### Contoh 1 (Diskrit - Example 3.8 Walpole)
**Soal**:  
Sebuah pengiriman berisi 20 laptop serupa ke toko ritel, di mana 3 di antaranya rusak. Jika sebuah sekolah membeli 2 laptop secara acak, tentukan distribusi probabilitas jumlah laptop yang rusak.

**Penyelesaian**:
1. *Definisikan Variabel Acak*:  
   $X$ = jumlah laptop rusak yang dibeli sekolah.  
   Nilai yang mungkin: $X \in \{0, 1, 2\}$.
2. *Ruang Sampel*:  
   Banyak cara memilih 2 dari 20 laptop:
   $$n(S) = \binom{20}{2} = \frac{20 \times 19}{2 \times 1} = 190$$
3. *Banyak Cara Kejadian*:
   - $X = 0$ (tidak ada yang rusak, berarti 2 laptop bagus dari 17):
     $$\binom{3}{0} \times \binom{17}{2} = 1 \times 136 = 136 \implies P(X=0) = \frac{136}{190} = \frac{68}{95} \approx 0.7158$$
   - $X = 1$ (1 rusak dari 3, dan 1 bagus dari 17):
     $$\binom{3}{1} \times \binom{17}{1} = 3 \times 17 = 51 \implies P(X=1) = \frac{51}{190} \approx 0.2684$$
   - $X = 2$ (2 rusak dari 3):
     $$\binom{3}{2} \times \binom{17}{0} = 3 \times 1 = 3 \implies P(X=2) = \frac{3}{190} \approx 0.0158$$
4. *Tabel Distribusi Probabilitas*:

| $x$ | 0 | 1 | 2 |
|---|---|---|---|
| $f(x)$ | $\frac{68}{95}$ ($\approx 0.7158$) | $\frac{51}{190}$ ($\approx 0.2684$) | $\frac{3}{190}$ ($\approx 0.0158$) |

---

### Contoh 2 (Kontinu - Example 3.11 Walpole)
**Soal**:  
Kesalahan suhu reaksi lab dalam $^\circ\text{C}$ adalah variabel random kontinu $X$ dengan fungsi densitas:
$$f(x) = \begin{cases} \frac{x^2}{3}, & -1 < x < 2 \\ 0, & \text{di tempat lain} \end{cases}$$
a) Buktikan bahwa $f(x)$ adalah fungsi densitas peluang yang sah!  
b) Hitung $P(0 < X \le 1)$!

**Penyelesaian**:
- **Bagian a (Pembuktian)**:
  1. Untuk $-1 < x < 2$, $x^2 \ge 0 \implies \frac{x^2}{3} \ge 0$. Syarat pertama ($f(x) \ge 0$) terpenuhi.
  2. Integralkan di seluruh ruang sampel:
     $$\int_{-\infty}^{\infty} f(x)\,dx = \int_{-1}^{2} \frac{x^2}{3}\,dx = \frac{1}{3} \left[ \frac{x^3}{3} \right]_{-1}^{2} = \frac{1}{9} \left( 2^3 - (-1)^3 \right) = \frac{1}{9} (8 - (-1)) = \frac{9}{9} = 1$$
     Syarat kedua terpenuhi. Maka terbukti $f(x)$ adalah PDF yang sah.
- **Bagian b (Peluang Interval)**:
  $$P(0 < X \le 1) = \int_{0}^{1} \frac{x^2}{3}\,dx = \frac{1}{3} \left[ \frac{x^3}{3} \right]_0^1 = \frac{1}{9}(1^3 - 0^3) = \frac{1}{9} \approx 0.1111$$

---

## 6. Fungsi Distribusi Kumulatif (CDF)

### Definisi 3.5 (CDF Diskrit)
Fungsi distribusi kumulatif $F(x)$ dari variabel random diskrit $X$ dengan PMF $f(x)$ adalah:
$$F(x) = P(X \le x) = \sum_{t \le x} f(t), \quad -\infty < x < \infty$$

### Definisi 3.7 (CDF Kontinu)
Fungsi distribusi kumulatif $F(x)$ dari variabel random kontinu $X$ dengan PDF $f(x)$ adalah:
$$F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt, \quad -\infty < x < \infty$$
Konsekuensi:
$$P(a < X < b) = F(b) - F(a) \quad \text{dan} \quad f(x) = \frac{dF(x)}{dx}$$

Pada contoh Example 3.11 di atas:
$$F(x) = \int_{-1}^x \frac{t^2}{3}\,dt = \left[ \frac{t^3}{9} \right]_{-1}^x = \frac{x^3 + 1}{9}, \quad \text{untuk } -1 \le x < 2$$
Sehingga:
$$P(0 < X \le 1) = F(1) - F(0) = \frac{1^3+1}{9} - \frac{0^3+1}{9} = \frac{2}{9} - \frac{1}{9} = \frac{1}{9}$$

---

## 7. Distribusi Probabilitas Gabungan (Joint Distribution)

### A. Joint PMF (Diskrit - Definisi 3.8)
Fungsi $f(x, y)$ adalah joint PMF dari variabel random diskrit $(X, Y)$ jika:
1. $f(x, y) \ge 0, \quad \forall (x, y)$
2. $\sum_x \sum_y f(x, y) = 1$
3. $P(X = x, Y = y) = f(x, y)$

#### Contoh Soal: Example 3.14 (Kotak Berisi Pena)
Kotak berisi 8 pena: **3 biru**, **2 merah**, dan **3 hijau**. Diambil 2 pena secara acak.  
Misalkan $X$ = banyaknya pena biru yang terambil, dan $Y$ = banyaknya pena merah yang terambil.
- Ruang sampel total: $\binom{8}{2} = 28$ cara.
- Rumus umum probabilitas gabungan:
  $$f(x, y) = \frac{\binom{3}{x}\binom{2}{y}\binom{3}{2 - x - y}}{\binom{8}{2}}, \quad x \ge 0, y \ge 0, x + y \le 2$$

**Tabel Distribusi Gabungan $f(x, y)$**:

| $y \backslash x$ | 0 | 1 | 2 | Total Baris $h(y)$ |
|---|---|---|---|---|
| **0** | $3/28$ | $9/28$ | $3/28$ | $15/28$ |
| **1** | $6/28 = 3/14$ | $6/28 = 3/14$ | $0$ | $3/7 = 12/28$ |
| **2** | $1/28$ | $0$ | $0$ | $1/28$ |
| **Total Kolom $g(x)$** | $10/28 = 5/14$ | $15/28$ | $3/28$ | **1** |

- Menghitung $P((X, Y) \in A)$ untuk $A = \{(x, y) \mid x + y \le 1\}$:
  $$P[(X,Y) \in A] = f(0,0) + f(0,1) + f(1,0) = \frac{3}{28} + \frac{6}{28} + \frac{9}{28} = \frac{18}{28} = \frac{9}{14}$$

---

### B. Joint PDF (Kontinu - Definisi 3.9)
Fungsi $f(x, y)$ adalah joint PDF dari variabel kontinu $(X, Y)$ jika:
1. $f(x, y) \ge 0, \quad \forall (x, y)$
2. $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y)\,dx\,dy = 1$
3. $P((X, Y) \in A) = \iint_A f(x, y)\,dx\,dy$

#### Contoh Soal: Example 3.15 (Drive-In & Walk-In)
Sebuah fasilitas mengoperasikan fasilitas drive-in ($X$) dan walk-in ($Y$) dengan proporsi waktu penggunaan yang memiliki PDF gabungan:
$$f(x, y) = \begin{cases} \frac{2}{5}(2x + 3y), & 0 \le x \le 1, 0 \le y \le 1 \\ 0, & \text{di tempat lain} \end{cases}$$

1. **Verifikasi Kondisi 2**:
   $$\int_0^1 \int_0^1 \frac{2}{5}(2x + 3y)\,dx\,dy = \int_0^1 \left[ \frac{2}{5}(x^2 + 3xy) \right]_{x=0}^{x=1} dy = \int_0^1 \left( \frac{2}{5} + \frac{6y}{5} \right) dy = \left[ \frac{2}{5}y + \frac{3}{5}y^2 \right]_0^1 = \frac{2}{5} + \frac{3}{5} = 1 \quad \text{(Terbukti)}$$
2. **Peluang pada Daerah $A = \{ (x, y) \mid 0 < x < \frac{1}{2}, \frac{1}{4} < y < \frac{1}{2} \}$**:
   $$\int_{1/4}^{1/2} \int_0^{1/2} \frac{2}{5}(2x + 3y)\,dx\,dy = \int_{1/4}^{1/2} \left( \frac{1}{10} + \frac{6y}{5} \cdot \frac{1}{2} \right) dy = \left[ \frac{y}{10} + \frac{3y^2}{10} \right]_{1/4}^{1/2} = \frac{13}{160}$$

---

## 8. Distribusi Probabilitas Marginal

### Definisi 3.10
Distribusi marginal adalah fungsi probabilitas untuk masing-masing variabel secara individual yang diperoleh dari distribusi gabungan:
- **Diskrit**:
  $$g(x) = \sum_y f(x, y) \quad \text{dan} \quad h(y) = \sum_x f(x, y)$$
- **Kontinu**:
  $$g(x) = \int_{-\infty}^{\infty} f(x, y)\,dy \quad \text{dan} \quad h(y) = \int_{-\infty}^{\infty} f(x, y)\,dx$$

#### Contoh: Example 3.17 (Marginal dari Example 3.15)
$$g(x) = \int_0^1 \frac{2}{5}(2x + 3y)\,dy = \left[ \frac{4xy}{5} + \frac{6y^2}{10} \right]_{y=0}^{y=1} = \frac{4x + 3}{5}, \quad 0 \le x \le 1$$
$$h(y) = \int_0^1 \frac{2}{5}(2x + 3y)\,dx = \left[ \frac{2x^2}{5} + \frac{6xy}{5} \right]_{x=0}^{x=1} = \frac{2(1 + 3y)}{5}, \quad 0 \le y \le 1$$

---

## 9. Distribusi Probabilitas Bersyarat (Conditional)

### Definisi 3.11
Distribusi bersyarat memberikan peluang suatu variabel dengan diketahui nilai variabel lainnya:
$$f(y \mid x) = \frac{f(x, y)}{g(x)}, \quad \text{asalkan } g(x) > 0$$
$$f(x \mid y) = \frac{f(x, y)}{h(y)}, \quad \text{asalkan } h(y) > 0$$

#### Contoh: Example 3.18 (Pena Merah & Biru)
Dari tabel Example 3.14, cari distribusi bersyarat $X$ jika diketahui $Y = 1$ (terpilih 1 pena merah):
- $h(1) = \frac{3}{14} + \frac{3}{14} + 0 = \frac{3}{7}$
- $f(0 \mid 1) = \frac{f(0,1)}{h(1)} = \frac{3/14}{3/7} = \frac{1}{2}$
- $f(1 \mid 1) = \frac{f(1,1)}{h(1)} = \frac{3/14}{3/7} = \frac{1}{2}$
- $f(2 \mid 1) = \frac{0}{3/7} = 0$
- Maka: $P(X = 0 \mid Y = 1) = \frac{1}{2}$. Artinya jika diketahui 1 pena merah terpilih, peluang pena kedua bukan biru adalah $\frac{1}{2}$.

#### Contoh: Example 3.19 (Suhu dan Pergeseran Spektrum Partikel)
Diketahui joint density: $f(x, y) = 10xy^2$ untuk $0 < x < y < 1$:
- $g(x) = \int_x^1 10xy^2\,dy = \frac{10}{3}x(1 - x^3)$
- $h(y) = \int_0^y 10xy^2\,dx = 5y^4$
- Distribusi bersyarat:
  $$f(y \mid x) = \frac{f(x,y)}{g(x)} = \frac{10xy^2}{\frac{10}{3}x(1 - x^3)} = \frac{3y^2}{1 - x^3}, \quad 0 < x < y < 1$$
- Peluang pergeseran spektrum lebih dari separuh ($Y > 1/2$) jika suhu bertambah $0.25$ unit ($X = 0.25$):
  $$P(Y > 1/2 \mid X = 0.25) = \int_{1/2}^1 \frac{3y^2}{1 - 0.25^3}\,dy = \frac{8}{9}$$

---

## 10. Independensi Statistik (Statistical Independence)

### Definisi 3.12 & 3.13
Dua variabel random $X$ dan $Y$ dikatakan saling bebas / independen secara statistik jika dan hanya jika:
$$f(x, y) = g(x) \cdot h(y) \quad \text{untuk semua } (x, y)$$
Untuk $n$ variabel random:
$$f(x_1, x_2, \dots, x_n) = f_1(x_1) \cdot f_2(x_2) \cdots f_n(x_n)$$

#### Contoh Uji Independensi 1 (Diskrit - Terbukti Independen):
Diketahui:
- $P(X=0) = 0.3, \quad P(X=1) = 0.7$
- $P(Y=0) = 0.4, \quad P(Y=1) = 0.6$
- Joint PMF:
  - $P(0,0) = 0.12 = 0.3 \times 0.4$ (Cocok)
  - $P(0,1) = 0.18 = 0.3 \times 0.6$ (Cocok)
  - $P(1,0) = 0.28 = 0.7 \times 0.4$ (Cocok)
  - $P(1,1) = 0.42 = 0.7 \times 0.6$ (Cocok)  
  $\implies X$ dan $Y$ **independen secara statistik**.

#### Contoh Uji Independensi 2 (Kontinu - Tidak Independen):
Fungsi densitas: $f_{X,Y}(x,y) = 6(1 - x - y)$ untuk $0 \le x \le 1, 0 \le y \le 1, x + y \le 1$.
- Marginal $X$: $f_X(x) = 3(1 - x)^2$
- Marginal $Y$: $f_Y(y) = 3(1 - y)^2$
- Uji perkalian: $f_X(x) \cdot f_Y(y) = 9(1 - x)^2(1 - y)^2 \ne 6(1 - x - y)$.  
  $\implies X$ dan $Y$ **tidak independen (dependen)**.

---

## 11. Karakteristik Distribusi Probabilitas (Preview Minggu ke-4)
Karakteristik penting yang akan dipelajari pada Pertemuan ke-4 (Chapter 4):
1. **Mean** (Nilai Harapan / Ekspektasi Matematik - $\mu = E[X]$)
2. **Varians & Standar Deviasi** ($\sigma^2 = \text{Var}(X), \sigma$)
3. **Skewness** (Tingkat Kemiringan Kurva)
4. **Kurtosis** (Tingkat Keruncingan Kurva)
5. **Modus** (Nilai dengan probabilitas tertinggi)
6. **Median** (Nilai tengah pemisah 50% probabilitas)
7. **Momen** (Momen ke-$k$ di sekitar origin dan di sekitar mean)
8. **Fungsi Kepadatan Peluang** (PMF atau PDF)
9. **Fungsi Distribusi Kumulatif** (CDF)

---

## 12. Praktikum Python (Google Colab / Jupyter)

### Praktikum 1-3: Variabel Random Diskrit (Contoh Kasus Laptop Rusak)
```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Fungsi untuk menghitung probabilitas hipergeometrik
def laptop_pmf(k, N, K, n):
    """
    k: jumlah item cacat dalam sampel
    N: total item (populasi)
    K: total item cacat dalam populasi
    n: ukuran sampel
    """
    return (comb(K, k) * comb(N - K, n - k)) / comb(N, n)

# Parameter distribusi
N = 20  # Total laptop
K = 3   # Laptop cacat
n = 2   # Laptop yang dibeli

k_vals = np.arange(0, min(K, n) + 1)
pmf_vals = [laptop_pmf(k, N, K, n) for k in k_vals]

# 1. Gambarkan PDF (PMF)
plt.figure(figsize=(8, 4))
plt.stem(k_vals, pmf_vals, basefmt=" ")
plt.title('Probability Mass Function (PMF)')
plt.xlabel('Banyaknya Laptop Rusak (k)')
plt.ylabel('Probabilitas')
plt.xticks(k_vals)
plt.grid(True)
plt.show()

# 2. Gambarkan CDF
cdf_vals = np.cumsum(pmf_vals)
plt.figure(figsize=(8, 4))
plt.step(k_vals, cdf_vals, where='mid', label='CDF', color='green')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Banyaknya Laptop Rusak (k)')
plt.ylabel('Cumulative Probability')
plt.xticks(k_vals)
plt.grid(True)
plt.show()

# 3. Tampilkan Tabel Probabilitas
for k, pmf in zip(k_vals, pmf_vals):
    print(f"P(X = {k}) = {pmf:.4f}")
```

### Praktikum 4-7: Variabel Random Kontinu (Contoh Kasus Suhu Lab)
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definisikan fungsi PDF
def pdf(x):
    if -1 < x < 2:
        return (x**2) / 3
    else:
        return 0

# Vektorisasi fungsi agar mendukung array numpy
pdf_vec = np.vectorize(pdf)

# Definisikan fungsi CDF menggunakan integrasi numerik
def cdf(x):
    result, _ = quad(pdf, -1, x)
    return result

cdf_vec = np.vectorize(cdf)

x_vals = np.linspace(-1.5, 2.5, 500)
pdf_vals = pdf_vec(x_vals)
cdf_vals = cdf_vec(x_vals)

# 1. Gambarkan Kurva PDF
plt.figure(figsize=(8, 4))
plt.plot(x_vals, pdf_vals, label='PDF', color='blue')
plt.fill_between(x_vals, pdf_vals, alpha=0.3, color='blue')
plt.title('Probability Density Function (PDF)')
plt.xlabel('x (Suhu)')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

# 2. Gambarkan Kurva CDF
plt.figure(figsize=(8, 4))
plt.plot(x_vals, cdf_vals, label='CDF', color='green')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('x (Suhu)')
plt.ylabel('F(x)')
plt.grid(True)
plt.legend()
plt.show()

# 3. Hitung Probabilitas Interval P(0 < X < 1)
prob_0_to_1, _ = quad(pdf, 0, 1)
print(f"P(0 < X < 1) = {prob_0_to_1:.6f} (Teori: 1/9 ≈ 0.111111)")
```

---

## 13. Instruksi Tugas 1 - Individu (Slide 34)

1. **Kerjakan praktikum** yang ada pada materi pembelajaran ini (jalankan kode di Google Colab / Jupyter Notebook).
2. **Cari 1 soal tentang Variabel Random Diskrit** dan **1 soal tentang Variabel Random Kontinu**:
   - Buktikan hasil perhitungan manual untuk PDF, CDF, dan peluang kejadian yang ditentukan.
   - Bandingkan dengan hasil pemrograman Python dan buktikan keduanya menunjukkan hasil yang persis sama.
3. **Waktu Pengerjaan**: 1 minggu (Deadline H-1 sebelum Pertemuan Minggu ke-4).
4. **Tempat Pengumpulan**: Diunggah ke Google Classroom sesuai instruksi dosen.
5. **Format Berkas yang Diunggah**:
   - Berkas **Jupyter Notebook (`.ipynb`)** untuk simulasi Python (soal VR diskrit dan kontinu).
   - Berkas **MS Word (`.docx`)** untuk penjelasan perbandingan antara perhitungan manual dan simulasi Python.
