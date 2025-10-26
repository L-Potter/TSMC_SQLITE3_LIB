def xor_encrypt_file(input_path, output_path, key):
    key_bytes = key.encode('utf-8')
    with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        data = f_in.read()
        encrypted = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])
        f_out.write(encrypted)

def xor_decrypt_file(input_path, output_path, key):
    # XOR 加密和解密一樣
    xor_encrypt_file(input_path, output_path, key)

# 使用範例
key = "mysecret"
#xor_encrypt_file("node_sqlite3.node", "encrypted", key) # node.lib
xor_decrypt_file("encrypted", "node_sqlite3.node", key)