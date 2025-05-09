## 🧠 Why Join DEMO, DRUG, and REAC?

Each FAERS file contains a part of a case:

- `DEMO`: patient information (age, sex, country)
- `DRUG`: drugs involved (names, role codes)
- `REAC`: adverse reactions reported

All are linked by `primaryid`, which represents one safety report.

Joining them gives a full view of:
- What happened (reaction)
- Who it happened to (patient)
- What drug(s) were involved

This allows:
- Analyzing side effects by demographics
- Identifying drugs with high-risk profiles
- Building visualizations for drug safety trends