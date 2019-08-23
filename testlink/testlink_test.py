
import testlink

manual = 1  # 手动
automation = 2  # 自动

# 连接test link
url = 'http://192.168.205.17/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
key = "a62718b68e80ca28cc9209883dd16ce0"
tlc = testlink.TestlinkAPIClient(url, key)

# 获取testlink上的信息
def get_information_test_project():
    print("Number of Projects      in TestLink: %s " % tlc.countProjects())
    print("Number of Platforms  (in TestPlans): %s " % tlc.countPlatforms())
    print("Number of Builds                   : %s " % tlc.countBuilds())
    print("Number of TestPlans                : %s " % tlc.countTestPlans())
    print("Number of TestSuites               : %s " % tlc.countTestSuites())
    print("Number of TestCases (in TestSuites): %s " % tlc.countTestCasesTS())
    print("Number of TestCases (in TestPlans) : %s " % tlc.countTestCasesTP())
    tlc.listProjects()

get_information_test_project()

# projects = tlc.getProjects()
# animbus = projects[0]
# topSuites = tlc.getFirstLevelTestSuitesForTestProject(animbus['id'])
# print(len(topSuites))
#
# suite = topSuites[0]
# for suite in topSuites:
#     print(suite['id'], suite['name'])


# 获取 test suite
def get_test_suite():
    projects = tlc.getProjects()
    top_suites = tlc.getFirstLevelTestSuitesForTestProject(projects[2]["id"])
    for suite in top_suites:
        print(suite["id"], suite["name"])

# 创建测试用例集
def create_test_suite(project_id, test_suite_name, test_suite_describe, father_id):
    if father_id == "":
        tlc.createTestSuite(project_id, test_suite_name, test_suite_describe)
        print("创建成功")
    else:
        tlc.createTestSuite(project_id, test_suite_name, test_suite_describe, parentid=father_id)

# create_test_suite(3,"testauto", "testautozeng","")

# 创建测试用例
def create_test_case(father_id, data):
    tlc.initStep(data[0][2], data[0][3], automation)
    for i in range(1, len(data)):
        tlc.appendStep(data[i][2], data[i][3], automation)
    tlc.createTestCase(data[0][0], father_id, "1", "admin", "", preconditions=data[0][1])

# create_test_case(9, ["aaaaaaaa", "bbbbbbbb", "ccccccccccc", "dddddddd"])

# 获取测试用例
def get_test_case(test_case_id):
    test_case = tlc.getTestCase(None, testcaseexternalid=test_case_id)
    for i in test_case:
        print ("序列", "执行步骤", "预期结果")
        for m in i.get("steps"):
            print (m.get("step_number"), m.get("actions"), m.get("expected_results"))

# get_test_case()

# 发送测试结果给testlink
def report_test_result(test_plan_id, test_case_id, test_result):
    tlc.reportTCResult(None, test_plan_id, None, test_result, "", guess=True,
                       testcaseexternalid=test_case_id, platformname="0")

report_test_result(2, 26, "pass")