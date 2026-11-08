# Contributing to AmiFarmer

First, thank you for taking the time to contribute to **AmiFarmer**! 🌾

AmiFarmer is an open-source, research-grade agricultural operating system dedicated to empowering farmers globally—especially smallholder and marginal farmers across India—with physics-informed agronomy, stochastic hydrology, market arbitrage, and rural wealth incubation.

Whether you are an **agricultural scientist, agronomist, hydrologist, software engineer, or rural macro-economist**, your contributions are warmly welcomed.

---

## Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [Research & Engineering Philosophy](#research--engineering-philosophy)
3. [How Can I Contribute?](#how-can-i-contribute)
   - [Reporting Bugs & Anomalies](#reporting-bugs--anomalies)
   - [Proposing New Features & Engines](#proposing-new-features--engines)
   - [Expanding Regional Datasets (ICAR / CGWB / Crops)](#expanding-regional-datasets)
4. [Local Development Setup](#local-development-setup)
5. [Testing & Quality Assurance](#testing--quality-assurance)
6. [Pull Request Workflow](#pull-request-workflow)
7. [Style Guide & Conventions](#style-guide--conventions)

---

## Code of Conduct

This project adheres to the [Contributor Covenant v2.1](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report any unacceptable behavior to **Arpan Ghosh** at `arpanghosh984@gmail.com`.

---

## Research & Engineering Philosophy

1. **Biophysical Grounding over Generative Hallucination**: Every recommendation must be bounded by real-world physical and biochemical constraints (e.g., Liebig's Law of the Minimum, Penman-Monteith evapotranspiration, CGWB aquifer drawdown curves).
2. **Deterministic Safety & Farmer Welfare**: Chemical dosages must include strict Pre-Harvest Intervals (PHI) and follow Central Insecticide Board & Registration Committee (CIBRC) guidelines. Over-capitalization debt must be actively mitigated via Custom Hiring Center (CHC) rental modeling.
3. **Reproducibility**: All models and algorithms must include explicit unit tests verifying numerical convergence and analytical bounds.

---

## How Can I Contribute?

### Reporting Bugs & Anomalies
If you discover a numerical anomaly in fertilizer dosing, crop pricing equations, or UI rendering:
1. Check the [GitHub Issues](https://github.com/Arpanthebaap/AmiFarmer/issues) to ensure it has not already been reported.
2. Open a new issue with a clear title and description including:
   - Input farm parameters (State, District, Soil pH, N-P-K, Water Table).
   - Expected scientific outcome vs. observed outcome.
   - Traceback or screenshots.

### Expanding Regional Datasets
We actively seek peer-reviewed agronomic datasets for:
- State-specific subsidies and agricultural welfare policies.
- Localized crop cultivars and high-yielding hybrid benchmarks.
- District-level Central Ground Water Board (CGWB) aquifer trends.
- Localized APMC Mandi wholesale price models.

All data contributions should be placed in `amifarmer/data/` accompanied by citations in the commit description.

---

## Local Development Setup

1. **Fork and Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/AmiFarmer.git
   cd AmiFarmer
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Verify Installation**:
   ```bash
   python -m pytest tests/ -v
   streamlit run amifarmer/ui/app.py
   ```

---

## Testing & Quality Assurance

All new features and modifications **must pass the test suite** before being merged:

```bash
# Run the complete test suite
python -m pytest tests/ -v

# Run with coverage report
python -m pytest --cov=amifarmer tests/
```

Ensure that:
- Every new core engine module has a corresponding unit test in `tests/`.
- Pydantic models validate data strictly with type annotations.
- Numerical calculations do not throw division-by-zero on edge-case farm parameters.

---

## Pull Request Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feat/groundwater-recharge-model
   ```
2. Commit your changes using conventional commit messages:
   - `feat:` for new capabilities or algorithms.
   - `fix:` for bug fixes or mathematical corrections.
   - `docs:` for README, mathematical derivations, or guide updates.
   - `test:` for adding or updating unit tests.
3. Push to your fork:
   ```bash
   git push origin feat/groundwater-recharge-model
   ```
4. Open a **Pull Request** against the `main` branch of `Arpanthebaap/AmiFarmer`.
5. Clearly describe the scientific rationale, mathematical equations implemented, and test results.

---

## Attribution & Authorship

AmiFarmer is maintained by **Arpan Ghosh** and the open-source agricultural research community. Contributors will be credited in the `README.md` and project release notes.
