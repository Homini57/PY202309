# 학생 이름 및 성적을 저장하는 클래스
class Student:
    이름 = ''
    국어 = 0
    수학 = 0
    영어 = 0
    def __init__(self, 이름, 국어, 수학, 영어):
        self.이름 = 이름
        self.국어 = 국어
        self.수학 = 수학
        self.영어 = 영어

    # 학생 별 성적의 평균 점수를 출력
    def get_average(self):
        sum_num = self.국어 + self.수학 + self.영어
        avr = sum_num / 3
        return avr

# 학생 별 성적들을 인스턴스에 저장
def loadData (lines):
    preprocessed_lines = []
    students_dict = {}
    grades_dict = {}
    student_list = []
    for line in lines:
        line = line.strip().split(',')
        preprocessed_lines.append(line)

    subject_list = preprocessed_lines.pop(0)
    
    for line in preprocessed_lines:
        학생 = Student(line[0], float(line[1]), float(line[2]), float(line[3]))
        student_list.append(학생)

    return student_list


lines = open("students.csv","r", encoding="utf8").readlines()

# TODO 1: 학생 정보를 딕셔너리에 저장
students_list = loadData(lines)

# TODO 2: 학생 별 평균 점수를 계산
print("------학생들의 평균 점수------")

for student in students_list:
    avr = student.get_average()
    print(f"{student.이름}의 평균 점수는{avr}입니다.")

file_name = "average.txt"
write_fp = open(file_name,'w',encoding = 'utf8')

# 학생 별 평균 점수를 파일에 저장
for student in students_list:
    avr = student.get_average()
    str_avr = student.이름 + "의 평균 점수는" + str(avr) + "입니다.\n"
    write_fp.write(str_avr)
write_fp.close()


