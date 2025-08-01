
# Bayesian Analysis of Concrete Compressive Strength

This project applies Bayesian linear modeling techniques to the **Concrete Compressive Strength Dataset** from the UCI Machine Learning Repository. The primary objective is to analyze the relationship between material composition and compressive strength using probabilistic inference.

---

## 📘 Table of Contents

- [Bayesian Analysis of Concrete Compressive Strength](#bayesian-analysis-of-concrete-compressive-strength)
  - [📘 Table of Contents](#-table-of-contents)
- [🏗️ Concrete Compressive Strength Dataset – Introduction](#️-concrete-compressive-strength-dataset--introduction)
  - [📊 Dataset Summary](#-dataset-summary)
  - [🧪 Features (Ingredients in kg/m³):](#-features-ingredients-in-kgm)
- [📦 Environment Setup Guide (Windows 10/11)](#-environment-setup-guide-windows-1011)
  - [✅ 1. Install TDM-GCC (C++ Compiler)](#-1-install-tdm-gcc-c-compiler)
    - [➤ Steps:](#-steps)
    - [➤ Verify:](#-verify)
  - [✅ 2. Set Up Your Python Environment](#-2-set-up-your-python-environment)
    - [➤ Create a virtual environment (with `uv`):](#-create-a-virtual-environment-with-uv)
  - [✅ 3. Install Required Python Packages](#-3-install-required-python-packages)

---
# 🏗️ Concrete Compressive Strength Dataset – Introduction

The **Concrete Compressive Strength dataset** is a widely used benchmark for regression modeling, sourced from the UCI Machine Learning Repository. It contains experimental data on how the proportions of different concrete ingredients affect the material’s strength. Below is a typical setup used in compressive strength testing of concrete cylinders:

![Concrete Compression Test](docs/Compression-test-configuration-concrete-cylinder.png)

**Figure:** Compression test configuration for a concrete cylinder  
**Source:** [ResearchGate - Compression Test Configuration](https://www.researchgate.net/figure/Compression-test-configuration-concrete-cylinder_fig5_34173598)


## 📊 Dataset Summary

- **Objective**: Predict the **compressive strength** (in MPa) of concrete based on its ingredient mix.
- **Records**: 1,030 observations
- **Features**: 8 numerical input variables + 1 target
- **Target**: `Concrete compressive strength (MPa)`

## 🧪 Features (Ingredients in kg/m³):

| Feature             | Description |
|---------------------|-------------|
| Cement              | Cement content |
| Blast Furnace Slag  | Supplementary cementitious material |
| Fly Ash             | Alternative cementitious material |
| Water               | Water content |
| Superplasticizer    | Chemical additive to improve flow |
| Coarse Aggregate    | Gravel or crushed stone |
| Fine Aggregate      | Sand |
| Age                 | Curing time in days |

- **Target**: `Strength` – compressive strength of concrete after curing for 90 days.

---

# 📦 Environment Setup Guide (Windows 10/11)

This guide walks you through installing the necessary tools to run Bayesian models using [PyMC](https://www.pymc.io/) with compiler and performance support on a Windows system.


## ✅ 1. Install TDM-GCC (C++ Compiler)

PyMC uses [PyTensor](https://pytensor.readthedocs.io/) as a backend that benefits from C compilation. You'll need a working `g++` compiler.

### ➤ Steps:
1. Download the **"TDM-GCC x64 for 64-bit"** installer. [Download from here](https://github.com/jmeubank/tdm-gcc/releases/download/v10.3.0-tdm64-2/tdm64-gcc-10.3.0-2.exe)
2. Run the installer:
   - Choose **TDM-GCC 10.3.0-2.exe** (default is fine)   
   - Keep all components selected
   - Install to: `C:\TDM-GCC-64\` (or leave default)
### ➤ Verify:
Open Command Prompt and run:

```bash
g++ --version
```

You should see something like:

```
g++ (tdm64-1) 10.3.0
```

## ✅ 2. Set Up Your Python Environment

We recommend using [`uv`](https://github.com/astral-sh/uv) or `venv` to create a clean workspace.

### ➤ Create a virtual environment (with `uv`):

```bash
uv venv .venv
```

## ✅ 3. Install Required Python Packages

Install PyMC and performance libraries:

```bash
uv add pymc arviz numba pytensor
```
---