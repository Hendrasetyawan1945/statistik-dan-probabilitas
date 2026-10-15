import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Tetapkan seed agar reproducible
np.random.seed(42)

n_samples = 500

# ==========================================
# 1. STUDI KASUS 1: DISTRIBUSI EKSPONENSIAL
# Waktu jeda antar-transaksi Payment Gateway (detik)
# Parameter laju kedatangan lambda = 0.5 transaksi/detik
# Nilai skala (scale = 1/lambda) = 2.0 detik
# ==========================================
scale_exp = 2.0
data_exp = np.random.exponential(scale=scale_exp, size=n_samples)

# Statistik Deskriptif Eksponensial
mean_exp = np.mean(data_exp)
median_exp = np.median(data_exp)
var_exp = np.var(data_exp, ddof=1)
std_exp = np.std(data_exp, ddof=1)
p20_exp = np.percentile(data_exp, 20)
p80_exp = np.percentile(data_exp, 80)
skew_exp = stats.skew(data_exp)
kurt_exp = stats.kurtosis(data_exp)  # excess kurtosis

# Modus kontinu menggunakan KDE (Kernel Density Estimation)
kde_exp = stats.gaussian_kde(data_exp)
x_grid_exp = np.linspace(0, np.max(data_exp), 1000)
mode_exp = x_grid_exp[np.argmax(kde_exp(x_grid_exp))]

print("=== STATISTIK DESKRIPTIF KASUS 1 (EKSPONENSIAL) ===")
print(f"Mean: {mean_exp:.4f}")
print(f"Modus (KDE peak): {mode_exp:.4f}")
print(f"Median: {median_exp:.4f}")
print(f"Persentil 20: {p20_exp:.4f}")
print(f"Persentil 80: {p80_exp:.4f}")
print(f"Varians: {var_exp:.4f}")
print(f"Standar Deviasi: {std_exp:.4f}")
print(f"Skewness: {skew_exp:.4f}")
print(f"Kurtosis: {kurt_exp:.4f}")

# ==========================================
# 2. STUDI KASUS 2: DISTRIBUSI LOGNORMAL
# Waktu respon / Download Aset CDN Aplikasi Mobile (milidetik)
# Parameter underlying normal: mu = 5.7, sigma = 0.5
# ==========================================
mu_lognorm = 5.7
sigma_lognorm = 0.5
data_lognorm = np.random.lognormal(mean=mu_lognorm, sigma=sigma_lognorm, size=n_samples)

# Statistik Deskriptif Lognormal
mean_lognorm = np.mean(data_lognorm)
median_lognorm = np.median(data_lognorm)
var_lognorm = np.var(data_lognorm, ddof=1)
std_lognorm = np.std(data_lognorm, ddof=1)
p20_lognorm = np.percentile(data_lognorm, 20)
p80_lognorm = np.percentile(data_lognorm, 80)
skew_lognorm = stats.skew(data_lognorm)
kurt_lognorm = stats.kurtosis(data_lognorm)

kde_lognorm = stats.gaussian_kde(data_lognorm)
x_grid_lognorm = np.linspace(np.min(data_lognorm), np.max(data_lognorm), 1000)
mode_lognorm = x_grid_lognorm[np.argmax(kde_lognorm(x_grid_lognorm))]

print("\n=== STATISTIK DESKRIPTIF KASUS 2 (LOGNORMAL) ===")
print(f"Mean: {mean_lognorm:.4f}")
print(f"Modus (KDE peak): {mode_lognorm:.4f}")
print(f"Median: {median_lognorm:.4f}")
print(f"Persentil 20: {p20_lognorm:.4f}")
print(f"Persentil 80: {p80_lognorm:.4f}")
print(f"Varians: {var_lognorm:.4f}")
print(f"Standar Deviasi: {std_lognorm:.4f}")
print(f"Skewness: {skew_lognorm:.4f}")
print(f"Kurtosis: {kurt_lognorm:.4f}")

# ==========================================
# 3. PEMBUATAN GRAFIK VISUALISASI
# ==========================================
# Visualisasi Kasus 1: Eksponensial
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Histogram & PDF
count, bins, ignored = axes[0].hist(data_exp, bins=25, density=True, alpha=0.6, color='#2b5c8f', edgecolor='black', label='Histogram Sampel (n=500)')
x_plot_exp = np.linspace(0, np.max(data_exp), 500)
axes[0].plot(x_plot_exp, stats.expon.pdf(x_plot_exp, scale=scale_exp), 'r-', lw=2.5, label='PDF Teoretis ($\lambda=0.5$)')
axes[0].axvline(mean_exp, color='green', linestyle='--', lw=2, label=f'Mean ({mean_exp:.2f} s)')
axes[0].axvline(median_exp, color='purple', linestyle=':', lw=2, label=f'Median ({median_exp:.2f} s)')
axes[0].axvline(p20_exp, color='orange', linestyle='-.', lw=1.5, label=f'P20 ({p20_exp:.2f} s)')
axes[0].axvline(p80_exp, color='brown', linestyle='-.', lw=1.5, label=f'P80 ({p80_exp:.2f} s)')
axes[0].set_title('Distribusi Eksponensial: Jeda Waktu Transaksi Payment Gateway', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Waktu Antar-Kedatangan (detik)', fontsize=11)
axes[0].set_ylabel('Kepadatan Peluang (Density)', fontsize=11)
axes[0].legend(loc='upper right', fontsize=9)
axes[0].grid(True, linestyle=':', alpha=0.6)

# Subplot 2: Boxplot
box = axes[1].boxplot(data_exp, vert=False, patch_artist=True, boxprops=dict(facecolor='#a1c4fd', color='#1d4e89'))
axes[1].axvline(p20_exp, color='orange', linestyle='-.', lw=1.5, label=f'P20 ({p20_exp:.2f} s)')
axes[1].axvline(median_exp, color='purple', linestyle=':', lw=2, label=f'Median ({median_exp:.2f} s)')
axes[1].axvline(mean_exp, color='green', linestyle='--', lw=2, label=f'Mean ({mean_exp:.2f} s)')
axes[1].axvline(p80_exp, color='brown', linestyle='-.', lw=1.5, label=f'P80 ({p80_exp:.2f} s)')
axes[1].set_title('Boxplot Sebaran & Deteksi Outlier (Eksponensial)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Waktu Antar-Kedatangan (detik)', fontsize=11)
axes[1].set_yticks([])
axes[1].legend(loc='upper right', fontsize=9)
axes[1].grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('/var/www/html/statistik-dan-probabilitas/tugas/assets/exponential_distribution_analysis.png', dpi=300)
plt.close()

# Visualisasi Kasus 2: Lognormal
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Histogram & PDF
count, bins, ignored = axes[0].hist(data_lognorm, bins=25, density=True, alpha=0.6, color='#1e7e34', edgecolor='black', label='Histogram Sampel (n=500)')
x_plot_lognorm = np.linspace(np.min(data_lognorm), np.max(data_lognorm), 500)
axes[0].plot(x_plot_lognorm, stats.lognorm.pdf(x_plot_lognorm, s=sigma_lognorm, scale=np.exp(mu_lognorm)), 'r-', lw=2.5, label='PDF Teoretis ($\mu=5.7, \sigma=0.5$)')
axes[0].axvline(mean_lognorm, color='blue', linestyle='--', lw=2, label=f'Mean ({mean_lognorm:.1f} ms)')
axes[0].axvline(median_lognorm, color='purple', linestyle=':', lw=2, label=f'Median ({median_lognorm:.1f} ms)')
axes[0].axvline(p20_lognorm, color='orange', linestyle='-.', lw=1.5, label=f'P20 ({p20_lognorm:.1f} ms)')
axes[0].axvline(p80_lognorm, color='brown', linestyle='-.', lw=1.5, label=f'P80 ({p80_lognorm:.1f} ms)')
axes[0].set_title('Distribusi Lognormal: Waktu Respon Download CDN Aplikasi Mobile', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Latensi Respon (milidetik)', fontsize=11)
axes[0].set_ylabel('Kepadatan Peluang (Density)', fontsize=11)
axes[0].legend(loc='upper right', fontsize=9)
axes[0].grid(True, linestyle=':', alpha=0.6)

# Subplot 2: Boxplot
box = axes[1].boxplot(data_lognorm, vert=False, patch_artist=True, boxprops=dict(facecolor='#b8e994', color='#1e7e34'))
axes[1].axvline(p20_lognorm, color='orange', linestyle='-.', lw=1.5, label=f'P20 ({p20_lognorm:.1f} ms)')
axes[1].axvline(median_lognorm, color='purple', linestyle=':', lw=2, label=f'Median ({median_lognorm:.1f} ms)')
axes[1].axvline(mean_lognorm, color='blue', linestyle='--', lw=2, label=f'Mean ({mean_lognorm:.1f} ms)')
axes[1].axvline(p80_lognorm, color='brown', linestyle='-.', lw=1.5, label=f'P80 ({p80_lognorm:.1f} ms)')
axes[1].set_title('Boxplot Sebaran & Deteksi Outlier (Lognormal)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Latensi Respon (milidetik)', fontsize=11)
axes[1].set_yticks([])
axes[1].legend(loc='upper right', fontsize=9)
axes[1].grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('/var/www/html/statistik-dan-probabilitas/tugas/assets/lognormal_distribution_analysis.png', dpi=300)
plt.close()

print("\nVisualisasi grafik berhasil disimpan di tugas/assets/")
