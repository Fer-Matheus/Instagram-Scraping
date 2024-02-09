# List of dependencies to install
$dependencies = @(
    "selenium",
    "BeautifulSoup4",
    "pandas"
)

# Create a virtual environment
if (-not (Test-Path venv)) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Install dependencies using pip install
foreach ($dependency in $dependencies) {
    Write-Host "Installing $dependency..."
    pip install $dependency
}
