# 문제
# 방금그곡
# 라디오를 자주 듣는 네오는 라디오에서 방금 나왔던 음악이 무슨 음악인지 궁금해질 때가 많다.
# 그럴 때 네오는 다음 포털의 '방금그곡' 서비스를 이용하곤 한다. 방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스이다.
# 네오는 자신이 기억한 멜로디를 가지고 방금그곡을 이용해 음악을 찾는다.
# 그런데 라디오 방송에서는 한 음악을 반복해서 재생할 때도 있어서 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다.
# 반대로, 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다.
# 그렇기 때문에 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다. 다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.
#
# 방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
# 네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
# 각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
# 음악이 00:00를 넘겨서까지 재생되는 일은 없다.
# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
# 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.

# 입력
# 입력으로 네오가 기억한 멜로디를 담은 문자열 m과 방송된 곡의 정보를 담고 있는 배열 musicinfos가 주어진다.
#
# m은 음 1개 이상 1439개 이하로 구성되어 있다.
# musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.
# 음악의 시작 시각과 끝난 시각은 24시간 HH:MM 형식이다.
# 음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다.
# 악보 정보는 음 1개 이상 1439개 이하로 구성되어 있다.

# 입출력 예시
# m = "ABCDEFG", "CC#BCC#BCC#BCC#B", "ABC"
# music_infos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# answer = "HELLO"
m = "ABCDEFG"
music_infos = ["12:00,12:14,HELLO,ABCDEFG", "13:00,13:05,WORLD,ABCDEF"]


# 방법1

def replace_sharps(notes):
    replace_dict = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for k, v in replace_dict.items():
        notes = notes.replace(k, v)
    return notes


def solution(m, music_infos):
    m = replace_sharps(m)  # #빼고 소문자 처리
    music_infos = [song.split(",") for song in music_infos]  # music_infos 를 돌면서 ',' 로 스플릿한 정보들을 다시 담는다
    song_infos = []
    for song in music_infos:
        time_infos = list(map(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]), song[:2]))  # [720, 734] 와같이 시간이 찍히는데 초로 변환한 후 두 숫자의 길이차이를 잰다.
        duration = time_infos[1] - time_infos[0]  # 빼서 곡의 길이 구하기
        notes = replace_sharps(song[3])  # #빼고 소문자 처리
        notes = notes * (duration // len(notes) + 1)  # 노트들 올림으로 +1 번더 반복시킨다 ex. ABC 가 ABCABCA 에서 끈켯다고 치면 3번 반복후 A 까지 자르기 위함
        notes = notes[:duration]  # duration 의 길이만큼 잘라내기 ex. 14개 ABCDEFGABCDEFG
        song_infos.append({'duration': duration, 'song_name': song[2], 'notes': notes,
                           'is_in': m in notes})  # is_in 으로 notes 가 m 에 들어있는지 boolean 으로 확인
    candidate = sorted(song_infos, key=lambda x: (x['is_in'], x['duration']), reverse=True)[0]  # candidate 에 is_in 이 ture 고 duration 이 큰애들 순으로 역정렬 해서 그 중 0 번째를 저장
    if candidate.get("is_in"):  # is_in 이 True 면 song_name return
        return candidate["song_name"]
    else:  # 없으면 (None) 반환
        return "(None)"


print(solution(m, music_infos))
