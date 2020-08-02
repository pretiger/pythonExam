# w: 처음부터 쓰기, a: 마지막에 추가모드,
# f = open('test.txt', 'a', encoding='utf-8')
# f.write('테스트입니다.')

# f = open('test.txt', 'r', encoding='utf-8')
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# print(f.read())
# f.seek(0)
# print(f.read())
# f.close()

for i in range(1, 11):
    with open(str(i)+'date report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write('{0} date report'.format(i))
        report_file.write('\n부서:')
        report_file.write('\n사번:')
        report_file.write('\n이름:')
