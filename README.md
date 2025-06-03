# Technical-Screen-Assessment submission by Aaryan Dharmadhikari

# 📦 Thoughtful Package Sorter

This project contains a Python function that determines how packages should be dispatched by a robotic arm in Thoughtful’s automation factory based on their **volume** and **mass**.

## 🚀 Objective

Sort packages into appropriate categories:
- **STANDARD**: Not bulky and not heavy
- **SPECIAL**: Either bulky or heavy
- **REJECTED**: Both bulky and heavy

## 📏 Classification Rules

A package is considered:
- **Bulky** if:
  - Volume (Width × Height × Length) ≥ 1,000,000 cm³ **OR**
  - Any single dimension ≥ 150 cm
- **Heavy** if:
  - Mass ≥ 20 kg

## 🧠 Sorting Logic

| Bulky | Heavy | Classification |
|-------|--------|----------------|
| No    | No     | STANDARD       |
| Yes   | No     | SPECIAL        |
| No    | Yes    | SPECIAL        |
| Yes   | Yes    | REJECTED       |

## 📄 Function Definition

```python
def sort(width, height, length, mass) -> str:
    # Returns: "STANDARD", "SPECIAL", or "REJECTED"
