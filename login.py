def login(max_attempts=3):
    print("=== ระบบเข้าสู่ระบบ (พยายามได้สูงสุด 3 ครั้ง) ===")
    for attempt in range(max_attempts):
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            print("✅ เข้าสู่ระบบสำเร็จ!")
            return True
        else:
            print(f"❌ ไม่ถูกต้อง (ครั้งที่ {attempt + 1} จาก {max_attempts})")
    
    print("⛔ คุณพยายามเข้าสู่ระบบเกินจำนวนครั้งที่กำหนด")
    return False

# เรียกใช้งาน
login()
