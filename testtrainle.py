import unittest 
import datetime

def my_brand(assignamentname):
    print("=*=*=*= Sanjana =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*=")
    print("=*=*=*=", assignmentname," =*=*=*=")
    print("=*=*=*=",datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),"=*=*=*=")

# In[4]:
assignmentname = "HW 01"
my_brand(assignmentname)

def classify_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False
def triangle_type(a,b,c):
        if a==b and b==c:
            print('Triangle is Equilateral.')
        elif a==b or b==c or a==c:
            print('Triangle is Isosceles.')
        else:
            print('Triangle is Scalane')
        if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
            print('Tringle is Right angle')

a=3
b=4
c=5
if classify_triangle(a, b, c):
    triangle_type(a, b, c)
else:
    print('Tringle is not possible from given sides.')

class TestTriangles(unittest.TestCase):
  
    def testset_1(self):
        self.assertEqual(classify_triangle(5,5,5),True,'Equilateral triangle')
        
    def testset_2(self):
        self.assertEqual(classify_triangle(4,5,4),False,'Isosceles')
        self.assertNotEqual(classify_triangle(3,4,3),False,'Scalene : should be Isosceles')
        self.assertNotEqual(classify_triangle(6,7,5),False,'Scalene : should be Isosceles')
        
    def testset_3(self):
        self.assertNotEqual(classify_triangle(7,6,5),False,'Isosceles')
        self.assertNotEqual(classify_triangle(5,6,6),False,'Isosceles : should be Scalene')
        self.assertNotEqual(classify_triangle(8,9,5),False,'Isosceles : should be Scalene')
        
    def testset_4(self):
        self.assertEqual(classify_triangle(3,4,5),True,'Isosceles : should be Scalene test')
        
if __name__ == '__main__':
    unittest.main()
