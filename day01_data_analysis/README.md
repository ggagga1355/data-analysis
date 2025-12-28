## Day01 데이터 분석
- pandas로 CSV 데이터를 불러와 분석했습니다.
- matplotlib을 사용해 막대 그래프를 시각화했습니다.

## Trouble Shooting

### 1. CSV 파일 로드 오류
- 문제: FileNotFoundError 발생
- 원인: Python 실행 디렉토리와 CSV 파일 위치가 달랐음
- 해결: VS Code에서 '폴더 열기'로 프로젝트 폴더를 기준으로 실행함

### 2. matplotlib 그래프 에러
- 문제: AttributeError: module 'matplotlib'has no attribute 'bar'
- 원인: matplotlib가 아닌 matplotlib.pyplot 모듈을 import해야 했음
- 해결: import matplotlib.pyplot as plt로 수정함
