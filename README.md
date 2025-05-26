<p align="center">
  <img src="assets/images/auraops_logo.png" alt="AuraOps Logo" width="90"/>
</p>

# AuraOps
AuraOps is a modular system for automated planning and resource allocation that combines geospatial intelligence, machine learning, and operational analytics.


**[In Progress]: XNN**, is a neighborhood-based classifier that computes label distributions from nearby events using spatial proximity, based on Cross-Tabulation Analysis. An interactive interface built with Streamlit allows users to explore these results in real time.

The XNN engine is based on research conducted as part of the author's master's dissertation at FEA-USP.

APA Citation
Cunha, D. P. R. (2023). Estimando um indicador de desempenho com machine learning para o serviço de patrulhamento preventivo municipal. Faculdade de Economia, Administração e Contabilidade, Universidade de São Paulo, São Paulo. [doi:10.11606/D.12.2023.tde-29052023-164445.](https://doi.org/10.11606/D.12.2023.tde-29052023-164445)


## 🚀 Features

- 🔎 **XNN**: Lightweight, interpretable spatial classifier
- 📍 Minimal input: just `label`, `lat`, and `lon`
- 🧪 YAML-based schema validation for structured data
- 🧭 Streamlit dashboard for exploration and interaction
- 🧰 Modular design ready for future engines (SVM, LSTM, etc.)

## 📌 Roadmap

- [ ] XNN engine implemented
- [ ] Streamlit dashboard bootstrapped
- [ ] YAML schema validation for input files
- [ ] Initial unit test coverage
- [ ] CLI support with argparse
- [ ] Map-based label distribution visualization
- [ ] BallTree optimization for large-scale inputs
- [ ] Dashboard theming and ACL


## 📁 Project Main Structure

```bash
auraops/
│
├── auraops/           # Main package
│   ├── main.py        # Entry point (Streamlit app)
│   ├── engines/       # Core logic (e.g. xnn.py)
│   ├── schemas/       # Data format definitions (YAML)
│   ├── utils/         # Loaders, validation, helpers
│   ├── app/           # Streamlit components (dashboard, layout)
│   └── services/      # Parsers and scrapers for data from statistical agencies
│       └── ssp_sp.py  # São Paulo State Secretariat of Public Security (SSP-SP)
│
├── data/              # Inputs and outputs
├── assets/            # Logo, images, media and resources
├── tests/             # Unit tests

```

## 📜 License

MIT License. See [LICENSE](./LICENSE)


## 👤 Author

Daniel Cunha  
[github.com/danielpedrocp](https://github.com/danielpedrocp)