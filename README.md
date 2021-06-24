# Baekjoon Online Judge

For Algorithm Study

###Fail to solve

27-05 경찰차

### STAGE34 문자열 알고리즘 1

**KMP 알고리즘**

두개의 문자열 A, B 에서 A 에 B 가 포함되어 있는지 확인하는 KMP 알고리즘.  
B 를 분석하여 반복 일치하는 문구의 위치 및 길이를 저장하는 KMP table 을 만드는 것과, KMP table 을 이용하여 A를 탐색하는 과정으로 나누어짐.  

**트라이(TRIE)**

문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 저장구조.  
각 문자 노드에 다음 문자가 될 수 있는 자식 노드들을 저장해줌.  
빠른 탐색에 효과적이지만 각 노드에서 자식들에 대한 포인터를 모두 저장하고 있기 때문에 저장 공간의 크기가 크다는 단점이 있음.

###STAGE35 위상 정렬

**위상 정렬**

방향이 있는 그래프를 방향을 거스르지 않도록 나열하는 것. (가장 직관적인 예시는 선수과목이 있는 과목의 수강신청)  
각 꼭짓점의 다음 꼭짓점을 표시하는 tree 리스트와 진입 경로를 나타내는 in_degree 리스트를 이용.
적용하기 위해서는 싸이클이 없어야 함.