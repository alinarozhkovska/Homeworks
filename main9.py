class MyClass:
    def __init__(self, file_name):
        self.file_name = file_name

    def create_attribute(self):
        with open(self.file_name) as domains:
            domen_list = [i.strip()[1:] for i in domains.readlines()]
        setattr(self, 'domains', domen_list)


    def names(self):
        with open(self.file_name) as names:
            names_list = [i.strip().split("\t")[1] for i in names.readlines()]
        return names_list


    def authors1(self):
        with open(self.file_name) as authors:
            authors_list = []
            for i in authors.readlines():
                if len(i.strip())>1 and i.strip()[0].isdigit():
                    authors_list += [{"date": i.strip()[:i.find("-")-1]}]
        return authors_list



    def authors2(self):

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        with open(self.file_name) as authors:
            authors_list = []
            for i in authors.readlines():
                if len(i.strip())>1 and i.strip()[0].isdigit():
                    
                    date_original = i.strip()[:i.find("-")-1]

                    
                    for j in date_original.split()[0]:
                        if j.isalpha():                            
                            dd = i[:i.find(j)-1]
                    mm = months.index(date_original.split()[1])+1
                    yyyy = date_original.split()[2]


                                  
                    date_modified = "/".join([dd,str(mm),yyyy])
                    
                    authors_list += [{"date_original": date_original}]
                    authors_list += [{"date_modified": date_modified}]

        return authors_list








domains = MyClass('domains.txt')
names = MyClass('names.txt')
authors1 = MyClass('authors.txt')
authors2 = MyClass('authors.txt')


domains.create_attribute()
print(domains.domains)
