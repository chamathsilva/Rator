from adaptors.user.github import GithubAdaptor
from adaptors.user.stackoverflow import StackoverflowAdaptor
x = GithubAdaptor()
# print(x.username('ashanrupasinghe'))
# print(x.rate('tdevinda'))
# print(x.rate('THarsh'))


y = StackoverflowAdaptor()
print(y.rate('http://stackoverflow.com/users/5198749/'))
