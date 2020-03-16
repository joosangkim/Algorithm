# Tree
## Terms
* 루트 노드 - 자식 노드 - 형제 노드 
* 깊이(Depth)
* Leaf 노드: 자식이 없는 노드(끝 노드)
* 트리: 노드와 브랜치로 이루어진 **사이클**이 없는 자료구조

## 이진트리 / 이진탐색트리(BST)
* 이진트리: 최대 브랜치가 2개인 노드 
* 이진탐색트리: 이진트리 중 왼쪽노드는 작은 값, 오른쪽 노드는 큰 값 
  + 11(LeftChild) - 14(Parent) - 18(RightChild)
  + 데이터 검색 / 탐색속도 개선가능
> BST 구현
* 노드 클래스 구현: 노드 클래스는 값 / 왼쪽 / 오른쪽 브랜치를 갖음
* 노드 핸들러
  + 클래스 선언 시 루트 노드 생성
  + insert(v):
    - v > node.v -> put new Node(v) to right 
    - v < node.v -> put new Node(v) to left 
  + search(v):
    - v > node.v -> move to right
    - v < node.v -> move to left
  + remove(v): -> divided and concour
    - remove leaf node:
    - remove one child:
    - remove two childs:


```python
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class NodeHandler:
  def __init__(self, head):
    self.head = head 

  def insert(self, value):
    self.current_node = self.head
    while True:
      if value < self.current_node.value:  # <-- value is smaller than current node value
        if self.current_node.left != None:
          self.current_node = self.current_node.left
        else 
          self.current_node = Node(value)
          break
      else:
        if self.current_node.right != None: # <-- value is bigger than current node value
          self.current_node = self.current_node.right
        else 
          self.current_node = Node(value)
          break  

  def search(self, value):
    self.current_node = self.head 
    while self.current_node:
      if self.current_node.value == value:
        return True 
      elif self.current_node.value < value:
        self.current_node = self.current_node.right
      else:
        self.current_node = self.current_node.left
    return False

```