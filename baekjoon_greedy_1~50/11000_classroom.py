# 문제
# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.
# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!
#
# 입력
# 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
# 이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)
#
# 출력
# 강의실의 개수를 출력하라.
import heapq


n = int(input())
time_list = []
for i in range(n):
    s, e = map(int, input().split())
    time_list.append([s, e])

time_list.sort(key=lambda x: x[0])
end_time = []
heapq.heappush(end_time, time_list[0][1])
for i in range(1, n):
    if end_time[0] > time_list[i][0]:       # 수업끝나는 시간이 다음 수업 시작시간보다 클때 다음 수업끝나는 시간을 추가 heapq 특성상 0번째 인덱스로 추가됨.
        heapq.heappush(end_time, time_list[i][1])
    else:       # 수업끝나는 시간이 다음 수업 시작시간보다 적을때 (같은 강의실에서 바로 다음 수업을 진행할 수 있을 경우) 원래있던 시간을 pop 으로 제거해주고 다음수업 종료시간을 저장
        heapq.heappop(end_time)
        heapq.heappush(end_time, time_list[i][1])

print(len(end_time))
