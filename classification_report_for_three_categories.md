### Classification Stats Breakdown

#### Classification Report Recap:
| Class | Genre           | Precision | Recall | Support |
|-------|-----------------|-----------|--------|---------|
| 0     | Rap             | 0.85      | 0.84   | 133     |
| 1     | Jazz/Classical  | 0.66      | 0.79   | 153     |
| 2     | Country         | 0.75      | 0.60   | 143     |

---

### Rap (Class 0)
- **Precision:** 0.85  
- **Recall:** 0.84  
- **Support:** 133  

#### Calculations:
- **True Positives (TP):**
  $$
  TP = \text{Recall} \times \text{Support} = 0.84 \times 133 = 111.72 \approx 112
  $$
- **Guesses:**
  $$
  \text{Guesses} = \frac{TP}{\text{Precision}} = \frac{112}{0.85} \approx 132
  $$

#### Results:
- **Guesses for Rap:** 132  
- **Correct (TP):** 112  
- **Incorrect (False Positives):** 132 - 112 = 20  

---

### Jazz/Classical (Class 1)
- **Precision:** 0.66  
- **Recall:** 0.79  
- **Support:** 153  

#### Calculations:
- **True Positives (TP):**
  $$
  TP = \text{Recall} \times \text{Support} = 0.79 \times 153 = 120.87 \approx 121
  $$
- **Guesses:**
  $$
  \text{Guesses} = \frac{TP}{\text{Precision}} = \frac{121}{0.66} \approx 183
  $$

#### Results:
- **Guesses for Jazz/Classical:** 183  
- **Correct (TP):** 121  
- **Incorrect (False Positives):** 183 - 121 = 62  

---

### Country (Class 2)
- **Precision:** 0.75  
- **Recall:** 0.60  
- **Support:** 143  

#### Calculations:
- **True Positives (TP):**
  $$
  TP = \text{Recall} \times \text{Support} = 0.60 \times 143 = 85.8 \approx 86
  $$
- **Guesses:**
  $$
  \text{Guesses} = \frac{TP}{\text{Precision}} = \frac{86}{0.75} \approx 115
  $$

#### Results:
- **Guesses for Country:** 115  
- **Correct (TP):** 86  
- **Incorrect (False Positives):** 115 - 86 = 29  

---

### Final Summary:
| Genre           | Guesses | Correct (TP) | Incorrect (FP) | True Albums (Support) |
|-----------------|---------|--------------|----------------|-----------------------|
| Rap             | 132     | 112          | 20             | 133                   |
| Jazz/Classical  | 183     | 121          | 62             | 153                   |
| Country         | 115     | 86           | 29             | 143                   |
