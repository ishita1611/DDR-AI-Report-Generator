# DDR AI Report Generator

An AI-assisted workflow that converts inspection reports and thermal scan documents into a structured **Detailed Diagnostic Report (DDR)**.

This system extracts textual observations and images from PDF inspection reports and generates a clear, client-friendly diagnostic report.

---

## Objective

The goal of this project is to automate the process of analyzing technical inspection documents and generating a structured report that includes:

- Property Issue Summary
- Area-wise Observations
- Probable Root Cause
- Severity Assessment
- Recommended Actions
- Additional Notes
- Missing or Unclear Information

---

## System Workflow

The pipeline works as follows:

Inspection Report (PDF)  
Thermal Report (PDF)  

↓

Text Extraction (PyMuPDF)

↓

Image Extraction (largest image per page)

↓

Page-wise Processing

↓

Area-wise Observations Generation

↓

Structured DDR Report Generation

---

## Project Structure
