def is_inverse(n, lst):
    # إنشاء القائمة المعكوسة
    inverse_list = [0] * n
    for index, value in enumerate(lst):
        inverse_list[value - 1] = index + 1
    
    # التحقق مما إذا كانت القائمة المعطاة تطابق القائمة المعكوسة
    return lst == inverse_list

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        lst = list(map(int, data[index:index + n]))
        index += n
        
        if is_inverse(n, lst):
            results.append("inverse")
        else:
            results.append("not inverse")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

