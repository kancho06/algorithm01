all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# 총 시간 복잡도  O(N)
# 공간 복잡도도 O(N)
# 해쉬는 시간 복잡도의 효율은 극대화 시킬 수 있지만 공간 복잡도를 대신 사용한다.
def get_absent_student(all_array, present_array):
    student_dick = {}
    for key in all_array:       # O(N)
        student_dick[key] = True    # 공간 복잡도 O(N)

    for key in present_array:   # O(N)
        del student_dick[key]

    for key in student_dick.keys():
        return key


print(get_absent_student(all_students, present_students))