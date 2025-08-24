import statistics

# Sample dataset
data = [10, 20, 30, 40, 50, 50, 60, 70]

# --- Measures of Central Tendency ---
print("Mean:", statistics.mean(data))             # Average
print("Median:", statistics.median(data))         # Middle value
print("Mode:", statistics.mode(data))             # Most frequent value
print("Multimode:", statistics.multimode(data))   # Multiple modes (if exist)

# --- Measures of Spread ---
print("Variance:", statistics.variance(data))     # Sample variance
print("Population Variance:", statistics.pvariance(data)) # Population variance
print("Standard Deviation:", statistics.stdev(data))       # Sample standard deviation
print("Population Std Dev:", statistics.pstdev(data))      # Population standard deviation

# --- Median Variants ---
print("Median Low:", statistics.median_low(data))     # Lower middle value
print("Median High:", statistics.median_high(data))   # Upper middle value
print("Median Grouped:", statistics.median_grouped(data))  # Median in continuous data

# --- Harmonic and Geometric Mean ---
print("Harmonic Mean:", statistics.harmonic_mean(data))   # Useful for rates
print("Geometric Mean:", statistics.geometric_mean(data)) # Useful for growth rates

# --- Quantiles ---
print("Quantiles:", statistics.quantiles(data, n=4))  # Quartiles (Q1, Q2, Q3)

# --- Correlation & Covariance (new in Python 3.10) ---
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

print("Covariance:", statistics.covariance(x, y))
print("Correlation:", statistics.correlation(x, y))
