// ===== ฟังก์ชัน Modal =====
    function showModal() {
      document.getElementById('success-modal').style.display = 'flex';
    }
    function closeModal() {
      document.getElementById('success-modal').style.display = 'none';
    }

    // ✅ ฟังก์ชันกลับไปหน้า index.html
    function goHome() {
      window.location.href = "index.html";
    }

    // ===== เมื่อกดบันทึกแบบฟอร์ม =====
const itemForms = document.querySelectorAll('.item-form');

itemForms.forEach(form => {
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    showModal();

    // หลัง 5 นาที ปิด modal แล้วไปหน้า index4.html
    setTimeout(() => {
      console.log("➡ ครบ 5 นาที กำลังเปลี่ยนหน้า index4.html");
      closeModal();
      window.location.href = "index4.html";
    }, 300000); // ⏱ 5 นาที = 300,000 มิลลิวินาที
  });
});
