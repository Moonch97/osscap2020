# osscap2020

## Pacman game with LED_Matrix
LED_Matrix화면과 컴퓨터화면으로 팩맨을 플레이한다. 

## 게임 프로그램 설치
github홈페이지에서 Final_pacman 폴더에 있는 소스코드 다운로드

## 사용법
게임 모드. 
게임 모드는 1P모드를 제공한다. 게임 시작 후 팩맨 맵이 출력되면서 게임이 시작된다. 
사용자플레이어: 사용자가 플레이하는 팩맨은 노란색점으로 지정
고스트: 고스트는 빨간 점으로 지정
맵: 플레이맵은 파란색으로 지정

컴퓨터와 LED_Matrix 를 이용하여 게임 진행
사용자는 키보드의 W, A, S, D 키를 이용하여 조작
사용자가 움직일때마다 4마리의 고스트도 랜덤으로 이동

컴퓨터화면에서 게임 메시지 출력
## 게임 설명
1P MODE:
사용자의 이동 : 사용자는 맵에 놓여진 점 먹이 들을 맵을 이동하면서 스코어를 획득해야함
모든 먹이를 획득한경우 고스트를 잡을 수 있음
고스트의 이동 : 고스트는 사용자가 이동할때마다 변칙적으로 이동함
#### 승리 조건: 이동한 거리에 비례하여 점수 획득
#### 패배 조건: 플레이어가 고스트에 닿으면 플레이어가 사망하여 게임이 종료된다.

# 시연 유튜브 영상 링크
https://youtu.be/95qZDG3lBz0








