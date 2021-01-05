"""
    目的：python模拟生成人的姓名、地址、职业、电话信息
    前提：从github安装仓库
            git clone https://github.com/joke2k/faker.git
            python setup.py install
"""
from faker_master.faker import Faker

# fake = Faker()
fake = Faker('zh_CN')
for index in enumerate(range(20)):  # 设置生成数量
    street = fake.address()
    name = fake.name()
    job = fake.job()
    ph_num = fake.phone_number()
    print(name, street, job, ph_num)