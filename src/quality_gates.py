
def evaluate_quality_gates(
    metrics,
    baseline_metrics,
    tests_passed=True,
    data_quality_passed=True,
    coverage=0.0,
    security_blockers=0
):
    """
    Vérifie les Quality Gates du pipeline MLOps.
    Retourne ACCEPTED ou REJECTED.
    """

    delta = 0.05

    gates = {}

    # G1 : Tests unitaires
    gates["G1 - Unit Tests"] = tests_passed

    # G2 : Data Quality
    gates["G2 - Data Quality"] = data_quality_passed

    # G3 : Accuracy
    gates["G3 - Accuracy"] = metrics["accuracy"] >= 0.60

    # G4 : F1-score
    gates["G4 - F1-score"] = metrics["f1"] >= 0.50

    # G5 : Code Coverage
    gates["G5 - Coverage"] = coverage >= 70.0

    # G6 : Security Scan
    gates["G6 - Security"] = security_blockers == 0

    # G7 : Non-regression
    accuracy_non_regression = (
        metrics["accuracy"] >= baseline_metrics["accuracy"] - delta
    )

    f1_non_regression = (
        metrics["f1"] >= baseline_metrics["f1"] - delta
    )

    gates["G7 - Non-regression"] = (
        accuracy_non_regression and f1_non_regression
    )

    # Affichage des résultats
    print("\nQUALITY GATES")

    for gate, passed in gates.items():
        status = "PASS" if passed else "FAIL"
        print(f"{gate}: {status}")

    # Décision finale
    if all(gates.values()):
        decision = "ACCEPTED"
    else:
        decision = "REJECTED"

    print("\nFinal decision:", decision)

    return decision
