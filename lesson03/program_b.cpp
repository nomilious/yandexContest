#include <algorithm>
#include <iostream>
#include <limits>
#include <queue>
#include <vector>

struct Vortex {
  int num;
  int weight;
  Vortex(int num, int weight) {
    this->num = num;
    this->weight = weight;
  }

  bool operator<(const Vortex &other) const { return weight > other.weight; }
};
int findTheLighterPick(std::vector<int> weight, std::vector<bool> visited) {
  int min_weight = std::max(weight);
  int min_pick = -1;
  for (int i = 0; i < weight.size(); i++) {
    if (!visited[i] && weight[i] < min_weight) {
      min_weight = weight[i];
      min_pick = i;
    }
  }
  return min_pick;
}

int main() {
  int n, start, finish;
  int inf = 200;

  std::cin >> n >> start >> finish;

  start--;
  finish--;
  std::vector<std::vector<Vortex>> graph;
  std::vector<bool> visited(n, false);
  std::vector<int> parents(n, -1);
  std::vector<int> weight(n, inf);

  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) {
      int weight;
      std::cin >> weight;
      graph[i].push_back(Vortex(j, weight));
    }

  weight[start] = 0;
  int pick = start;
  while (pick != -1) {
    visited[pick] = true;
    for (int i = 0; i < graph[pick].size(); i++) {
      int connected_pick = graph[pick][i].num;
      int edge_weight = graph[pick][i].weight;
      if (visited[connected_pick] == 0) {
        int new_weight = weight[pick] + edge_weight;
        if (new_weight < weight[connected_pick]) {
          weight[connected_pick] = new_weight;
          parents[connected_pick] = pick;
        }
      }
    }
    pick = findTheLighterPick(weight, visited);
  }
  if (weight[finish] == inf)
    std::cout << ("-1");
  else {
    int way = findTheWay(parents, start, finish);
    for (auto i : way) {
      std::cout << i << " "
    }
  }
}
