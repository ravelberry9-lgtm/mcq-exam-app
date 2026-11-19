/* G2 infographic viewer: tap an infographic to open it full screen, then zoom (buttons, double-tap or pinch) and pan.
   Links keep their href, so without JS (or with a modifier key) the image still opens on its own. */
(function(){
  var ZS=[1,1.5,2,3],ov,sc,img,cap,cnt,zi=0,list=[],idx=0,pushed=false;
  function build(){
    ov=document.createElement('div');ov.className='g2v';ov.setAttribute('role','dialog');ov.setAttribute('aria-modal','true');ov.setAttribute('aria-label','Infographic viewer');ov.hidden=true;
    ov.innerHTML='<div class="g2v-bar"><span class="g2v-cap"></span><span class="g2v-cnt"></span>'+
      '<button type="button" data-a="out" aria-label="Zoom out">−</button><button type="button" data-a="in" aria-label="Zoom in">+</button>'+
      '<a class="g2v-open" target="_blank" rel="noopener" aria-label="Open original image">↗</a><button type="button" data-a="close" aria-label="Close / మూసివేయి">✕</button></div>'+
      '<div class="g2v-sc"><img alt=""></div><button type="button" class="g2v-nav g2v-prev" data-a="prev" aria-label="Previous">‹</button><button type="button" class="g2v-nav g2v-next" data-a="next" aria-label="Next">›</button>'+
      '<p class="g2v-hint">రెండుసార్లు తాకి / చిటికెతో జూమ్ · Double-tap or pinch to zoom</p>';
    document.body.appendChild(ov);sc=ov.querySelector('.g2v-sc');img=sc.querySelector('img');cap=ov.querySelector('.g2v-cap');cnt=ov.querySelector('.g2v-cnt');
    ov.addEventListener('click',function(e){var b=e.target.closest('[data-a]');if(!b)return;var a=b.dataset.a;
      if(a=='close')close();else if(a=='in')zoom(zi+1);else if(a=='out')zoom(zi-1);else if(a=='prev')go(-1);else if(a=='next')go(1);});
    var lastTap=0;sc.addEventListener('click',function(e){var t=Date.now();if(t-lastTap<320){zoom(zi?0:2,e);lastTap=0}else lastTap=t;});
    sc.addEventListener('dblclick',function(e){e.preventDefault()});
    var sx=null,sy=0;sc.addEventListener('touchstart',function(e){sx=e.touches.length==1&&zi==0?e.touches[0].clientX:null;sy=e.touches[0].clientY},{passive:true});
    sc.addEventListener('touchend',function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx,dy=e.changedTouches[0].clientY-sy;sx=null;
      if(Math.abs(dx)>70&&Math.abs(dx)>2*Math.abs(dy)&&list.length>1)go(dx<0?1:-1)});
    document.addEventListener('keydown',function(e){if(ov.hidden)return;if(e.key=='Escape')close();else if(e.key=='ArrowRight')go(1);else if(e.key=='ArrowLeft')go(-1);else if(e.key=='+'||e.key=='=')zoom(zi+1);else if(e.key=='-')zoom(zi-1)});
    window.addEventListener('popstate',function(){if(!ov.hidden){pushed=false;close()}});
  }
  function zoom(n,e){n=Math.max(0,Math.min(ZS.length-1,n));var old=ZS[zi],r=sc.getBoundingClientRect();
    var cx=e?e.clientX-r.left:sc.clientWidth/2,cy=e?e.clientY-r.top:sc.clientHeight/2,px=(sc.scrollLeft+cx)/old,py=(sc.scrollTop+cy)/old;
    zi=n;img.style.width=(ZS[zi]*100)+'%';ov.classList.toggle('zoomed',zi>0);sc.scrollLeft=px*ZS[zi]-cx;sc.scrollTop=py*ZS[zi]-cy;}
  function show(){var a=list[idx];img.src=a.href;img.alt=a.dataset.title||'';cap.textContent=a.dataset.title||'';
    ov.querySelector('.g2v-open').href=a.href;cnt.textContent=list.length>1?(idx+1)+' / '+list.length:'';
    ov.classList.toggle('single',list.length<2);zi=0;img.style.width='100%';ov.classList.remove('zoomed');sc.scrollTop=0;sc.scrollLeft=0;}
  function go(d){if(list.length<2)return;idx=(idx+d+list.length)%list.length;show()}
  function open(a){if(!ov)build();var g=a.closest('[data-zoom-group]');list=g?[].slice.call(g.querySelectorAll('a[data-zoom]')):[a];idx=Math.max(0,list.indexOf(a));
    show();ov.hidden=false;document.documentElement.classList.add('g2v-on');ov.querySelector('[data-a=close]').focus();
    try{history.pushState({g2v:1},'');pushed=true}catch(_){}}
  function close(){if(!ov||ov.hidden)return;ov.hidden=true;document.documentElement.classList.remove('g2v-on');img.removeAttribute('src');
    var a=list[idx];if(a)a.focus({preventScroll:true});if(pushed){pushed=false;history.back()}}
  document.addEventListener('click',function(e){var a=e.target.closest('a[data-zoom]');if(!a||e.metaKey||e.ctrlKey||e.shiftKey||e.button)return;e.preventDefault();open(a)});
  // previews cut at a max height get a fade so it is clear there is more; the answer card takes focus after answering
  function mark(im){var a=im.closest('a.g2-zoom');if(a&&im.naturalWidth&&im.getBoundingClientRect().height>a.clientHeight+4)a.classList.add('tall')}
  [].forEach.call(document.querySelectorAll('a.g2-zoom img'),function(im){if(im.complete)mark(im);else im.addEventListener('load',function(){mark(im)})});
  var ar=document.getElementById('answer-result');if(ar&&location.hash=='#answer-result')try{ar.focus({preventScroll:true})}catch(_){}
})();
