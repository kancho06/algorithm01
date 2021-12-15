genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


# 문제
# 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.
# 노래는 인덱스 구분하며, 노래를 수록하는 기준은 다음과 같다.
# 속한 노래가 많이 재생된 장르를 먼저 수록한다.        # 장르별로 sort
# 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
# 노래의 장르를 나타내는 문자열 배열 genres 와 노래별 재생 횟수를 나타내는 정수 배열 plays 가 주어질 때,
# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 두곡씩 반환하시오.

# 장르 별로(key) 우선 재생된 횟수(value)를 저장해야 한다.
# dict 쓰자
# 장르 별로 곡의 정보 (인덱스, 재생횟수) 배열로 묶어 저장한다.
def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    n = len(genre_array)
    for i in range(n):  # 장르와 재생횟수를 각각의 딕셔너리에 key:value 로 추가해준다.
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)     # lambda 를 이용해 역정렬
    result = []
    for genre, _value in sorted_genre_play_array:   # 역정렬된 장르:재생 배열에서 장르별로 인덱스:재생수 어레이를 만든다.
        index_play_array = genre_index_play_array_dict[genre]
        print(index_play_array)
        sorted_index_play_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        print(sorted_index_play_array)
        for i in range(len(sorted_index_play_array)):   # 두곡씩만 선별
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
