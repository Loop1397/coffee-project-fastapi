string = 'https://shop-phinf.pstatic.net/20240209_48/1707410909143YMGM4_PNG/108546807828167167_922874094.png?type=f296_296'

index = string.find('?')
if index != -1:
    string = string[:index]

print(string)