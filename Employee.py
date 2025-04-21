import numpy as np
import matplotlib.pyplot as plt
def visualize_salaries(employee_list):
    try:
        if not employee_list:
            print("No employee data available for visualization.")
            return
        
        # Extract names and salaries
        names = [emp.name for emp in employee_list]
        salaries = [emp.calculate_gross_salary() for emp in employee_list]

        # Bar Graph - Employee Salaries
        plt.figure(figsize=(12, 5))
        plt.bar(names, salaries, color='skyblue')
        plt.xlabel("Employees")
        plt.ylabel("Salary (Rs)")
        plt.title("Employee Salaries - Bar Graph")
        plt.xticks(rotation=30)
        plt.show()

        # Pie Chart - Salary Distribution
        plt.figure(figsize=(7, 7))
        plt.pie(salaries, labels=names, autopct="%1.1f%%", colors=['blue', 'green', 'red', 'purple', 'orange'])
        plt.title("Salary Distribution - Pie Chart")
        plt.show()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

class Employee:
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        self.emp_id = emp_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_gross_salary(self):
            if self.hours_worked > 40:
                regular_hours = 40
                overtime_hours = self.hours_worked - 40
                overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
                return (regular_hours * self.hourly_rate) + overtime_pay
            else:
                return self.hours_worked * self.hourly_rate
    def calculate_tax(self):
        gross_salary = self.calculate_gross_salary()
        if gross_salary > 50000:
            return gross_salary * 0.2  # 20% tax for salaries > 50,000
        elif gross_salary > 20000:
            return gross_salary * 0.1  # 10% tax for salaries > 20,000
        else:
            return 0  # No tax for salaries <= 20,000

    def calculate_net_salary(self):
        return self.calculate_gross_salary() - self.calculate_tax()
def add_employee(employee_list):
    try:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        hourly_rate = float(input("Enter Hourly Rate: "))
        hours_worked = float(input("Enter Hours Worked: "))
        employee = Employee(emp_id, name, hourly_rate, hours_worked)
        employee_list.append(employee)
        print(f"Employee {name} added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for Hourly Rate and Hours Worked.")
def display_payroll(employee_list):
    print(f"{'ID':<10}{'Name':<15}{'Gross Salary':<15}{'Tax':<10}{'Net Salary':<15}")
    print("-" * 60)
    for emp in employee_list:
        print(f"{emp.emp_id:<10}{emp.name:<15}{emp.calculate_gross_salary():<15.2f}"
              f"{emp.calculate_tax():<10.2f}{emp.calculate_net_salary():<15.2f}")
def save_to_file(employee_list, filename="payroll.txt"):
    try:
        with open(filename, "w") as file:
            for emp in employee_list:
                file.write(f"{emp.emp_id},{emp.name},{emp.hourly_rate},{emp.hours_worked}\n")
        print(f"Payroll data saved to {filename} successfully!")
    except IOError:
        print("Error saving payroll data to file.")
def load_from_file(filename="payroll.txt"):
    employee_list = []
    try:
        with open(filename, "r") as file:
            for line in file:
                emp_id, name, hourly_rate, hours_worked = line.strip().split(",")
                employee = Employee(emp_id, name, float(hourly_rate), float(hours_worked))
                employee_list.append(employee)
    except FileNotFoundError:
        print(f"No file found named {filename}. Starting with an empty payroll.")
    return employee_list
def payroll_statistics(employee_list):
    try:
        if not employee_list:
            print("No employee data available for statistics.")
            return
        gross_salaries = np.array([emp.calculate_gross_salary() for emp in employee_list])

        print("\n╔════════════════════════════════════════════╗")
        print("║           Employee Payroll Statistics      ║")
        print("╚════════════════════════════════════════════╝")
        print("------------------------------------------------")
        print(f"Total Payroll: ₹{np.sum(gross_salaries):.2f}")
        print(f"Average Salary: ₹{np.mean(gross_salaries):.2f}")
        print(f"Highest Salary: ₹{np.max(gross_salaries):.2f}")
        print(f"Lowest Salary: ₹{np.min(gross_salaries):.2f}")
        print(f"Salary Standard Deviation: ₹{np.std(gross_salaries):.2f}")
        print("------------------------------------------------")
    except Exception as e:
        print("An error occurred while calculating statistics:", e)

def sort_employees_by_salary(employee_list):
    gross_salaries = np.array([emp.calculate_gross_salary() for emp in employee_list])
    sorted_indices = np.argsort(-gross_salaries)  # Sort in descending order

    print("\n╔══════════════════════════════════════════╗")
    print("║      Employees Sorted by Gross Salary    ║")
    print("╚══════════════════════════════════════════╝")
    print("------------------------------------------------")
    for idx in sorted_indices:
        emp = employee_list[idx]
        print(f"{emp.name:<20}: Gross Salary = ₹{gross_salaries[idx]:.2f}")
    print("------------------------------------------------")

def search_employee(employee_list):
    search_term = input("Enter Employee ID or Name to search: ").lower()
    found = False
    for emp in employee_list:
        if emp.emp_id.lower() == search_term or emp.name.lower() == search_term:
            print(f"Found Employee: {emp.emp_id}, {emp.name}, Hourly Rate: {emp.hourly_rate}, Hours Worked: {emp.hours_worked}")
            found = True
            break
    if not found:
        print("No employee found with the given ID or Name.")
def update_employee(employee_list):
    try:
        emp_id = input("Enter Employee ID to update: ").lower()
        for emp in employee_list:
            if emp.emp_id.lower() == emp_id:
                print(f"Current Details: Name: {emp.name}, Hourly Rate: {emp.hourly_rate}, Hours Worked: {emp.hours_worked}")
                emp.name = input("Enter new Name (leave blank to keep current): ") or emp.name
                emp.hourly_rate = float(input("Enter new Hourly Rate (leave blank to keep current): ") or emp.hourly_rate)
                emp.hours_worked = float(input("Enter new Hours Worked (leave blank to keep current): ") or emp.hours_worked)
                print(f"Employee {emp.emp_id} updated successfully!")
                return
        print("No employee found with the given ID.")
    except ValueError:
        print("Invalid input. Please enter a valid number for Hourly Rate and Hours Worked.")
def delete_employee(employee_list):
    emp_id = input("Enter Employee ID to delete: ").lower()
    for emp in employee_list:
        if emp.emp_id.lower() == emp_id:
            confirmation = input(f"Are you sure you want to delete Employee {emp.name} (ID: {emp.emp_id})? (yes/no): ").lower()
            if confirmation == "yes":
                employee_list.remove(emp)
                print(f"Employee {emp_id} deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    print("No employee found with the given ID.")
def generate_salary_slip(employee_list):
    try:
        emp_id = input("Enter Employee ID to generate salary slip: ").lower()
        for emp in employee_list:
            if emp.emp_id.lower() == emp_id:
                with open(f"{emp.name}_salary_slip.txt", "w") as file:
                    file.write(f"Salary Slip for {emp.name} (ID: {emp.emp_id})\n")
                    file.write("="*30 + "\n")
                    file.write(f"Hourly Rate: {emp.hourly_rate}\n")
                    file.write(f"Hours Worked: {emp.hours_worked}\n")
                    file.write(f"Gross Salary: {emp.calculate_gross_salary():.2f}\n")
                    file.write(f"Tax Deducted: {emp.calculate_tax():.2f}\n")
                    file.write(f"Net Salary: {emp.calculate_net_salary():.2f}\n")
                    file.write("="*30 + "\n")
                print(f"Salary slip for {emp.name} generated successfully!")
                return
        print("No employee found with the given ID.")
    except:
        print("exception occured")

def main():
    employee_list = load_from_file()
    while True:
        print("\n" + "="*40)
        print("      🏢 EMPLOYEE PAYROLL SYSTEM 🏢")
        print("="*40)
        print("🔹 1️⃣  Add Employee")
        print("🔹 2️⃣  Display Payroll")
        print("🔹 3️⃣  Search Employee")
        print("🔹 4️⃣  Update Employee")
        print("🔹 5️⃣  Delete Employee")
        print("🔹 6️⃣  Generate Salary Slip")
        print("🔹 7️⃣  Save Payroll to File")
        print("🔹 8️⃣  Display Payroll Statistics")
        print("🔹 9️⃣  Sort Employees by Salary")
        print("🔹 🔟  Graphical Representation 📊")
        print("🔹 1️⃣1️⃣  Exit ❌")
        print("="*40)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee(employee_list)
        elif choice == "2":
            display_payroll(employee_list)
        elif choice == "3":
            search_employee(employee_list)
        elif choice == "4":
            update_employee(employee_list)
        elif choice == "5":
            delete_employee(employee_list)
        elif choice == "6":
            generate_salary_slip(employee_list)
        elif choice == "7":
            save_to_file(employee_list)
        elif choice == "8":
            payroll_statistics(employee_list)
        elif choice == "9":
            sort_employees_by_salary(employee_list)    
        elif choice == "10":
            visualize_salaries(employee_list)
        elif choice == "11":
            print("╔════════════════════════════════════╗")
            print("║                                    ║")
            print("║  Exiting the program. Goodbye!     ║")
            print("║                                    ║")
            print("╚════════════════════════════════════╝")
            break
        else:
            print("Invalid choice! Please try again.")


main()
        