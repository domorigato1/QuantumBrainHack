grep -R "def handle_error" ~/quantum_project/money_module/
sed -i 's/oldError/newError/g' ~/quantum_project/money_module/*.py
