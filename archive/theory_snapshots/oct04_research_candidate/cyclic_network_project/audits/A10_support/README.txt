A10 independent audit-only package

Read ../A10_saddle_node_and_bistability.pdf; edit/compile the standalone ../A10_saddle_node_and_bistability.tex.
The mathematical body of P10 is not included or replaced. Exact target and audit output hashes are in audit_identity.json.
input_inventory.json and draft_member_hashes.json authenticate the original current files. prerequisite_body_authentication.json verifies the eight prerequisite header body hashes.
line_by_line_review.csv covers all 707 P10 lines in 62 contiguous PASS ranges. line_review_data.py reproduces that ledger.
Run independent_checks.py with Python 3 and NumPy to reproduce independent_results.json, matrix_cases.csv and static_search.csv. Floating-point results may differ slightly by platform.
Run authenticate_inputs.py from the original research workspace, or pass its path as an argument, to recheck the supplied draft and working copy. This requires the original input archives, deliberately not duplicated here.
Developer validation was inventoried, not rerun; see validation_provenance.txt and developer_validation_inventory.json.
See preservation_report.json and presentation_QA.txt for final preservation and PDF checks. package_member_hashes.json covers every other delivered member and deliberately excludes itself.
No P10 source, manifest or lifecycle metadata is edited. The original P10 development chat owns administrative closure and cyclic_network_project_P10_audited.zip. P11 is cleared only after that closure and is not begun here.
