# Open API 기본

import requests
import webbrowser

# ===========================================================
# 1. 랜덤 강아지 사진 가져오기
# ===========================================================


def get_dog_image():
    try:
        url = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"요청 실패(상태 코드 : {response.status_code})")
            return

        data = response.json()
        print(data["message"])
        webbrowser.open(data["message"])

    except requests.exceptions.Timeout as e:
        print(f"서버 응답시간 초과: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")

# get_dog_image()


# ===========================================================
#  2. 랜덤 고양이 사진 가져오기
# ===========================================================
def get_cat_image():
    try:
        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"요청 실패(상태 코드 : {response.status_code})")
            return

        data = response.json()
        webbrowser.open(data[0]["url"])

    except requests.exceptions.Timeout as e:
        print(f"서버 응답시간 초과: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")

# get_cat_image()


# ===========================================================
#  3. 대학 검색하기
# ===========================================================
def get_univ_list(country="Korea, Republic of"):
    try:
        url = "http://universities.hipolabs.com/search"
        params = {
            "country": country
        }
        # params를 포함하여 서버에 요청
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            print(f"요청 실패(상태 코드 : {response.status_code})")
            return

        data = response.json()

        # 대학 수 출력
        print(f"대학 수: {len(data)}개")

        # 상위 5개 대학명 및 홈페이지 출력
        print("--- 상위 5개 대학 ---")
        for univ in data[:5]:
            name = univ.get("name")
            web_page = univ.get("web_pages", ["-"])[0]
            print(f"{name} ({web_page})")

    except requests.exceptions.Timeout as e:
        print(f"서버 응답시간 초과: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")


get_univ_list()
# get_univ_list("United States")


# ===========================================================
#  4. 날씨 조회하기
# ===========================================================
def get_weather(lat, lon):
    try:
        url = "https://api.open-meteo.com/v1/forecast"

        # 1) 파라미터 먼저 설정
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m",
        }

        # 2) params를 포함하여 요청 전송
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            print(f"요청 실패(상태 코드 : {response.status_code})")
            return

        data = response.json()
        print(data)

        # 3) 현재 온도 데이터 출력
        print(f"측정 일시: {data["current"]["time"]}")
        print(f"기온: {data["current"]["temperature_2m"]}")

        current_temp = data["current"]["temperature_2m"]
        unit = data["current_units"]["temperature_2m"]
        print(f"현재 온도: {current_temp}{unit}")

    except requests.exceptions.Timeout as e:
        print(f"서버 응답시간 초과: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")


get_weather(lat=37.3416467, lon=126.8310305)
