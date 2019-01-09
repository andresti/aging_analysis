import ROOT
import sys

ROOT.gROOT.ProcessLine("""
struct testResults {
    short shortPlusOne() const { return 1; }
    short shortMinusOne() const { return -1; }
    int intPlusOne() const { return 1; }
    int intMinusOne() const { return -1; }
    long longPlusOne() const { return 1; }
    long longMinusOne() const { return -1; }
    long long longlongPlusOne() const { return 1444261665; }
    long long longlongMinusOne() const { return -1444261665; }
};
""")

print("ROOT Version: %s" % ROOT.gROOT.GetVersion())
print("python Version: %s" % sys.version)

tests = ROOT.testResults()
for type in ["short", "int", "long", "longlong"]:
    for name, value in [("PlusOne", 1), ("MinusOne", -1)]:
        member = "%s%s" % (type, name)
        result = getattr(tests, member)()
        print("%s() == %s, should be %s" % (member, result, value))
