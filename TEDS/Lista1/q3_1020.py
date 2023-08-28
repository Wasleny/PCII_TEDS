idade = int(input())

print(f"{idade // 365} ano(s)")
print(f"{(idade % 365) // 30} mes(es)")
print(f"{(idade % 365) % 30} dia(s)")