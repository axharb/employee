class Employee:
    def __init__(self, data, read_permissions, write_permissions):
        self.data = data #data is dictionnary 
        self.write_permissions = write_permissions # permissions['employee0'][i] = {'birthdate',etc
        self.read_permissions = read_permissions
        self.logs = [] #request, role, 

    def write(self, role, write_data):
        log  = ['write', role]
        role_permissions =  self.write_permissions[role]
        for key, value in write_data.items():
            if key in role_permissions:
                self.data[key] = value
                log.append(key)
        self.logs.append(log)

    def read(self, role):
        res = {}
        log = ['read', role]
        role_permissions =  self.read_permissions[role]
        for key, value in   self.data.items():
            if key in role_permissions:
                res[key] = value
                log.append(key)
        self.logs.append(log)
        return res
    
    #for testing viewing changes
    def display(self):
        for key, value in self.data.items():
            print(key, value)
        



#Testing
write_permissions = {} 
write_permissions['employee'] = {'name', 'date_of_birth', 'work_email'}
write_permissions['organization'] = { 'work_email', 'is_exempt'}
write_permissions['specialist'] = { 'work_email', 'is_exempt', 'name', 'date_of_birth','specialist_notes'}

read_permissions = {} 
read_permissions['employee'] = {'name', 'date_of_birth', 'work_email'}
read_permissions['organization'] = {'name', 'is_exempt', 'work_email'}
read_permissions['specialist'] =  { 'work_email', 'is_exempt', 'name', 'date_of_birth','specialist_notes'}


data = {}
data['name'] = 'john'
data['work_email'] = 'john@g.com'
data['is_exempt'] = True
data['date_of_birth'] = '2016'
data['specialist_notes'] = 'None'

employee = Employee(data, read_permissions, write_permissions)

print('org',employee.read('organization'))
print('employee',employee.read('employee'))
print('specialist',employee.read('specialist'))

wdata = {}
wdata['name'] = 'mary'
wdata['work_email'] = 'maty@g.com'
wdata['is_exempt'] = False
wdata['date_of_birth'] = '2020'
wdata['specialist_notes'] = 'Hello'

employee.write('specialist', wdata)
employee.display()

print(employee.logs)



