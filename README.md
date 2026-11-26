# Scholarship Eligibility Screening System

A rule-based Python console application that validates student scholarship applications, evaluates mandatory and conditional eligibility criteria, computes a deterministic 100-point eligibility score, ranks eligible applicants, and generates formatted screening reports.

---

## Key Features

- **Input Validation:** Checks for blank IDs/names and verifies numeric ranges for CGPA (`0.0–10.0`), attendance (`0%–100%`), family income (`>= 0`), and backlogs (`>= 0`).
- **Rule-Based Screening:** Evaluates five mandatory thresholds (`CGPA >= 7.00`, `Attendance >= 75.0%`, `Family Income <= 5,00,000`, `Backlogs <= 1`, and `Enrollment Status == "Active"`).
- **Tiered Classification:** Categorizes applicants into **Highly Eligible**, **Eligible**, **Conditionally Eligible** (marginal CGPA `6.75–6.99` or attendance `72.0%–74.9%` when critical checks pass), **Not Eligible**, or **Invalid Data**.
- **100-Point Scoring Model:** Scores applicants across CGPA (`40 pts`), attendance (`25 pts`), financial need (`20 pts`), backlog record (`5 pts`), and additional considerations such as extracurriculars and first-generation or disability status (`up to 10 pts`).
- **Merit Ranking & Reporting:** Ranks eligible students using `sorted()` with a `lambda` key `(score, cgpa)` and prints timestamped reports via `datetime`.
- **Interactive CLI Menu:** Supports viewing records, screening single or all students, searching by ID or name, filtering by eligibility tier, adding new applications, and checking current screening timestamps.

---

## Project Structure

The codebase is organized as a single self-contained Python script (`scholarship_screening.py` or your chosen filename) containing:

| Section | Purpose |
| :--- | :--- |
| **Constants & Sample Data** | Defines immutable `MANDATORY_THRESHOLDS` and initial `students_data` records (`AUBC24001`–`AUBC24007`). |
| **Display & Validation** | `display_students()` formats tabular output; `validate_student()` checks field constraints. |
| **Eligibility Checks & Scoring** | `check_*_eligibility()`, `check_enrollment()`, `evaluate_additional_considerations()`, and `calculate_eligibility_score()`. |
| **Decision Engine & Reports** | `calculate_eligibility()`, `generate_explanation()`, and `generate_report()`. |
| **Menu & Search Helpers** | `find_student_by_id()`, `filter_by_statuses()`, `rank_eligible_students()`, `add_new_application()`, and `main()`. |

---

## Requirements

- **Python:** 3.8 or higher
- **External Dependencies:** None (uses only the Python standard library `datetime`).

---

## How to Run

1. Save the script as `scholarship_screening.py`.
2. Open a terminal or command prompt in the script directory.
3. Run the program:

   #Developer Sudipta Bhattacharya
python scholarship_screening.py


