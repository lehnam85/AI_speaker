// alert('Hello Wold!');
// alert(3 + 1 +1);
// ['hello', 'world'].forEach(alert)

// alert('에러가 발생!');
// [1, 2].forEach(alert)
/*
    이안에는 모두 주석처리
*/ 

// "use strict";

// alert('some code!');

//변수 사용
// let message;

// message = 'Hello';
// alert(message)

/*
let user = 'John', age = 24, message = 'Hello!';
alert(user)
alert(age)
alert(message)
*/

// const는 변하지 않는 변수
// const COLOR_RED = '#F00';

// let color = COLOR_RED;
// alert(color);
// const pageLoadTime 

var scene = new THREE.Scene();
document.addEventListener( 'mousemove', onMouseMove, false );
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 2000 );
var mouseX;
var mouseY;

var myCanvasElement = document.getElementById("myCanvas")
var renderer = new THREE.WebGLRenderer({ canvas: myCanvasElement });
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

window.addEventListener("resize", function() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize( window.innerWidth, window.innerHeight );
});

var distance = Math.min(200, window.innerWidth / 4);
var geometry = new THREE.Geometry();

// 원형의 점 개수
for (var i = 0; i < 1200; i++) {

  var vertex = new THREE.Vector3();

  // var theta = THREE.Math.randFloatSpread(360);
  
  var theta = Math.acos(THREE.Math.randFloatSpread(2)); 
  var phi = THREE.Math.randFloatSpread(90); 

  vertex.x = distance * Math.sin(theta) * Math.cos(phi);
  vertex.y = distance * Math.sin(theta) * Math.sin(phi);
  vertex.z = distance * Math.cos(theta);

  geometry.vertices.push(vertex);
}
var particles = new THREE.Points(geometry, new THREE.PointsMaterial({color: 0xEEEEEE, size: 5}));
particles.boundingSphere = 50;


var renderingParent = new THREE.Group();
renderingParent.add(particles);

var resizeContainer = new THREE.Group();
resizeContainer.add(renderingParent);
scene.add(resizeContainer);

//카메라 위치
camera.position.z = 1000;

var animate = function () {
  requestAnimationFrame( animate );
  renderer.render( scene, camera );
};
var myTween;
function onMouseMove(event) {
  if(myTween)
    myTween.kill();
  
  mouseX = ( event.clientX / window.innerWidth ) * 2 - 1;
  mouseY = - ( event.clientY / window.innerHeight ) * 2 + 1;
  myTween = gsap.to(particles.rotation, {duration: 0.1, x: mouseY*-1, y: mouseX});
  //particles.rotation.x = mouseY*-1;
  //particles.rotation.y = mouseX;
}
animate();

// Scaling animation
// duration는 원의 숨쉬기 운동 속도
var animProps = {scale: 1, xRot: 0, yRot: 0};
var speed = 1
gsap.to(animProps, {duration: speed, scale: 1.5, repeat: -1, yoyo: true, ease: "sine", onUpdate: function() {
  renderingParent.scale.set(animProps.scale,animProps.scale,animProps.scale);
}});

gsap.to(animProps, {duration: 120, xRot: Math.PI * 2, yRot: Math.PI * 4, repeat: -1, yoyo: true, ease: "none", onUpdate: function() {
  renderingParent.rotation.set(animProps.xRot,animProps.yRot,0);
}});

//0xff44ff
//0x13acaf