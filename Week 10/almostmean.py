"""almostmean"""
def almost_mean():
    """Student"""
    cnt_student = int(input())
    classroom = []
    total_score = 0

    for _ in range(cnt_student):
        student_info = input().split("\t")
        _id, _score = int(student_info[0]), float(student_info[1])
        total_score += _score
        classroom.append((_id, _score))

    mean = total_score / cnt_student
    ans = (-1, -1)

    for student_tuple in classroom:  # Changed variable name to avoid conflict
        if student_tuple[1] <= mean and ans[1] < student_tuple[1]:
            ans = student_tuple

    print(f"{ans[0]}\t{ans[1]}")

almost_mean()
