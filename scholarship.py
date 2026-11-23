

from datetime import datetime


MANDATORY_THRESHOLDS = (7.00, 75.0, 500000.0, 1, "Active")

# Initial sample dataset stored as a list of dictionaries
students_data = [
    {
        "student_id": "AUBC24001",
        "name": "Rahul Sen",
        "programme": "B.Com",
        "semester": 4,
        "cgpa": 8.24,
        "attendance": 82.0,
        "family_income": 380000.0,
        "backlogs": 0,
        "category": "General",
        "extracurricular": "Yes",
        "first_gen": "No",
        "disability": "No",
        "previous_scholarship": "No",
        "enrollment_status": "Active"
    },
    {
        "student_id": "AUBC24002",
        "name": "Ananya Das",
        "programme": "B.Sc Computer Science",
        "semester": 6,
        "cgpa": 9.15,
        "attendance": 92.0,
        "family_income": 250000.0,
        "backlogs": 0,
        "category": "SC",
        "extracurricular": "Yes",
        "first_gen": "Yes",
        "disability": "No",
        "previous_scholarship": "Yes",
        "enrollment_status": "Active"
    },
    {
        "student_id": "AUBC24003",
        "name": "Vikram Roy",
        "programme": "B.Tech",
        "semester": 4,
        "cgpa": 6.85,
        "attendance": 80.0,
        "family_income": 410000.0,
        "backlogs": 0,
        "category": "OBC",
        "extracurricular": "No",
        "first_gen": "Yes",
        "disability": "No",
        "previous_scholarship": "No",
        "enrollment_status": "Active"
    },
    {
        "student_id": "AUBC24004",
        "name": "Sneha Mukherjee",
        "programme": "B.A. English",
        "semester": 2,
        "cgpa": 7.80,
        "attendance": 70.0,
        "family_income": 620000.0,
        "backlogs": 2,
        "category": "General",
        "extracurricular": "Yes",
        "first_gen": "No",
        "disability": "No",
        "previous_scholarship": "No",
        "enrollment_status": "Active"
    },
    {
        "student_id": "AUBC24005",
        "name": "Arjun Nair",
        "programme": "BBA",
        "semester": 6,
        "cgpa": 8.65,
        "attendance": 88.0,
        "family_income": 320000.0,
        "backlogs": 0,
        "category": "General",
        "extracurricular": "No",
        "first_gen": "No",
        "disability": "Yes",
        "previous_scholarship": "Yes",
        "enrollment_status": "Active"
    },
    {
        "student_id": "AUBC24006",
        "name": "Priya Verma",
        "programme": "B.Sc Physics",
        "semester": 4,
        "cgpa": 7.45,
        "attendance": 73.0,
        "family_income": 450000.0,
        "backlogs": 1,
        "category": "ST",
        "extracurricular": "Yes",
        "first_gen": "Yes",
        "disability": "No",
        "previous_scholarship": "No",
        "enrollment_status": "Active"
    },
    {
        "student_id": "AUBC24007",
        "name": "Rohan Kapoor",
        "programme": "B.Com",
        "semester": 2,
        "cgpa": 8.90,
        "attendance": 91.0,
        "family_income": 200000.0,
        "backlogs": 0,
        "category": "General",
        "extracurricular": "Yes",
        "first_gen": "No",
        "disability": "No",
        "previous_scholarship": "No",
        "enrollment_status": "Inactive"
    }
]


# ==============================================================================
# 8.1 DISPLAY APPLICATIONS
# ==============================================================================
def display_students(students=students_data):
    """Displays all available scholarship applications in a formatted table."""
    if not students:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 115)
    print(f"{'ID':<11} {'Name':<18} {'Prog.':<22} {'Sem':<4} {'CGPA':<6} {'Att%':<6} {'Income(Rs)':<11} {'Bklg':<5} {'Status':<8}")
    print("=" * 115)
    for s in students:
        print(
            f"{s['student_id']:<11} "
            f"{s['name']:<18} "
            f"{s['programme']:<22} "
            f"{s['semester']:<4} "
            f"{s['cgpa']:<6.2f} "
            f"{s['attendance']:<6.1f} "
            f"{s['family_income']:<11,.0f} "
            f"{s['backlogs']:<5} "
            f"{s['enrollment_status']:<8}"
        )
    print("=" * 115)


# ==============================================================================
# 8.2 VALIDATE STUDENT DATA
# ==============================================================================
def validate_student(student):
    """Validates student input values. Returns (is_valid, error_messages_list)."""
    errors = []

    if not str(student.get("student_id", "")).strip():
        errors.append("Student ID cannot be blank.")
    if not str(student.get("name", "")).strip():
        errors.append("Student Name cannot be blank.")

    cgpa = student.get("cgpa", -1)
    if not (0.0 <= cgpa <= 10.0):
        errors.append(f"Invalid CGPA ({cgpa}): must be between 0 and 10.")

    attendance = student.get("attendance", -1)
    if not (0.0 <= attendance <= 100.0):
        errors.append(f"Invalid Attendance ({attendance}%): must be between 0 and 100.")

    income = student.get("family_income", -1)
    if income < 0:
        errors.append(f"Invalid Family Income ({income}): cannot be negative.")

    backlogs = student.get("backlogs", -1)
    if backlogs < 0:
        errors.append(f"Invalid Backlogs ({backlogs}): cannot be negative.")

    return (len(errors) == 0, errors)


# ==============================================================================
# 8.3 - 8.7 INDIVIDUAL ELIGIBILITY CHECK FUNCTIONS
# ==============================================================================
def check_academic_eligibility(student):
    """Checks CGPA against prescribed criterion (>= 7.00)."""
    return student["cgpa"] >= MANDATORY_THRESHOLDS[0]


def check_attendance_eligibility(student):
    """Checks attendance percentage against prescribed criterion (>= 75%)."""
    return student["attendance"] >= MANDATORY_THRESHOLDS[1]


def check_income_eligibility(student):
    """Checks annual family income against prescribed criterion (<= 5,00,000)."""
    return student["family_income"] <= MANDATORY_THRESHOLDS[2]


def check_backlog_eligibility(student):
    """Checks number of backlogs against prescribed criterion (<= 1)."""
    return student["backlogs"] <= MANDATORY_THRESHOLDS[3]


def check_enrollment(student):
    """Checks whether the student is currently enrolled (Active)."""
    return student["enrollment_status"].strip().lower() == MANDATORY_THRESHOLDS[4].lower()


# ==============================================================================
# ADDITIONAL CONSIDERATIONS & ELIGIBILITY SCORE CALCULATION
# ==============================================================================
def evaluate_additional_considerations(student):
    """Evaluates merit, high attendance, extracurricular, and special considerations."""
    merit_bonus = student["cgpa"] >= 8.50
    high_attendance = student["attendance"] >= 90.0
    extracurricular_bonus = student["extracurricular"].strip().lower() == "yes"
    special_consideration = (
        student["first_gen"].strip().lower() == "yes"
        or student["disability"].strip().lower() == "yes"
    )

    return {
        "merit_bonus": merit_bonus,
        "high_attendance": high_attendance,
        "extracurricular_bonus": extracurricular_bonus,
        "special_consideration": special_consideration
    }


def calculate_eligibility_score(student):
    """
    Calculates a deterministic 100-point eligibility score:
    - CGPA component (up to 40 pts)
    - Attendance component (up to 25 pts)
    - Financial Need component (up to 20 pts)
    - Clean Academic Record / No Backlogs (5 pts)
    - Additional Considerations bonus (up to 10 pts)
    """
    cgpa_score = (student["cgpa"] / 10.0) * 40.0
    att_score = (student["attendance"] / 100.0) * 25.0

    if student["family_income"] <= 500000:
        income_score = ((500000 - student["family_income"]) / 500000.0) * 20.0
    else:
        income_score = 0.0

    backlog_score = 5.0 if student["backlogs"] == 0 else (2.5 if student["backlogs"] == 1 else 0.0)

    extras = evaluate_additional_considerations(student)
    bonus_score = 0.0
    if extras["extracurricular_bonus"]:
        bonus_score += 5.0
    if extras["special_consideration"]:
        bonus_score += 5.0

    total_score = round(cgpa_score + att_score + income_score + backlog_score + bonus_score, 2)
    return total_score


# ==============================================================================
# 8.8 CALCULATE ELIGIBILITY
# ==============================================================================
def calculate_eligibility(student):
    """
    Combines individual checks to determine final status:
    Highly Eligible, Eligible, Conditionally Eligible, or Not Eligible.
    """
    is_valid, errors = validate_student(student)
    if not is_valid:
        return {
            "status": "Invalid Data",
            "checks": {},
            "extras": {},
            "score": 0.0,
            "conditional_reason": "; ".join(errors)
        }

    acad_ok = check_academic_eligibility(student)
    att_ok = check_attendance_eligibility(student)
    inc_ok = check_income_eligibility(student)
    bklg_ok = check_backlog_eligibility(student)
    enr_ok = check_enrollment(student)

    checks = {
        "Academic Requirement": acad_ok,
        "Attendance Requirement": att_ok,
        "Income Requirement": inc_ok,
        "Backlog Requirement": bklg_ok,
        "Enrollment Requirement": enr_ok
    }

    extras = evaluate_additional_considerations(student)
    score = calculate_eligibility_score(student)
    conditional_reason = ""

    all_mandatory = acad_ok and att_ok and inc_ok and bklg_ok and enr_ok

    if all_mandatory:
        if student["cgpa"] >= 8.50 and student["attendance"] >= 85.0:
            status = "Highly Eligible"
        else:
            status = "Eligible"
    else:
        critical_ok = enr_ok and inc_ok and bklg_ok
        marginal_cgpa = (6.75 <= student["cgpa"] < 7.00) and att_ok
        marginal_att = (72.0 <= student["attendance"] < 75.0) and acad_ok

        if critical_ok and marginal_cgpa:
            status = "Conditionally Eligible"
            conditional_reason = (
                f"CGPA ({student['cgpa']:.2f}) is marginally below 7.00 (within 6.75–6.99 band); "
                "all other mandatory conditions satisfied."
            )
        elif critical_ok and marginal_att:
            status = "Conditionally Eligible"
            conditional_reason = (
                f"Attendance ({student['attendance']:.1f}%) is marginally below 75.0% (within 72.0%–74.9% band); "
                "all other mandatory conditions satisfied."
            )
        else:
            status = "Not Eligible"

    return {
        "status": status,
        "checks": checks,
        "extras": extras,
        "score": score,
        "conditional_reason": conditional_reason
    }


# ==============================================================================
# 8.9 GENERATE EXPLANATION
# ==============================================================================
def generate_explanation(student):
    """Produces a detailed, step-by-step explanation of the screening decision."""
    result = calculate_eligibility(student)
    lines = [
        "-" * 65,
        f"SCREENING REPORT FOR: {student['name']} ({student['student_id']})",
        f"Programme: {student['programme']} | Semester: {student['semester']} | Category: {student['category']}",
        "-" * 65
    ]

    if result["status"] == "Invalid Data":
        lines.append(f"VALIDATION ERROR: {result['conditional_reason']}")
        return "\n".join(lines)

    lines.append("Mandatory Criterion Evaluation:")
    for criterion, passed in result["checks"].items():
        badge = "PASS" if passed else "FAIL"
        lines.append(f"  {criterion:<26} -> {badge}")

    lines.append("\nAdditional Considerations:")
    extras = result["extras"]
    lines.append(f"  Merit Condition (CGPA >= 8.50)       : {'Yes' if extras['merit_bonus'] else 'No'}")
    lines.append(f"  High Attendance (Att >= 90%)         : {'Yes' if extras['high_attendance'] else 'No'}")
    lines.append(f"  Extracurricular Achievement          : {'Yes' if extras['extracurricular_bonus'] else 'No'}")
    lines.append(f"  Special Consideration (1st Gen/PwD)  : {'Yes' if extras['special_consideration'] else 'No'}")

    lines.append(f"\nCalculated Eligibility Score : {result['score']:.2f} / 100.00")
    lines.append(f"Final Decision               : {result['status'].upper()}")

    if result["status"] == "Highly Eligible":
        lines.append("Reason: Satisfies all mandatory conditions plus CGPA >= 8.50 and Attendance >= 85%.")
    elif result["status"] == "Eligible":
        lines.append("Reason: Satisfies all mandatory scholarship conditions.")
    elif result["status"] == "Conditionally Eligible":
        lines.append(f"Reason: {result['conditional_reason']}")
    else:
        failed_items = [k for k, v in result["checks"].items() if not v]
        lines.append(f"Reason: Violated critical mandatory condition(s): {', '.join(failed_items)}.")

    lines.append("-" * 65)
    return "\n".join(lines)


# ==============================================================================
# 8.10 GENERATE SCHOLARSHIP REPORT
# ==============================================================================
def generate_report(students):
    """Produces a consolidated screening report with summary statistics and timestamp."""
    now_str = datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")
    counts = {
        "Highly Eligible": 0,
        "Eligible": 0,
        "Conditionally Eligible": 0,
        "Not Eligible": 0,
        "Invalid Data": 0
    }

    print("\n" + "=" * 85)
    print("CONSOLIDATED SCHOLARSHIP SCREENING REPORT")
    print(f"Generated On: {now_str}")
    print("=" * 85)
    print(f"{'ID':<11} {'Student Name':<18} {'CGPA':<6} {'Att%':<6} {'Score':<8} {'Classification':<24}")
    print("-" * 85)

    for s in students:
        res = calculate_eligibility(s)
        status = res["status"]
        counts[status] = counts.get(status, 0) + 1
        print(
            f"{s['student_id']:<11} "
            f"{s['name']:<18} "
            f"{s['cgpa']:<6.2f} "
            f"{s['attendance']:<6.1f} "
            f"{res['score']:<8.2f} "
            f"{status:<24}"
        )

    print("-" * 85)
    print("SUMMARY STATISTICS:")
    print(f"  Total Applications Screened : {len(students)}")
    print(f"  Highly Eligible             : {counts['Highly Eligible']}")
    print(f"  Eligible                    : {counts['Eligible']}")
    print(f"  Conditionally Eligible      : {counts['Conditionally Eligible']}")
    print(f"  Not Eligible                : {counts['Not Eligible']}")
    print("=" * 85)


# ==============================================================================
# HELPER FUNCTIONS FOR MENU OPERATIONS
# ==============================================================================
def find_student_by_id(students, sid):
    """Searches for a student record by Student ID (case-insensitive)."""
    target = sid.strip().upper()
    for s in students:
        if s["student_id"].strip().upper() == target:
            return s
    return None


def filter_by_statuses(students, allowed_statuses):
    """Returns a list of tuples (student_dict, result_dict) matching allowed statuses."""
    matched = []
    for s in students:
        res = calculate_eligibility(s)
        if res["status"] in allowed_statuses:
            matched.append((s, res))
    return matched


def rank_eligible_students(students):
    """Ranks Highly Eligible and Eligible students using lambda sorting by score and CGPA."""
    eligible_pairs = filter_by_statuses(students, ("Highly Eligible", "Eligible"))

    ranked = sorted(
        eligible_pairs,
        key=lambda item: (item[1]["score"], item[0]["cgpa"]),
        reverse=True
    )

    if not ranked:
        print("\nNo eligible students available to rank.")
        return

    print("\n" + "=" * 88)
    print("MERIT RANKING OF ELIGIBLE SCHOLARSHIP APPLICANTS")
    print("=" * 88)
    print(f"{'Rank':<6} {'ID':<11} {'Name':<18} {'CGPA':<6} {'Att%':<6} {'Score':<8} {'Status':<18}")
    print("-" * 88)
    for idx, (s, res) in enumerate(ranked, start=1):
        print(
            f"{idx:<6} "
            f"{s['student_id']:<11} "
            f"{s['name']:<18} "
            f"{s['cgpa']:<6.2f} "
            f"{s['attendance']:<6.1f} "
            f"{res['score']:<8.2f} "
            f"{res['status']:<18}"
        )
    print("=" * 88)


def add_new_application(students):
    """Allows interactive entry of a new student scholarship application."""
    print("\n--- Enter New Student Application Details ---")
    try:
        sid = input("Student ID (e.g., AUBC24008): ").strip().upper()
        if find_student_by_id(students, sid):
            print("Error: A student with this ID already exists.")
            return

        name = input("Student Name: ").strip().title()
        programme = input("Programme (e.g., B.Com / B.Tech): ").strip()
        semester = int(input("Semester (1-8): ").strip())
        cgpa = float(input("CGPA (0.00 - 10.00): ").strip())
        attendance = float(input("Attendance Percentage (0 - 100): ").strip())
        income = float(input("Annual Family Income (INR): ").strip())
        backlogs = int(input("Number of Active Backlogs: ").strip())
        category = input("Category (General/SC/ST/OBC): ").strip().upper()
        extracurricular = input("Extracurricular Achievement (Yes/No): ").strip().capitalize()
        first_gen = input("First Generation Learner (Yes/No): ").strip().capitalize()
        disability = input("Disability Status (Yes/No): ").strip().capitalize()
        prev_sch = input("Previous Scholarship Status (Yes/No): ").strip().capitalize()
        enrollment = input("Enrollment Status (Active/Inactive): ").strip().capitalize()

        new_student = {
            "student_id": sid,
            "name": name,
            "programme": programme,
            "semester": semester,
            "cgpa": cgpa,
            "attendance": attendance,
            "family_income": income,
            "backlogs": backlogs,
            "category": category,
            "extracurricular": extracurricular,
            "first_gen": first_gen,
            "disability": disability,
            "previous_scholarship": prev_sch,
            "enrollment_status": enrollment
        }

        is_valid, errors = validate_student(new_student)
        if not is_valid:
            print("\nApplication Rejected due to validation errors:")
            for err in errors:
                print(f"  - {err}")
            return

        students.append(new_student)
        print(f"\nApplication for {name} ({sid}) added successfully!")

    except ValueError:
        print("\nInvalid numeric input entered. Application cancelled.")


# ==============================================================================
# 9. MENU-DRIVEN APPLICATION
# ==============================================================================
def main():
    """Main while-loop menu driver for the Scholarship Eligibility Screening System."""
    while True:
        print("\n" + "=" * 54)
        print("      SCHOLARSHIP ELIGIBILITY SCREENING SYSTEM")
        print("=" * 54)
        print("1.  Display All Applications")
        print("2.  Screen Individual Student")
        print("3.  Screen All Students (Detailed Explanations)")
        print("4.  Search Student")
        print("5.  Display Eligible Students (Highly Eligible & Eligible)")
        print("6.  Display Highly Eligible Students")
        print("7.  Rank Eligible Students")
        print("8.  Display Consolidated Scholarship Summary Report")
        print("9.  Display Screening Date and Time")
        print("10. Add New Student Application")
        print("11. Exit")
        print("=" * 54)

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            display_students(students_data)

        elif choice == "2":
            sid = input("Enter Student ID to screen: ").strip()
            student = find_student_by_id(students_data, sid)
            if student:
                print("\n" + generate_explanation(student))
            else:
                print(f"\nNo application found with Student ID '{sid}'.")

        elif choice == "3":
            for student in students_data:
                print("\n" + generate_explanation(student))

        elif choice == "4":
            query = input("Enter Student ID or Name to search: ").strip().lower()
            matches = [
                s for s in students_data
                if query in s["student_id"].lower() or query in s["name"].lower()
            ]
            if matches:
                display_students(matches)
                for m in matches:
                    print(generate_explanation(m))
            else:
                print(f"\nNo student matching '{query}' was found.")

        elif choice == "5":
            eligible_list = filter_by_statuses(students_data, ("Highly Eligible", "Eligible"))
            if eligible_list:
                print(f"\nTotal Eligible Applicants: {len(eligible_list)}")
                display_students([item[0] for item in eligible_list])
            else:
                print("\nNo eligible students found.")

        elif choice == "6":
            highly_eligible = filter_by_statuses(students_data, ("Highly Eligible",))
            if highly_eligible:
                print(f"\nTotal Highly Eligible Applicants: {len(highly_eligible)}")
                display_students([item[0] for item in highly_eligible])
            else:
                print("\nNo Highly Eligible students found.")

        elif choice == "7":
            rank_eligible_students(students_data)

        elif choice == "8":
            generate_report(students_data)

        elif choice == "9":
            current_dt = datetime.now().strftime("%A, %d %B %Y | %I:%M:%S %p")
            print(f"\nCurrent Screening Date & Time: {current_dt}")

        elif choice == "10":
            add_new_application(students_data)

        elif choice == "11":
            print("\nExiting Scholarship Eligibility Screening System. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 11.")


if __name__ == "__main__":
    main()