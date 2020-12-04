import os

class Archive:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def to_map(self):
        return {
            'name': self.name
        ,   'size': self.size
    }


def get_arquives(directory):
    archives = []

    archives_aux = os.listdir(directory)

    for archive in archives_aux:
        path = str(directory + archive)
        if os.path.isfile(path):            
            size = os.stat(path).st_size
            archive = Archive(path, size)
            archives.append(archive)

    archives.sort(key=lambda x:x.size)
    
    return archives


directory = input('Inform The Directory')
result = ''

if os.path.exists(directory):
    response = get_arquives(directory)
    response.reverse()
    result = response
    
elif directory == '':
    response = get_arquives(os.getcwd())
    response.reverse()
    result = response
else:
    print('Not found directory')


if result != '':
    file_aux = open('at-python.txt', 'w')

    for r in result:
        file_aux.writelines(str(r.to_map()) + '\n')
    
    file_aux.close()



