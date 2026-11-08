from src.quality_gates import evaluate_quality_gates

# Métriques du modèle de référence
baseline_metrics = {
    "accuracy": 0.85,
    "f1": 0.80
}

# Métriques du nouveau modèle
candidate_metrics = {
    "accuracy": 0.82,
    "f1": 0.76
}

decision = evaluate_quality_gates(
    metrics=candidate_metrics,
    baseline_metrics=baseline_metrics,
    tests_passed=True,
    data_quality_passed=True,
    coverage=85.0,
    security_blockers=0
)

print("\nRésultat final :", decision)
