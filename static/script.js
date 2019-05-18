/* モーダル非表示(ここから) */
$('#delModal').click(function () {
  $(this).parents('.alert').hide();
  return false;
});
/* モーダル非表示(ここまで) */

/* フッター固定(ここから) */
let page_size = {
  w : $(window).width()
 ,h : $(window).height()
};
let browser_size = {
  w: document.body.clientWidth
 ,h: document.body.clientHeight
};
if(page_size.h > browser_size.h) {
  $('footer').css('position', 'fixed');
  $('footer').css('bottom', '0px');
  $('footer').css('width', '100%'); /* 必要なら */
}
/* フッター固定(ここまで) */
