document.addEventListener('DOMContentLoaded', () => {
  // ปุ่มติดต่อ
  document.querySelectorAll('.contact-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      alert('ติดต่อเจ้าของสิ่งของ\nFacebook: ***\nLine: ***\nเบอร์โทร: ***');
    });
  });

  // hover การ์ด
  document.querySelectorAll('.item-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.transform = 'translateY(-5px)';
      card.style.boxShadow = '0px 8px 16px rgba(0,0,0,0.3)';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'translateY(0)';
      card.style.boxShadow = '0px 4px 4px rgba(0,0,0,0.25)';
    });
  });
});


