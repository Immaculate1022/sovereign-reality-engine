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
