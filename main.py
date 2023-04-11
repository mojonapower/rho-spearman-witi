import pandas as pd
from scipy.stats import spearmanr

# Leer el archivo CSV
input_file = "witis.csv"
df = pd.read_csv(input_file)
print(df)
# Calcular la correlación entre las dos columnas
correlation = df["SFGM_FIX"].corr(df["NIVEL_CARGO_CAT"])

print("La correlación entre NO SPEARMAN RHO SFGM_FIX y NIVEL_CARGO_CAT es:", correlation)

correlation, _ = spearmanr(df["SFGM_FIX"], df["NIVEL_CARGO_CAT"])
correlation

print("La correlación entre SPEARMAN RHO SFGM_FIX y NIVEL_CARGO_CAT es:", correlation)