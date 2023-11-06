import pyDes
import uuid

# 生成机器码
def generate_machine_code():

    # 获取CPU序列号
    cpu_serial = str(uuid.getnode())

    # 获取硬盘序列号
    disk_serial = ""

    # 获取网卡地址

    mac_address = ""

    # 组合硬件信息

    hardware_info = cpu_serial + disk_serial + mac_address

    # 组合产品信息和用户信息

    product_info = "product_name:1.0"

    user_info = "user_name:company_name"

    # 组合明文

    plain_text = hardware_info + product_info + user_info

    # 加密明文

    des_key = pyDes.des(b"01234567", pyDes.CBC, b"12345678", pad=None, padmode=pyDes.PAD_PKCS5)

    encrypted_text = des_key.encrypt(plain_text)

    # 生成机器码

    machine_code = encrypted_text.hex()

    return machine_code


# 验证注册码
def verify_registration_code(registration_code, machine_code):

    # 获取CPU序列号

    cpu_serial = str(uuid.getnode())

    # 获取硬盘序列号

    disk_serial = ""

    # 获取网卡地址

    mac_address = ""

    # 组合硬件信息

    hardware_info = cpu_serial + disk_serial + mac_address

    # 解密注册码

    des_key = pyDes.des(b"01234567", pyDes.CBC, b"12345678", pad=None, padmode=pyDes.PAD_PKCS5)

    decrypted_text = des_key.decrypt(bytes.fromhex(registration_code))

    # 判断注册码是否有效

    if hardware_info + decrypted_text.decode() == machine_code:

        return True

    else:

        return False


if __name__=="__main__":
    generate_machine_code()