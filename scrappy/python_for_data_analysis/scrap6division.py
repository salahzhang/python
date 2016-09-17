#这个代码之前还差个第5章代码，但是那个要跑好几天，先存着
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql', charset='utf-8')

cur = conn.cursor()
cur.execute("USE wikipedia")

class SolutionFound(RuntimeError):
	def __int__(self, message):
		self.message = message

def getLinks(fromPageId):
	cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
	if cur.rowcount == 0:
		return None
	else:
		return [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
	links = getLinks(currentPageId)
	if links:
		return dict(zip(links, [{}]*len(links)))
	return {}

#list must be null or include mutiple links#
def searchDepth(targetPageId, currentPageId, linkTree, depth):
	if depth == 0:
		return linkTree
	if not linkTree:
		linkTree = constructDict(currentPageId)
		if not linkTree:
			#skip if no link
			return{}
	if targetPageId in linkTree.keys():
		print("TARGET" +str(targetPageId)+ " FOUND!")
		raise SolutionFound("PAGE: " + str(currentPageId))

	for branchKey, branchValue in linkTree.items():
		try:
			#build recursive tree
			linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
		except SolutionFound as e:
			print(e.message)
			raise SolutionFound("PAGE: " + str(currentPageId))
	return linkTree

try:
	searchDepth(134951, 1, {}, 4)
	print("No solution found")
except SolutionFound as e:
	print(e.message)




