"""Exploratory 1-D scalar-field diagnostic for the Sovereign Reality Engine.

This script is a toy numerical experiment, not a wormhole solver or a validation
of negative-energy physics. It computes the model's diagnostic T_00 expression
under fixed boundary conditions and reports whether the diagnostic becomes
negative at the center of the grid. It does not solve the Einstein equations,
construct a spacetime metric, or establish long-term stability.
"""

import numpy as np

GRID_SIZE = 500
TIME_STEPS = 1000
DT = 0.005
DX = 0.2
x = np.linspace(-50, 50, GRID_SIZE)

ALPHA = 0.75
LAMBDA = 2.0
SIGMA = 3.0


def lagrangian_density(X: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """Toy K-essence-style density: L(X, phi) = X + alpha X^2 - V(phi)."""
    potential = LAMBDA * (1.0 - np.tanh(phi / SIGMA) ** 2)
    return X + ALPHA * X**2 - potential


def compute_stress_tensor_T00(
    X: np.ndarray, phi_dot: np.ndarray, phi: np.ndarray
) -> np.ndarray:
    """Return the model's effective diagnostic energy-density expression."""
    dL_dX = 1.0 + 2.0 * ALPHA * X
    return phi_dot**2 * dL_dX - lagrangian_density(X, phi)


def run_diagnostic() -> list[tuple[int, np.ndarray, np.ndarray]]:
    """Run the finite-difference toy model with fixed boundary anchors."""
    phi = np.arctan(x / SIGMA)
    phi_dot = np.zeros(GRID_SIZE)
    snapshots: list[tuple[int, np.ndarray, np.ndarray]] = []

    for step in range(TIME_STEPS):
        dphi_dx = np.gradient(phi, DX)
        d2phi_dx2 = np.gradient(dphi_dx, DX)
        X = 0.5 * (phi_dot**2 - dphi_dx**2)
        T_00 = compute_stress_tensor_T00(X, phi_dot, phi)

        if step % max(1, TIME_STEPS // 5) == 0 or step == TIME_STEPS - 1:
            snapshots.append((step, T_00.copy(), phi.copy()))

        # This floor is a numerical regularization of the toy update, not a
        # proof that the underlying field equation remains hyperbolic.
        cs2_eff = np.maximum(1.0 + 2.0 * ALPHA * X, 0.05)
        dV_dphi = -(2.0 * LAMBDA / SIGMA) * np.tanh(phi / SIGMA) * (
            1.0 - np.tanh(phi / SIGMA) ** 2
        )
        phi_ddot = (d2phi_dx2 - dV_dphi) / cs2_eff

        phi_dot += phi_ddot * DT
        phi += phi_dot * DT
        phi[0], phi[-1] = -np.pi / 2, np.pi / 2
        phi_dot[0], phi_dot[-1] = 0.0, 0.0

    return snapshots


if __name__ == "__main__":
    snapshots = run_diagnostic()
    final_step, final_T00, _ = snapshots[-1]
    center = GRID_SIZE // 2

    print("=" * 60)
    print(f"TOY FIELD DIAGNOSTIC COMPLETE ({final_step + 1} steps)")
    print("=" * 60)
    print(f"Center diagnostic T_00 : {final_T00[center]:.6f}")
    print(f"Minimum diagnostic T_00: {np.min(final_T00):.6f}")
    print(f"Maximum diagnostic T_00: {np.max(final_T00):.6f}")
    print()
    print("INTERPRETATION: diagnostic output only; no physical or engineering")
    print("stability, wormhole construction, or Einstein-equation solution is claimed.")
