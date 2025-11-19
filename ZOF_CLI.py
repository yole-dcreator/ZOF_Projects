import math
import sys

def parse_function(expr, x):
    """Safely evaluate mathematical expression"""
    try:
        # Replace common math functions
        expr = expr.replace('^', '**')
        allowed_names = {
            'x': x,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'exp': math.exp,
            'log': math.log,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e
        }
        return eval(expr, {"__builtins__": {}}, allowed_names)
    except:
        raise ValueError("Invalid function expression")

def derivative(f_expr, x, h=1e-7):
    """Numerical derivative using central difference"""
    return (parse_function(f_expr, x + h) - parse_function(f_expr, x - h)) / (2 * h)

def bisection_method(f_expr, a, b, tol, max_iter):
    """Bisection Method"""
    print("\n=== BISECTION METHOD ===")
    print(f"{'Iter':<6} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12} {'Error':<12}")
    print("-" * 72)
    
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = parse_function(f_expr, c)
        fa = parse_function(f_expr, a)
        
        error = abs(b - a) / 2
        print(f"{i:<6} {a:<12.6f} {b:<12.6f} {c:<12.6f} {fc:<12.6e} {error:<12.6e}")
        
        if abs(fc) < tol or error < tol:
            print(f"\nRoot found: {c:.8f}")
            print(f"Final error: {error:.8e}")
            print(f"Iterations: {i}")
            return c
        
        if fa * fc < 0:
            b = c
        else:
            a = c
    
    print(f"\nMax iterations reached. Approximate root: {c:.8f}")
    return c

def regula_falsi(f_expr, a, b, tol, max_iter):
    """Regula Falsi (False Position) Method"""
    print("\n=== REGULA FALSI METHOD ===")
    print(f"{'Iter':<6} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12} {'Error':<12}")
    print("-" * 72)
    
    c_old = a
    for i in range(1, max_iter + 1):
        fa = parse_function(f_expr, a)
        fb = parse_function(f_expr, b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = parse_function(f_expr, c)
        
        error = abs(c - c_old)
        print(f"{i:<6} {a:<12.6f} {b:<12.6f} {c:<12.6f} {fc:<12.6e} {error:<12.6e}")
        
        if abs(fc) < tol or error < tol:
            print(f"\nRoot found: {c:.8f}")
            print(f"Final error: {error:.8e}")
            print(f"Iterations: {i}")
            return c
        
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        c_old = c
    
    print(f"\nMax iterations reached. Approximate root: {c:.8f}")
    return c

def secant_method(f_expr, x0, x1, tol, max_iter):
    """Secant Method"""
    print("\n=== SECANT METHOD ===")
    print(f"{'Iter':<6} {'x_n-1':<12} {'x_n':<12} {'x_n+1':<12} {'f(x_n+1)':<12} {'Error':<12}")
    print("-" * 78)
    
    for i in range(1, max_iter + 1):
        f0 = parse_function(f_expr, x0)
        f1 = parse_function(f_expr, x1)
        
        if abs(f1 - f0) < 1e-12:
            print("Division by zero encountered")
            return x1
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = parse_function(f_expr, x2)
        error = abs(x2 - x1)
        
        print(f"{i:<6} {x0:<12.6f} {x1:<12.6f} {x2:<12.6f} {f2:<12.6e} {error:<12.6e}")
        
        if abs(f2) < tol or error < tol:
            print(f"\nRoot found: {x2:.8f}")
            print(f"Final error: {error:.8e}")
            print(f"Iterations: {i}")
            return x2
        
        x0, x1 = x1, x2
    
    print(f"\nMax iterations reached. Approximate root: {x2:.8f}")
    return x2

def newton_raphson(f_expr, x0, tol, max_iter):
    """Newton-Raphson Method"""
    print("\n=== NEWTON-RAPHSON METHOD ===")
    print(f"{'Iter':<6} {'x_n':<12} {'f(x_n)':<12} {'f\'(x_n)':<12} {'x_n+1':<12} {'Error':<12}")
    print("-" * 84)
    
    x = x0
    for i in range(1, max_iter + 1):
        fx = parse_function(f_expr, x)
        fpx = derivative(f_expr, x)
        
        if abs(fpx) < 1e-12:
            print("Derivative too small, method fails")
            return x
        
        x_new = x - fx / fpx
        error = abs(x_new - x)
        
        print(f"{i:<6} {x:<12.6f} {fx:<12.6e} {fpx:<12.6e} {x_new:<12.6f} {error:<12.6e}")
        
        if abs(fx) < tol or error < tol:
            print(f"\nRoot found: {x_new:.8f}")
            print(f"Final error: {error:.8e}")
            print(f"Iterations: {i}")
            return x_new
        
        x = x_new
    
    print(f"\nMax iterations reached. Approximate root: {x:.8f}")
    return x

def fixed_point_iteration(g_expr, x0, tol, max_iter):
    """Fixed Point Iteration Method"""
    print("\n=== FIXED POINT ITERATION METHOD ===")
    print(f"{'Iter':<6} {'x_n':<12} {'g(x_n)':<12} {'x_n+1':<12} {'Error':<12}")
    print("-" * 66)
    
    x = x0
    for i in range(1, max_iter + 1):
        gx = parse_function(g_expr, x)
        x_new = gx
        error = abs(x_new - x)
        
        print(f"{i:<6} {x:<12.6f} {gx:<12.6f} {x_new:<12.6f} {error:<12.6e}")
        
        if error < tol:
            print(f"\nRoot found: {x_new:.8f}")
            print(f"Final error: {error:.8e}")
            print(f"Iterations: {i}")
            return x_new
        
        x = x_new
    
    print(f"\nMax iterations reached. Approximate root: {x:.8f}")
    return x

def modified_secant(f_expr, x0, delta, tol, max_iter):
    """Modified Secant Method"""
    print("\n=== MODIFIED SECANT METHOD ===")
    print(f"{'Iter':<6} {'x_n':<12} {'f(x_n)':<12} {'f(x_n+δx_n)':<14} {'x_n+1':<12} {'Error':<12}")
    print("-" * 84)
    
    x = x0
    for i in range(1, max_iter + 1):
        fx = parse_function(f_expr, x)
        fx_delta = parse_function(f_expr, x + delta * x)
        
        denom = fx_delta - fx
        if abs(denom) < 1e-12:
            print("Division by zero encountered")
            return x
        
        x_new = x - fx * delta * x / denom
        error = abs(x_new - x)
        
        print(f"{i:<6} {x:<12.6f} {fx:<12.6e} {fx_delta:<14.6e} {x_new:<12.6f} {error:<12.6e}")
        
        if abs(fx) < tol or error < tol:
            print(f"\nRoot found: {x_new:.8f}")
            print(f"Final error: {error:.8e}")
            print(f"Iterations: {i}")
            return x_new
        
        x = x_new
    
    print(f"\nMax iterations reached. Approximate root: {x:.8f}")
    return x

def main():
    print("=" * 60)
    print(" ZERO OF FUNCTIONS (ZOF) SOLVER - CLI ")
    print("=" * 60)
    
    print("\nAvailable Methods:")
    print("1. Bisection Method")
    print("2. Regula Falsi (False Position) Method")
    print("3. Secant Method")
    print("4. Newton-Raphson Method")
    print("5. Fixed Point Iteration Method")
    print("6. Modified Secant Method")
    
    try:
        choice = int(input("\nSelect method (1-6): "))
        
        if choice not in range(1, 7):
            print("Invalid choice!")
            return
        
        if choice == 5:
            print("\nEnter g(x) for fixed point iteration (x = g(x)):")
            print("Example: cos(x) or (x**2 + 2)/3")
            g_expr = input("g(x) = ")
            x0 = float(input("Initial guess x0: "))
        else:
            print("\nEnter function f(x):")
            print("Example: x**3 - x - 2 or sin(x) - x/2")
            f_expr = input("f(x) = ")
            
            if choice in [1, 2]:
                a = float(input("Enter a: "))
                b = float(input("Enter b: "))
            elif choice == 3:
                x0 = float(input("Enter x0: "))
                x1 = float(input("Enter x1: "))
            elif choice == 4:
                x0 = float(input("Enter initial guess x0: "))
            elif choice == 6:
                x0 = float(input("Enter initial guess x0: "))
                delta = float(input("Enter delta (perturbation factor, e.g., 0.01): "))
        
        tol = float(input("Enter tolerance (e.g., 1e-6): "))
        max_iter = int(input("Enter maximum iterations: "))
        
        # Execute selected method
        if choice == 1:
            bisection_method(f_expr, a, b, tol, max_iter)
        elif choice == 2:
            regula_falsi(f_expr, a, b, tol, max_iter)
        elif choice == 3:
            secant_method(f_expr, x0, x1, tol, max_iter)
        elif choice == 4:
            newton_raphson(f_expr, x0, tol, max_iter)
        elif choice == 5:
            fixed_point_iteration(g_expr, x0, tol, max_iter)
        elif choice == 6:
            modified_secant(f_expr, x0, delta, tol, max_iter)
            
    except ValueError as e:
        print(f"\nError: {e}")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()