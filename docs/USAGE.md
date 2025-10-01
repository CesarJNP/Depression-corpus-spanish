# USO RÁPIDO (Python)

```python
import pandas as pd
df = pd.read_csv('data/corpus.csv')
print(df.head())

# Conteo por clase
print(df['label'].value_counts(normalize=True))

# Ejemplo: dividir en train/test (si no usas los splits)
from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size=0.2, stratify=df['label'], random_state=42)
```
