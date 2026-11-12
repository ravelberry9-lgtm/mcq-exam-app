/* Focus (reading) mode for practice pages: hides app bars and side extras; remembered per device. */
(function(){var K='polityFocus',h=document.documentElement;
function get(){try{return localStorage.getItem(K)==='1'}catch(e){return false}}
function set(v){try{localStorage.setItem(K,v?'1':'0')}catch(e){}}
var b=document.createElement('button');b.type='button';b.className='fm-btn';
function paint(on){h.classList.toggle('fm-on',on);b.setAttribute('aria-pressed',on?'true':'false');b.innerHTML=on?'<span aria-hidden="true">⤡</span> Exit focus':'<span aria-hidden="true">⤢</span> Focus';b.title=on?'Show menus again':'Hide menus to read without distraction';}
b.addEventListener('click',function(){var on=!h.classList.contains('fm-on');set(on);paint(on);});
paint(get());document.body.appendChild(b);
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&h.classList.contains('fm-on')){set(false);paint(false);}});
})();
