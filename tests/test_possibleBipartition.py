import unittest
from solutions.possibleBipartition import Solution

class TestPossibleBipartition(unittest.TestCase):
    def setUp(self) -> None:
        self.Solution = Solution()

    def test_possibleBipartition_test1(self):
        self.assertTrue(self.Solution.possibleBipartition(4, [[1,2],[1,3],[2,4]]))

    def test_possibleBipartition_test1(self):
        self.assertFalse(self.Solution.possibleBipartition(3, [[1,2],[1,3],[2,3]]))

    def test_possibleBipartition_test1(self):
        self.assertFalse(self.Solution.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))

    def test_possibleBipartition_test1(self):
        self.assertTrue(self.Solution.possibleBipartition(4, [[1,3],[2,4],[3,4]]))

    def test_possibleBipartition_test1(self):
        self.assertTrue(self.Solution.possibleBipartition(50, [[21,47],[4,41],[2,41],[36,42],[32,45],[26,28],[32,44],[5,41],[29,44],[10,46],[1,6],[7,42],[46,49],[17,46],[32,35],[11,48],[37,48],[37,43],[8,41],[16,22],[41,43],[11,27],[22,44],[22,28],[18,37],[5,11],[18,46],[22,48],[1,17],[2,32],[21,37],[7,22],[23,41],[30,39],[6,41],[10,22],[36,41],[22,25],[1,12],[2,11],[45,46],[2,22],[1,38],[47,50],[11,15],[2,37],[1,43],[30,45],[4,32],[28,37],[1,21],[23,37],[5,37],[29,40],[6,42],[3,11],[40,42],[26,49],[41,50],[13,41],[20,47],[15,26],[47,49],[5,30],[4,42],[10,30],[6,29],[20,42],[4,37],[28,42],[1,16],[8,32],[16,29],[31,47],[15,47],[1,5],[7,37],[14,47],[30,48],[1,10],[26,43],[15,46],[42,45],[18,42],[25,42],[38,41],[32,39],[6,30],[29,33],[34,37],[26,38],[3,22],[18,47],[42,48],[22,49],[26,34],[22,36],[29,36],[11,25],[41,44],[6,46],[13,22],[11,16],[10,37],[42,43],[12,32],[1,48],[26,40],[22,50],[17,26],[4,22],[11,14],[26,39],[7,11],[23,26],[1,20],[32,33],[30,33],[1,25],[2,30],[2,46],[26,45],[47,48],[5,29],[3,37],[22,34],[20,22],[9,47],[1,4],[36,46],[30,49],[1,9],[3,26],[25,41],[14,29],[1,35],[23,42],[21,32],[24,46],[3,32],[9,42],[33,37],[7,30],[29,45],[27,30],[1,7],[33,42],[17,47],[12,47],[19,41],[3,42],[24,26],[20,29],[11,23],[22,40],[9,37],[31,32],[23,46],[11,38],[27,29],[17,37],[23,30],[14,42],[28,30],[29,31],[1,8],[1,36],[42,50],[21,41],[11,18],[39,41],[32,34],[6,37],[30,38],[21,46],[16,37],[22,24],[17,32],[23,29],[3,30],[8,30],[41,48],[1,39],[8,47],[30,44],[9,46],[22,45],[7,26],[35,42],[1,27],[17,30],[20,46],[18,29],[3,29],[4,30],[3,46]]))

    def test_possibleBipartition_test1(self):
        self.assertTrue(self.Solution.possibleBipartition(100, [[26,47],[20,25],[23,60],[6,28],[30,41],[34,52],[5,57],[76,100],[39,92],[65,84],[28,88],[64,88],[31,80],[26,98],[67,80],[2,27],[68,92],[15,34],[39,97],[85,87],[53,62],[27,97],[36,67],[57,85],[8,38],[59,61],[14,34],[7,44],[35,52],[53,73],[54,73],[31,89],[44,55],[10,66],[5,93],[22,88],[83,90],[1,15],[30,51],[39,43],[29,89],[61,100],[68,97],[6,14],[82,87],[45,97],[61,94],[62,84],[16,29],[73,92],[35,61],[38,90],[43,45],[24,28],[40,86],[10,19],[39,57],[4,11],[35,79],[22,74],[14,95],[70,72],[43,83],[3,60],[36,37],[65,81],[29,75],[40,93],[84,89],[39,54],[13,63],[11,19],[12,20],[30,99],[72,90],[58,68],[21,48],[5,29],[59,64],[86,88],[2,82],[8,33],[32,46],[17,90],[54,82],[34,44],[2,4],[31,82],[7,70],[47,95],[1,18],[2,25],[50,63],[45,76],[2,51],[56,60],[23,55],[32,37],[23,45],[6,47],[37,42],[44,49],[9,17],[45,52],[43,71],[46,80],[87,88],[7,9],[20,68],[27,84],[33,57],[40,44],[39,76],[11,32],[35,63],[42,46],[16,53],[10,55],[18,55],[14,17],[10,17],[25,31],[56,91],[41,92],[16,90],[64,100],[70,78],[69,100],[25,43],[39,69],[15,73],[16,44],[14,24],[38,53],[3,85],[10,24],[67,73],[33,96],[18,65],[21,84],[56,72],[44,91],[32,84],[14,36],[66,97],[15,33],[14,78],[82,97],[54,62],[63,72],[55,63],[59,69],[78,90],[29,66],[42,58],[13,54],[45,57],[4,87],[90,100],[25,53],[33,63],[70,82],[6,11],[8,42],[31,36],[64,94],[25,47],[28,83],[75,81],[90,91],[92,100],[17,61],[64,83],[44,51],[55,67],[17,87],[11,25],[33,84],[57,94],[67,99],[14,88],[38,98],[5,23],[24,84],[20,36],[15,66],[41,47],[63,68],[18,27],[53,94],[36,58],[50,92],[31,66],[9,24],[42,54],[4,90],[17,98],[89,98],[2,83],[96,99],[86,99],[52,55],[74,86],[61,83],[62,67],[27,47],[28,40],[31,45],[27,69],[23,27],[66,98],[77,98],[65,79],[7,69],[57,82],[80,93],[43,99],[32,76],[20,39],[6,22],[54,60],[47,49],[13,64],[11,80],[9,32],[16,37],[25,96],[90,94],[54,72],[8,17],[30,68],[8,73],[22,91],[2,21],[46,77],[68,90],[91,98],[27,61],[23,51],[61,95],[23,41],[52,73],[15,71],[79,83],[38,63],[67,95],[4,29],[46,62],[23,72],[9,82],[74,96],[52,80],[31,38],[5,63],[11,36],[10,51],[55,90],[3,80],[64,66],[44,66],[34,97],[46,65],[23,65],[4,31],[37,83],[14,75],[9,91],[24,93],[78,87],[18,42],[89,93],[3,89],[67,77],[39,44],[76,89],[19,64],[7,93],[68,93],[10,72],[22,49],[70,95],[75,96],[6,20],[36,76],[34,76],[29,36],[12,92],[29,94],[75,92],[36,48],[31,88],[38,58],[44,78],[14,51],[9,99],[45,70],[19,47],[45,64],[28,74],[23,77],[82,84],[45,96],[2,39],[15,91],[33,58],[30,34],[17,31],[48,91],[11,33],[31,65],[77,87],[22,80],[41,93],[69,91],[66,79],[13,31],[19,52],[56,59],[26,57],[28,55],[97,100],[15,78],[54,88],[31,78],[29,74],[55,84],[12,63],[30,94],[12,81],[91,92],[33,97],[29,41],[8,77],[22,77],[21,63],[35,93],[37,51],[59,67],[52,89],[48,73],[61,73],[26,93],[33,46],[51,79],[2,77],[18,40],[12,54],[39,46],[65,67],[76,91],[8,94],[34,84],[43,65],[42,97],[46,78],[3,7],[36,96],[22,55],[14,80],[20,35],[70,89],[28,35],[29,34],[2,35],[4,52],[31,60],[28,72],[22,95],[14,49],[47,77],[8,65],[9,75],[63,74],[19,23],[93,100],[35,81],[11,77],[29,38],[52,85],[79,95],[42,47],[25,44],[79,99],[46,88],[19,54],[33,64],[46,66],[69,99],[34,92],[6,30],[15,72],[7,31],[61,78],[75,76],[40,58],[4,64],[7,53],[5,76],[12,57],[10,25],[67,72],[20,73],[46,99],[7,96],[51,58],[9,95],[8,36],[61,71],[36,47],[53,75],[36,53],[8,82],[39,52],[47,88],[3,99],[21,92],[56,80],[13,96],[70,83],[29,32],[25,64],[81,99],[4,54],[1,92],[9,12],[51,67],[37,49],[51,98],[39,63],[7,86],[42,86],[5,98],[27,29],[69,94],[57,71],[9,19],[34,67],[7,10],[30,38],[50,67],[63,71],[29,83],[78,79],[24,97],[6,81],[66,81],[64,65],[5,52],[19,56],[36,44],[4,30]]))