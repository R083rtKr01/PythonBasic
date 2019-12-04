from Employee_Management.controller.CompanyController import CompanyController
from Employee_Management.model.Employee import Employee
from Employee_Management.model.Trainee import Trainee

cc = CompanyController()
# cc.addEmployeeOrTrainee(Employee("e1","e2","e1","e2","Junior DEV", 5000))
# cc.addEmployeeOrTrainee(Employee("e1","e2","e1","e2","Junior DEV", 5000))
# cc.addEmployeeOrTrainee("Pani Jadzia z gazowni")
# cc.addEmployeeOrTrainee(Trainee("p1","p2","p1","p2"))
cc.getEmployees()
#cc.getTraineeOrderByLogin()
#cc.getManagersOrderByLogin()
#cc.getManagersOrderByLoginASC()
# cc.setPrise(1000)
# cc.getTraineeOrderByLogin()
# cc.changeEmployeeSalary("t1",17234)

cc.deleteEmployeeOrTraineeWithPassConfirm("mk8")