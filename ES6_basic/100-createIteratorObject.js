function* createIteratorObject(reportObject) {
    const departments = reportObject.departments;
  
    for (const departmentName in departments) {
      if (departments.hasOwnProperty(departmentName)) {
        const employees = departments[departmentName].employees;
  
        for (const employee of employees) {
          yield { department: departmentName, employee: employee };
        }
      }
    }
  }
  
  // Example usage:
  const report = {
    departments: {
      department1: {
        employees: ['employee1', 'employee2', 'employee3'],
      },
      department2: {
        employees: ['employee4', 'employee5'],
      },
      // ... other departments
    },
  };
  
  const iterator = createIteratorObject(report);
  
  for (const employeeInfo of iterator) {
    console.log(`Department: ${employeeInfo.department}, Employee: ${employeeInfo.employee}`);
  }
  