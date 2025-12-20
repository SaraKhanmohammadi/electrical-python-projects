# circuit_fault_detector.py
# Project 4 – AI Portfolio: Simple Electrical Circuit Fault Detector
# December 2025
# Author: Sara Khanmohammadi
# Transition from Electrical Engineering to AI/ML

print("=== Simple Electrical Circuit Fault Detector ===")
print("This tool detects basic faults in a circuit based on voltage and current measurements.\n")

# Nominal values for a sample 220V circuit with 100Ω load
NOMINAL_VOLTAGE = 220.0   # Nominal voltage in volts
NOMINAL_CURRENT = 2.2     # Nominal current in amps (P = V²/R ≈ 484W)
VOLTAGE_TOLERANCE = 0.1   # 10% tolerance for voltage

# Get user input
measured_voltage = float(input("Enter measured voltage (V): "))
measured_current = float(input("Enter measured current (A): "))

# Fault detection logic
print("\n--- Diagnosis ---")
if abs(measured_voltage - NOMINAL_VOLTAGE) > NOMINAL_VOLTAGE * VOLTAGE_TOLERANCE:
    if measured_voltage < NOMINAL_VOLTAGE * 0.5:
        print("⚠️ Fault: Open circuit or severe voltage drop")
    else:
        print("⚠️ Fault: Overvoltage condition")
elif measured_current > NOMINAL_CURRENT * 1.5:
    print("⚠️ Fault: Overload or short circuit")
elif measured_current < NOMINAL_CURRENT * 0.5:
    print("⚠️ Fault: Open circuit or high resistance")
else:
    power = measured_voltage * measured_current
    print("✓ Circuit is healthy!")
    print(f"Current power consumption: {power:.1f} Watts")

print("\nProject 4 of 12 – Portfolio for AI/ML career transition")
print("GitHub: https://github.com/SaraKhanmohammadi/electrical-python-projects")
