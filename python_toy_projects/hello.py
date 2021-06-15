import hello_module

print("메인 런 함수 실행")
name = hello_module.__name__
print(f'모듈의 전역변수 : { name }')