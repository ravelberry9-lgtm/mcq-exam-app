(function(){
  var root=document.querySelector('.rv');if(!root)return;
  var base=root.dataset.part,kind=root.dataset.kind,lang=root.dataset.lang,showAll=false;
  var loaded={},pending={};
  function setOpen(btn,open){btn.setAttribute('aria-expanded',open?'true':'false');btn.querySelector('.rv-hid').hidden=open;btn.querySelector('.rv-shown').hidden=!open;}
  function tidy(sec){
    sec.querySelectorAll('.rv-opts').forEach(function(ol){var long=[].some.call(ol.children,function(li){return li.textContent.length>42});if(long)ol.style.gridTemplateColumns='minmax(0,1fr)';});
    if(showAll)sec.querySelectorAll('.rv-ab').forEach(function(b){setOpen(b,true)});
  }
  function load(sec){
    var ch=sec.dataset.ch;if(loaded[ch])return Promise.resolve();if(pending[ch])return pending[ch];
    var u=base+'?ch='+encodeURIComponent(ch)+'&kind='+kind+'&qlang='+lang;
    pending[ch]=fetch(u,{credentials:'same-origin'}).then(function(r){if(!r.ok)throw 0;return r.text()}).then(function(h){
      var body=sec.querySelector('.rv-body');body.innerHTML=h;body.style.minHeight='';loaded[ch]=true;tidy(sec);
    }).catch(function(){pending[ch]=null;sec.querySelector('.rv-load').textContent='Could not load. Scroll again to retry.';});
    return pending[ch];
  }
  var secs=[].slice.call(document.querySelectorAll('.rv-ch'));
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)load(e.target)})},{rootMargin:'1200px 0px'});
    secs.forEach(function(s){io.observe(s)});
  }else secs.forEach(load);
  function goTo(chKey,hash){
    var sec=document.getElementById(chKey);if(!sec)return;
    load(sec).then(function(){var t=hash&&document.getElementById(hash);(t||sec).scrollIntoView({block:t?'center':'start'});if(t){var b=t.querySelector('.rv-ab');if(b)setOpen(b,true);t.classList.add('rv-back');}});
  }
  // returning from a full explanation: open that chapter and that question
  var h=location.hash.slice(1),open=root.dataset.open;
  if(open)goTo(open,h&&h.indexOf('q-')===0?h:'');else if(h&&document.getElementById(h))goTo(h,'');
  document.getElementById('rv-jump').addEventListener('change',function(){if(this.value){history.replaceState(null,'','#'+this.value);goTo(this.value,'')}});
  root.addEventListener('click',function(e){var b=e.target.closest('.rv-ab');if(b)setOpen(b,b.getAttribute('aria-expanded')!=='true');});
  var sa=document.getElementById('rv-showall');
  sa.addEventListener('click',function(){showAll=!showAll;sa.classList.toggle('on',showAll);sa.textContent=showAll?'Hide all answers':'Show all answers';
    document.querySelectorAll('.rv-ab').forEach(function(b){setOpen(b,showAll)});});
  var so=document.getElementById('rv-showopts');
  so.addEventListener('click',function(){var on=root.classList.toggle('all-opts');so.classList.toggle('on',on);so.textContent=on?'Hide options again':'Show options for all';});
})();
