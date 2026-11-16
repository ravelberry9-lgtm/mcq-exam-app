// Polity practice keyboard: 1-4 choose, Enter check, N / ArrowRight next, P / ArrowLeft previous.
(function(){
  document.addEventListener('keydown',function(e){
    if(e.defaultPrevented||e.altKey||e.ctrlKey||e.metaKey)return;
    var t=e.target;if(t&&(t.isContentEditable||/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)&&t.type!=='radio'))return;
    var k=e.key;
    if(/^[1-4]$/.test(k)){var r=document.querySelector('.geo-option input[value="'+k+'"]');if(r){r.checked=true;r.focus();e.preventDefault();}return;}
    if(k==='Enter'&&t&&t.type==='radio'){var b=document.querySelector('.geo-submit');if(b){b.click();e.preventDefault();}return;}
    var nav=document.querySelector('.geo-question-nav');if(!nav)return;
    if(k==='n'||k==='N'||k==='ArrowRight'){var n=nav.querySelector('a[rel=next]');if(n){location.href=n.href;e.preventDefault();}}
    else if(k==='p'||k==='P'||k==='ArrowLeft'){var p=nav.querySelector('a[rel=prev]');if(p){location.href=p.href;e.preventDefault();}}
  });
})();
