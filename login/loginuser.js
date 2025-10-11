// แสดง/ซ่อนรหัสผ่าน
function togglePassword() {
  const passwordField = document.getElementById("password");
  passwordField.type = passwordField.type === "password" ? "text" : "password";
}

// กลับไปหน้าหลัก (ทดแทนด้วย redirect จริงๆ ได้)
function goHome() {
  alert("กลับไปหน้าหลัก");
}

// จัดการฟอร์ม login
document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  alert("อีเมล: " + email + "\nรหัสผ่าน: " + password);
});
