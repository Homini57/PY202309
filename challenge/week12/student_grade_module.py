from student import loadData 

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


