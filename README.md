# ZOF Project - Zero of Functions Solver

CSC 431: Computational Science and Numerical Methods  
Covenant University

## Project Overview

This project implements six numerical methods for finding roots of nonlinear equations:

1. **Bisection Method** - Interval halving method
2. **Regula Falsi Method** - False position method
3. **Secant Method** - Uses two initial guesses
4. **Newton-Raphson Method** - Uses derivative
5. **Fixed Point Iteration** - Iterative convergence
6. **Modified Secant Method** - Perturbed secant method

## Project Structure

```
ZOF_Project/
├── ZOF_CLI.py                      # Command-line interface
├── app.py                          # Flask web application
├── templates/
│   └── index.html                  # Web interface
├── requirements.txt                # Python dependencies
├── ZOF_hosted_webGUI_link.txt     # Deployment info
└── README.md                       # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Local Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/ZOF_Project.git
cd ZOF_Project
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Running the Applications

### CLI Application

Run the command-line interface:
```bash
python ZOF_CLI.py
```

**Example Usage:**
```
Select method (1-6): 1
Enter function f(x): x**3 - x - 2
Enter a: 1
Enter b: 2
Enter tolerance: 1e-6
Enter maximum iterations: 50
```

### Web Application

1. **Start the Flask server:**
```bash
python app.py
```

2. **Open your browser:**
Navigate to `http://localhost:5000`

3. **Use the interface:**
   - Select a numerical method
   - Enter the function (e.g., `x**3 - x - 2`)
   - Provide required parameters
   - Click "Calculate Root"

## Supported Function Syntax

When entering functions, use Python syntax:

| Operation | Syntax | Example |
|-----------|--------|---------|
| Power | `**` or `^` | `x**2` or `x^2` |
| Multiplication | `*` | `2*x` |
| Division | `/` | `x/2` |
| Sine | `sin(x)` | `sin(x)` |
| Cosine | `cos(x)` | `cos(x)` |
| Tangent | `tan(x)` | `tan(x)` |
| Exponential | `exp(x)` | `exp(x)` |
| Natural Log | `log(x)` | `log(x)` |
| Square Root | `sqrt(x)` | `sqrt(x)` |
| Pi | `pi` | `pi*x` |
| Euler's number | `e` | `e**x` |

**Example Functions:**
- Polynomial: `x**3 - x - 2`
- Trigonometric: `sin(x) - x/2`
- Exponential: `exp(x) - 3*x`
- Mixed: `x**2 - 2*sin(x)`

## Deployment Instructions

### Option 1: Deploy to Render.com

1. **Create a Render account** at https://render.com

2. **Create a new Web Service:**
   - Connect your GitHub repository
   - Select "Web Service"
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

3. **Deploy** and copy your live URL

### Option 2: Deploy to PythonAnywhere

1. **Create account** at https://www.pythonanywhere.com

2. **Upload files:**
   - Go to Files tab
   - Upload all project files

3. **Set up web app:**
   - Go to Web tab
   - Add a new web app
   - Choose Flask
   - Set working directory and WSGI file

4. **Reload** and get your URL

### Option 3: Deploy to Streamlit Cloud

If using Streamlit instead of Flask:

1. **Convert to Streamlit:**
   - Create `streamlit_app.py`
   - Use Streamlit components

2. **Deploy:**
   - Push to GitHub
   - Go to https://streamlit.io/cloud
   - Connect repository
   - Deploy

### Option 4: Deploy to Vercel

1. **Install Vercel CLI:**
```bash
npm i -g vercel
```

2. **Deploy:**
```bash
vercel
```

3. Follow prompts and get deployment URL

## Testing the Application

### Test Cases

**Test Case 1: Polynomial Root**
- Function: `x**3 - x - 2`
- Method: Bisection
- Interval: [1, 2]
- Expected Root: ~1.521

**Test Case 2: Trigonometric**
- Function: `cos(x) - x`
- Method: Newton-Raphson
- Initial Guess: 1.0
- Expected Root: ~0.739

**Test Case 3: Exponential**
- Function: `exp(x) - 3*x`
- Method: Secant
- Initial Guesses: 0.5, 1.0
- Expected Root: ~0.619

## Method-Specific Notes

### Bisection Method
- Requires interval [a, b] where f(a)·f(b) < 0
- Guaranteed convergence
- Slow but reliable

### Regula Falsi
- Similar to Bisection
- Often faster convergence
- May stall on one end

### Secant Method
- Requires two initial guesses
- No derivative needed
- Fast convergence

### Newton-Raphson
- Requires one initial guess
- Derivative computed numerically
- Very fast convergence near root

### Fixed Point Iteration
- Enter g(x) where x = g(x)
- Requires convergence condition |g'(x)| < 1
- Simple but limited

### Modified Secant
- Uses perturbation factor δ
- One initial guess needed
- Balance between Secant and Newton

## Troubleshooting

**Problem:** "Division by zero"
- **Solution:** Try different initial values or check if derivative exists

**Problem:** Method doesn't converge
- **Solution:** 
  - Increase maximum iterations
  - Try different initial values
  - Use a more suitable method

**Problem:** Invalid function error
- **Solution:** Check syntax, use `**` for powers, include `*` for multiplication

## Project Submission

1. **Complete the link file:**
```
Name: Your Name
Matric Number: Your Number
Live URL: https://your-app.onrender.com
GitHub Repository: https://github.com/yourname/ZOF_Project
```

2. **Verify GitHub structure:**
```
/ZOF_Project/
├── ZOF_CLI.py
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── ZOF_hosted_webGUI_link.txt
```

3. **Submit folder to Scorac.com**

## Credits

**Course:** CSC 431 - Computational Science and Numerical Methods  
**Institution:** Covenant University  
**Session:** 2024/2025 Alpha Semester

## License

This project is for educational purposes as part of CSC 431 coursework.
