from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def parse_function(expr, x):
    """Safely evaluate mathematical expression"""
    try:
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
    """Numerical derivative"""
    return (parse_function(f_expr, x + h) - parse_function(f_expr, x - h)) / (2 * h)

def bisection_method(f_expr, a, b, tol, max_iter):
    iterations = []
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = parse_function(f_expr, c)
        fa = parse_function(f_expr, a)
        error = abs(b - a) / 2
        
        iterations.append({
            'iteration': i,
            'a': round(a, 8),
            'b': round(b, 8),
            'c': round(c, 8),
            'fc': f"{fc:.6e}",
            'error': f"{error:.6e}"
        })
        
        if abs(fc) < tol or error < tol:
            return {'root': round(c, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': True}
        
        if fa * fc < 0:
            b = c
        else:
            a = c
    
    return {'root': round(c, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': False}

def regula_falsi(f_expr, a, b, tol, max_iter):
    iterations = []
    c_old = a
    
    for i in range(1, max_iter + 1):
        fa = parse_function(f_expr, a)
        fb = parse_function(f_expr, b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = parse_function(f_expr, c)
        error = abs(c - c_old)
        
        iterations.append({
            'iteration': i,
            'a': round(a, 8),
            'b': round(b, 8),
            'c': round(c, 8),
            'fc': f"{fc:.6e}",
            'error': f"{error:.6e}"
        })
        
        if abs(fc) < tol or error < tol:
            return {'root': round(c, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': True}
        
        if fa * fc < 0:
            b = c
        else:
            a = c
        c_old = c
    
    return {'root': round(c, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': False}

def secant_method(f_expr, x0, x1, tol, max_iter):
    iterations = []
    
    for i in range(1, max_iter + 1):
        f0 = parse_function(f_expr, x0)
        f1 = parse_function(f_expr, x1)
        
        if abs(f1 - f0) < 1e-12:
            return {'error': 'Division by zero encountered'}
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = parse_function(f_expr, x2)
        error = abs(x2 - x1)
        
        iterations.append({
            'iteration': i,
            'x0': round(x0, 8),
            'x1': round(x1, 8),
            'x2': round(x2, 8),
            'fx2': f"{f2:.6e}",
            'error': f"{error:.6e}"
        })
        
        if abs(f2) < tol or error < tol:
            return {'root': round(x2, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': True}
        
        x0, x1 = x1, x2
    
    return {'root': round(x2, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': False}

def newton_raphson(f_expr, x0, tol, max_iter):
    iterations = []
    x = x0
    
    for i in range(1, max_iter + 1):
        fx = parse_function(f_expr, x)
        fpx = derivative(f_expr, x)
        
        if abs(fpx) < 1e-12:
            return {'error': 'Derivative too small, method fails'}
        
        x_new = x - fx / fpx
        error = abs(x_new - x)
        
        iterations.append({
            'iteration': i,
            'xn': round(x, 8),
            'fx': f"{fx:.6e}",
            'fpx': f"{fpx:.6e}",
            'xn1': round(x_new, 8),
            'error': f"{error:.6e}"
        })
        
        if abs(fx) < tol or error < tol:
            return {'root': round(x_new, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': True}
        
        x = x_new
    
    return {'root': round(x, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': False}

def fixed_point_iteration(g_expr, x0, tol, max_iter):
    iterations = []
    x = x0
    
    for i in range(1, max_iter + 1):
        gx = parse_function(g_expr, x)
        x_new = gx
        error = abs(x_new - x)
        
        iterations.append({
            'iteration': i,
            'xn': round(x, 8),
            'gx': round(gx, 8),
            'xn1': round(x_new, 8),
            'error': f"{error:.6e}"
        })
        
        if error < tol:
            return {'root': round(x_new, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': True}
        
        x = x_new
    
    return {'root': round(x, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': False}

def modified_secant(f_expr, x0, delta, tol, max_iter):
    iterations = []
    x = x0
    
    for i in range(1, max_iter + 1):
        fx = parse_function(f_expr, x)
        fx_delta = parse_function(f_expr, x + delta * x)
        denom = fx_delta - fx
        
        if abs(denom) < 1e-12:
            return {'error': 'Division by zero encountered'}
        
        x_new = x - fx * delta * x / denom
        error = abs(x_new - x)
        
        iterations.append({
            'iteration': i,
            'xn': round(x, 8),
            'fx': f"{fx:.6e}",
            'fx_delta': f"{fx_delta:.6e}",
            'xn1': round(x_new, 8),
            'error': f"{error:.6e}"
        })
        
        if abs(fx) < tol or error < tol:
            return {'root': round(x_new, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': True}
        
        x = x_new
    
    return {'root': round(x, 8), 'iterations': iterations, 'final_error': f"{error:.8e}", 'converged': False}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.json
        method = data['method']
        tol = float(data['tolerance'])
        max_iter = int(data['max_iterations'])
        
        if method == 'bisection':
            f_expr = data['function']
            a = float(data['a'])
            b = float(data['b'])
            result = bisection_method(f_expr, a, b, tol, max_iter)
        
        elif method == 'regula_falsi':
            f_expr = data['function']
            a = float(data['a'])
            b = float(data['b'])
            result = regula_falsi(f_expr, a, b, tol, max_iter)
        
        elif method == 'secant':
            f_expr = data['function']
            x0 = float(data['x0'])
            x1 = float(data['x1'])
            result = secant_method(f_expr, x0, x1, tol, max_iter)
        
        elif method == 'newton_raphson':
            f_expr = data['function']
            x0 = float(data['x0'])
            result = newton_raphson(f_expr, x0, tol, max_iter)
        
        elif method == 'fixed_point':
            g_expr = data['function']
            x0 = float(data['x0'])
            result = fixed_point_iteration(g_expr, x0, tol, max_iter)
        
        elif method == 'modified_secant':
            f_expr = data['function']
            x0 = float(data['x0'])
            delta = float(data['delta'])
            result = modified_secant(f_expr, x0, delta, tol, max_iter)
        
        else:
            return jsonify({'error': 'Invalid method'}), 400
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)