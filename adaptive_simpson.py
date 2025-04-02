import numpy as np

def simpson(f, a, b):
    c = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4 * f(c) + f(b))

def adaptive_simpson(f, a, b, tol=1e-6, max_depth=100):
    c = (a + b) / 2
    s = simpson(f, a, b)  # Simpson's rule over the whole interval
    s1 = simpson(f, a, c)  # Simpson's rule over [a, c]
    s2 = simpson(f, c, b)  # Simpson's rule over [c, b]

    # Check if the error is within tolerance or max depth is reached
    if abs(s1 + s2 - s) < 15 * tol or max_depth == 0:
        return s1 + s2

    # Recursively subdivide the interval and integrate
    return (adaptive_simpson(f, a, c, tol / 2, max_depth - 1) +
            adaptive_simpson(f, c, b, tol / 2, max_depth - 1))


# Test the implementation
if __name__ == "__main__":
    # Test function: f(x) = x^2
    f = lambda x: x ** 2
    a, b = 0, 1  # Integration interval [0, 1]
    result = adaptive_simpson(f, a, b, tol=1e-6)
    expected = 1 / 3  # Analytical result: ∫(0 to 1) x^2 dx = 1/3
    print(f"Integration result: {result:.6f}")
    print(f"Expected value: {expected:.6f}")
    print(f"Error: {abs(result - expected):.6e}")