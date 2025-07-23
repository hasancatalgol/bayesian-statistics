
# 🏗️ Concrete Compressive Strength Dataset – Introduction

The **Concrete Compressive Strength dataset** is a widely used benchmark for regression modeling, sourced from the UCI Machine Learning Repository. It contains experimental data on how the proportions of different concrete ingredients affect the material’s strength.

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

- **Target**: `Strength` – compressive strength of concrete after curing

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
uv pip install --upgrade pip setuptools
```

## ✅ 3. Install Required Python Packages

Install PyMC and performance libraries:

```bash
uv add pymc arviz numba pytensor
```
---