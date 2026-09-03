# Exploratory Experiments

This directory contains small, local numerical experiments related to the Sovereign Reality Engine concept. They are research probes, not production systems and not evidence that a physical implementation exists.

## Permanent throat model

[`permanent_throat_model.py`](permanent_throat_model.py) is a one-dimensional finite-difference toy model. It evaluates a specified effective `T_00` expression for a scalar-field profile under fixed boundary anchors and applies a regularized update rule.

Run it locally with:

```bash
python3 permanent_throat_model.py
```

The output is a diagnostic of the model as written. It does **not** solve the Einstein field equations, construct a spacetime metric, demonstrate a traversable wormhole, establish sustained negative energy in nature, or prove long-term numerical stability. The `c_s^2` floor is an explicit numerical regularization, and the fixed boundary conditions are part of the experiment rather than derived physical constraints.

Before drawing physical conclusions, the model would need a documented action and metric signature, a well-posed PDE derivation, convergence and energy-conservation tests, boundary-condition analysis, independent reproduction, and comparison against established analytical limits.

## Archived production-stack sketch

The exact supplied `production_stack.py` source is preserved in [`archive/production_stack.py`](archive/production_stack.py) for traceability. It is an **unvalidated design artifact**, not an installed service or release. It contains templates that reference GitHub Actions, GitLab CI, AWS ECS/ECR, Kubernetes, Prometheus, Grafana, Slack, and external health checks. Those integrations are not evidence that the corresponding infrastructure exists or has been tested.

The archive is intentionally separate from the runnable toy model. Do not execute its deployment methods against real infrastructure. Before any operational use, split the code by responsibility, declare dependencies, add tests and fixtures, replace hard-coded metrics with measured inputs, make external actions dry-run by default, and review every secret, endpoint, and permission boundary.
