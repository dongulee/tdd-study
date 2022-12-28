class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

class TestResult:
    def __init__(self):
        self.runCount = 0
    
    def testStarted(self):
        self.runCount += 1

    def summary(self):
        return "%d run, 0 failed" % self.runCount    

class WasRun(TestCase):
    def testMethod(self):
        self.log = self.log + "testMethod "
    
    def testBrokenMethod(self):
        raise Exception
    
    def setUp(self):
        self.log =  "setUp "
    
    def tearDown(self):
        self.log = self.log + "tearDown "

# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)

class TestCaseTest(TestCase):
    
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)
    
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()