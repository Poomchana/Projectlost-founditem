
// ===== ฟังก์ชัน Modal =====
function showModal(title = 'สมัครสมาชิกสำเร็จ !') {
  const modal = document.getElementById('success-modal');
  const modalTitle = document.getElementById('modal-title');
  if (modal && modalTitle) {
    modalTitle.textContent = title;
    modal.style.display = 'block';
  }
}

function closeModal() {
  const modal = document.getElementById('success-modal');
  if (modal) modal.style.display = 'none';
}

// ปิด Modal เมื่อคลิกนอกกล่อง
window.onclick = function (event) {
  const modal = document.getElementById('success-modal');
  if (event.target === modal) {
    closeModal();
  }
};

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


// ===== สมัครสมาชิก =====
// รองรับทั้ง .register-form เดี่ยว ๆ หรือมี <form> ซ้อน
const registerForms = document.querySelectorAll('.register-form form, .register-form');
registerForms.forEach(form => {
  if (form.tagName === 'FORM' || form.querySelector('form')) {
    const actualForm = form.tagName === 'FORM' ? form : form.querySelector('form');
    if (actualForm) {
      actualForm.addEventListener('submit', function (e) {
        e.preventDefault();
        // แสดง Modal สมัครสมาชิกสำเร็จ
        showModal('สมัครสมาชิกสำเร็จ !');

        // ปิด Modal และสลับหน้าไป login ภายใน 2 วินาที
        setTimeout(() => {
          closeModal();
          // หากมีฟังก์ชัน showPage ให้ไปหน้า login
          if (typeof showPage === 'function') {
            showPage('login');
          }
        }, 2000);
      });
    }
  }
});
