import datetime

class PersonValueError(TypeError):
    pass

class PersonTypeError(TypeError):
    pass


class Person:
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str)) and sex in ("女", "男"):
            raise PersonValueError(name, sex) 
        try: 
            birth = datetime.date(*birthday) #生成日期对象
        except:
            raise PersonValueError("Wrong date: ", birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num +=1

    def id(self):
        return self._id

    def name(self):
        return self._name
    
    def sex(self):
        return self._sex

    def brithday(self):
        return self._birthday
    
    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    def set_name(self,name):
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another._id

    #define class method
    @classmethod
    def num(cls):
        return Person._num

    def __str__(self):
        return " ".join((self._id, self._name, self._sex, str(self._birthday)))

    def details(self):
        return ", ".join(("编号"+ self._id, "姓名"+ self._name, "性别"+self._sex, "出生日期"+self._birthday))

p1 = Person("xxx", "女", (1995,7,30), "1201510111")
p2 = Person("www", "男", (1990,2,17), "1201380324") 

# 定义学生类（从Person类继承）
class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)
    
    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_num)
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def  set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("No this course setected: ", course_name)
        self._courses[course_name] = score
    
    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    # 重新定义“details”类方法
    def details(self):
        return ", ".join((Person.details(self), 
        "入学日期" + str(self._enroll_date),
        "院系" + self._department,
        "课程记录" + str(self.scores())))
        

