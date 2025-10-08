// ฟอร์มเข้าสู่ระบบ
const loginForm = document.querySelector('.login-form');
if (loginForm) {
  loginForm.addEventListener('submit', function(e) {
    e.preventDefault();
    showModal('เข้าสู่ระบบสำเร็จ !');
    setTimeout(() => {
      closeModal();
      showPage('profile');
    }, 2000);
  });
}

function togglePassword(inputId, el) {
  const input = document.getElementById(inputId);
  if (input.type === 'password') {
    input.type = 'text';
    el.textContent = '🙈';    // เปลี่ยนเป็น “ตาหลับ”
  } else {
    input.type = 'password';
    el.textContent = '👁‍🗨'; // เปลี่ยนกลับเป็น “ตาเปิด”
  }
}