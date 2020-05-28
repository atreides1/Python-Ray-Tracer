from main import *

class Test_Vector(unittest.TestCase):
    def test_vector_add(self):
        v1 = Vector(1.0, 2.0, 3.0)
        v2 = Vector(4.0, 5.0, 6.0)
        self.assertEqual((v1+v2).componenets(), (5.0, 7.0, 9.0), "Should be (5.0, 7.0, 9.0)")
    def test_vector_subtract(self):
        v1 = Vector(1.0, 2.0, 3.0)
        v2 = Vector(4.0, 5.0, 6.0)
        self.assertEqual((v1-v2).componenets(), (-3.0, -3.0, -3.0), "Should be (-3.0, -3.0, -3.0)")
    def test_vector_scalar_multiplication(self):
        v1 = Vector(1.0, 2.0, 3.0)
        s = 5
        self.assertEqual((v1 * s).componenets(), (5.0, 10.0, 15.0), "Should be (5.0, 10.0, 15.0)")
    def test_vector_dot_product(self):
        v1 = Vector(1.0, 2.0, 3.0)
        v2 = Vector(4.0, 5.0, 6.0)
        self.assertEqual(v1.dot(v2), 32.0, "Should be 32")
    def test_vector_cross_product(self):
        v1 = Vector(1.0, 2.0, 3.0)
        v2 = Vector(4.0, 5.0, 6.0)
        self.assertEqual((v1.cross(v2)).componenets(), (-3.0, 6.0, -3.0), "Should be (-3.0, 6.0, -3.0)")
    def test_vector_magnitude(self):
        v1 = Vector(3.0, 4.0, 5.0)
        self.assertEqual(v1.magnitude(), math.sqrt(50), "Should be sqrt 50.")
    def test_vector_normalization(self):
        v1 = Vector(3.0, 4.0, 5.0)
        v1.normalize()
        self.assertEqual(v1.magnitude(), 1.0, "Should be 1.0")
    def test_vector_neg(self):
        v1 = Vector(1.0, 2.0, 3.0)
        -v1
        self.assertEqual(v1.componenets(), (-1.0,-2.0,-3.0), "Should be (-1.0,-2.0,-3.0)")
    def test_vector_plus_equal(self):
        v1 = Vector(1.0, 2.0, 3.0)
        v1 +=3
        self.assertEqual(v1.componenets(), (4.0,5.0,6.0), "Should be (4.0,5.0,6.0)")

class Test(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(3+3, 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
