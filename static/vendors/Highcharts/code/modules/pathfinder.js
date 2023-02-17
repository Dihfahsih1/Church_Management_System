/*
 Highcharts Gantt JS v7.2.0 (2019-09-03)

 Pathfinder

 (c) 2016-2019 ystein Moseng

 License: www.highcharts.com/license
*/
(function(h){"object"===typeof module&&module.exports?(h["default"]=h,module.exports=h):"function"===typeof define&&define.amd?define("highcharts/modules/pathfinder",["highcharts"],function(t){h(t);h.Highcharts=t;return h}):h("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(h){function t(e,g,w,h){e.hasOwnProperty(g)||(e[g]=h.apply(null,w))}h=h?h._modules:{};t(h,"parts-gantt/PathfinderAlgorithms.js",[h["parts/Globals.js"]],function(e){function g(c,a,k){k=k||0;var e=c.length-1;a-=1e-7;
for(var g,h;k<=e;)if(g=e+k>>1,h=a-c[g].xMin,0<h)k=g+1;else if(0>h)e=g-1;else return g;return 0<k?k-1:0}function w(c,a){for(var k=g(c,a.x+1)+1;k--;){var e;if(e=c[k].xMax>=a.x)e=c[k],e=a.x<=e.xMax&&a.x>=e.xMin&&a.y<=e.yMax&&a.y>=e.yMin;if(e)return k}return-1}function h(c){var a=[];if(c.length){a.push("M",c[0].start.x,c[0].start.y);for(var k=0;k<c.length;++k)a.push("L",c[k].end.x,c[k].end.y)}return a}function p(c,a){c.yMin=C(c.yMin,a.yMin);c.yMax=v(c.yMax,a.yMax);c.xMin=C(c.xMin,a.xMin);c.xMax=v(c.xMax,
a.xMax)}var v=Math.min,C=Math.max,A=Math.abs,t=e.pick;return{straight:function(c,a){return{path:["M",c.x,c.y,"L",a.x,a.y],obstacles:[{start:c,end:a}]}},simpleConnect:e.extend(function(c,a,k){function e(b,d,l,c,a){b={x:b.x,y:b.y};b[d]=l[c||d]+(a||0);return b}function g(b,d,l){var f=A(d[l]-b[l+"Min"])>A(d[l]-b[l+"Max"]);return e(d,l,b,l+(f?"Max":"Min"),f?1:-1)}var r=[],q=t(k.startDirectionX,A(a.x-c.x)>A(a.y-c.y))?"x":"y",p=k.chartObstacles,b=w(p,c);k=w(p,a);if(-1<k){var d=p[k];k=g(d,a,q);d={start:k,
end:a};var l=k}else l=a;-1<b&&(p=p[b],k=g(p,c,q),r.push({start:c,end:k}),k[q]>=c[q]===k[q]>=l[q]&&(q="y"===q?"x":"y",a=c[q]<a[q],r.push({start:k,end:e(k,q,p,q+(a?"Max":"Min"),a?1:-1)}),q="y"===q?"x":"y"));c=r.length?r[r.length-1].end:c;k=e(c,q,l);r.push({start:c,end:k});q=e(k,"y"===q?"x":"y",l);r.push({start:k,end:q});r.push(d);return{path:h(r),obstacles:r}},{requiresObstacles:!0}),fastAvoid:e.extend(function(c,a,e){function k(b,d,l){var f,y=b.x<d.x?1:-1;if(b.x<d.x){var e=b;var c=d}else e=d,c=b;if(b.y<
d.y){var z=b;var a=d}else z=d,a=b;for(f=0>y?v(g(m,c.x),m.length-1):0;m[f]&&(0<y&&m[f].xMin<=c.x||0>y&&m[f].xMax>=e.x);){if(m[f].xMin<=c.x&&m[f].xMax>=e.x&&m[f].yMin<=a.y&&m[f].yMax>=z.y)return l?{y:b.y,x:b.x<d.x?m[f].xMin-1:m[f].xMax+1,obstacle:m[f]}:{x:b.x,y:b.y<d.y?m[f].yMin-1:m[f].yMax+1,obstacle:m[f]};f+=y}return d}function u(b,d,l,f,y){var e=y.soft,c=y.hard,a=f?"x":"y",m={x:d.x,y:d.y},D={x:d.x,y:d.y};y=b[a+"Max"]>=e[a+"Max"];e=b[a+"Min"]<=e[a+"Min"];var z=b[a+"Max"]>=c[a+"Max"];c=b[a+"Min"]<=
c[a+"Min"];var F=A(b[a+"Min"]-d[a]),g=A(b[a+"Max"]-d[a]);l=10>A(F-g)?d[a]<l[a]:g<F;D[a]=b[a+"Min"];m[a]=b[a+"Max"];b=k(d,D,f)[a]!==D[a];d=k(d,m,f)[a]!==m[a];l=b?d?l:!0:d?!1:l;l=e?y?l:!0:y?!1:l;return c?z?l:!0:z?!1:l}function r(b,d,f){if(b.x===d.x&&b.y===d.y)return[];var a=f?"x":"y",c=e.obstacleOptions.margin;var g={soft:{xMin:y,xMax:D,yMin:H,yMax:F},hard:e.hardBounds};var n=w(m,b);if(-1<n){n=m[n];g=u(n,b,d,f,g);p(n,e.hardBounds);var z=f?{y:b.y,x:n[g?"xMax":"xMin"]+(g?1:-1)}:{x:b.x,y:n[g?"yMax":"yMin"]+
(g?1:-1)};var x=w(m,z);-1<x&&(x=m[x],p(x,e.hardBounds),z[a]=g?C(n[a+"Max"]-c+1,(x[a+"Min"]+n[a+"Max"])/2):v(n[a+"Min"]+c-1,(x[a+"Max"]+n[a+"Min"])/2),b.x===z.x&&b.y===z.y?(l&&(z[a]=g?C(n[a+"Max"],x[a+"Max"])+1:v(n[a+"Min"],x[a+"Min"])-1),l=!l):l=!1);b=[{start:b,end:z}]}else a=k(b,{x:f?d.x:b.x,y:f?b.y:d.y},f),b=[{start:b,end:{x:a.x,y:a.y}}],a[f?"x":"y"]!==d[f?"x":"y"]&&(g=u(a.obstacle,a,d,!f,g),p(a.obstacle,e.hardBounds),g={x:f?a.x:a.obstacle[g?"xMax":"xMin"]+(g?1:-1),y:f?a.obstacle[g?"yMax":"yMin"]+
(g?1:-1):a.y},f=!f,b=b.concat(r({x:a.x,y:a.y},g,f)));return b=b.concat(r(b[b.length-1].end,d,!f))}function q(b,d,a){var l=v(b.xMax-d.x,d.x-b.xMin)<v(b.yMax-d.y,d.y-b.yMin);a=u(b,d,a,l,{soft:e.hardBounds,hard:e.hardBounds});return l?{y:d.y,x:b[a?"xMax":"xMin"]+(a?1:-1)}:{x:d.x,y:b[a?"yMax":"yMin"]+(a?1:-1)}}var E=t(e.startDirectionX,A(a.x-c.x)>A(a.y-c.y)),b=E?"x":"y",d=[],l=!1,f=e.obstacleMetrics,y=v(c.x,a.x)-f.maxWidth-10,D=C(c.x,a.x)+f.maxWidth+10,H=v(c.y,a.y)-f.maxHeight-10,F=C(c.y,a.y)+f.maxHeight+
10,m=e.chartObstacles;var n=g(m,y);f=g(m,D);m=m.slice(n,f+1);if(-1<(f=w(m,a))){var x=q(m[f],a,c);d.push({end:a,start:x});a=x}for(;-1<(f=w(m,a));)n=0>a[b]-c[b],x={x:a.x,y:a.y},x[b]=m[f][n?b+"Max":b+"Min"]+(n?1:-1),d.push({end:a,start:x}),a=x;c=r(c,a,E);c=c.concat(d.reverse());return{path:h(c),obstacles:c}},{requiresObstacles:!0})}});t(h,"parts-gantt/ArrowSymbols.js",[h["parts/Globals.js"]],function(e){e.SVGRenderer.prototype.symbols.arrow=function(e,h,u,p){return["M",e,h+p/2,"L",e+u,h,"L",e,h+p/2,
"L",e+u,h+p]};e.SVGRenderer.prototype.symbols["arrow-half"]=function(g,h,u,p){return e.SVGRenderer.prototype.symbols.arrow(g,h,u/2,p)};e.SVGRenderer.prototype.symbols["triangle-left"]=function(e,h,u,p){return["M",e+u,h,"L",e,h+p/2,"L",e+u,h+p,"Z"]};e.SVGRenderer.prototype.symbols["arrow-filled"]=e.SVGRenderer.prototype.symbols["triangle-left"];e.SVGRenderer.prototype.symbols["triangle-left-half"]=function(g,h,u,p){return e.SVGRenderer.prototype.symbols["triangle-left"](g,h,u/2,p)};e.SVGRenderer.prototype.symbols["arrow-filled-half"]=
e.SVGRenderer.prototype.symbols["triangle-left-half"]});t(h,"parts-gantt/Pathfinder.js",[h["parts/Globals.js"],h["parts/Utilities.js"],h["parts-gantt/PathfinderAlgorithms.js"]],function(e,g,h){function u(b){var d=b.shapeArgs;return d?{xMin:d.x,xMax:d.x+d.width,yMin:d.y,yMax:d.y+d.height}:(d=b.graphic&&b.graphic.getBBox())?{xMin:b.plotX-d.width/2,xMax:b.plotX+d.width/2,yMin:b.plotY-d.height/2,yMax:b.plotY+d.height/2}:null}function p(b){for(var d=b.length,a=0,f,e,c=[],g=function(b,d,a){a=r(a,10);var f=
b.yMax+a>d.yMin-a&&b.yMin-a<d.yMax+a,l=b.xMax+a>d.xMin-a&&b.xMin-a<d.xMax+a,e=f?b.xMin>d.xMax?b.xMin-d.xMax:d.xMin-b.xMax:Infinity,c=l?b.yMin>d.yMax?b.yMin-d.yMax:d.yMin-b.yMax:Infinity;return l&&f?a?g(b,d,Math.floor(a/2)):Infinity:E(e,c)};a<d;++a)for(f=a+1;f<d;++f)e=g(b[a],b[f]),80>e&&c.push(e);c.push(80);return q(Math.floor(c.sort(function(b,d){return b-d})[Math.floor(c.length/10)]/2-1),1)}function v(b,d,a){this.init(b,d,a)}function t(b){this.init(b)}function A(b){if(b.options.pathfinder||b.series.reduce(function(b,
a){a.options&&B(!0,a.options.connectors=a.options.connectors||{},a.options.pathfinder);return b||a.options&&a.options.pathfinder},!1))B(!0,b.options.connectors=b.options.connectors||{},b.options.pathfinder),e.error('WARNING: Pathfinder options have been renamed. Use "chart.connectors" or "series.connectors" instead.')}var w=g.defined,c=g.objectEach,a=g.splat,k=e.deg2rad;g=e.extend;var G=e.addEvent,B=e.merge,r=e.pick,q=Math.max,E=Math.min;g(e.defaultOptions,{connectors:{type:"straight",lineWidth:1,
marker:{enabled:!1,align:"center",verticalAlign:"middle",inside:!1,lineWidth:1},startMarker:{symbol:"diamond"},endMarker:{symbol:"arrow-filled"}}});v.prototype={init:function(b,d,a){this.fromPoint=b;this.toPoint=d;this.options=a;this.chart=b.series.chart;this.pathfinder=this.chart.pathfinder},renderPath:function(b,d,a){var f=this.chart,l=f.styledMode,e=f.pathfinder,c=!f.options.chart.forExport&&!1!==a,g=this.graphics&&this.graphics.path;e.group||(e.group=f.renderer.g().addClass("highcharts-pathfinder-group").attr({zIndex:-1}).add(f.seriesGroup));
e.group.translate(f.plotLeft,f.plotTop);g&&g.renderer||(g=f.renderer.path().add(e.group),l||g.attr({opacity:0}));g.attr(d);b={d:b};l||(b.opacity=1);g[c?"animate":"attr"](b,a);this.graphics=this.graphics||{};this.graphics.path=g},addMarker:function(b,d,a){var f=this.fromPoint.series.chart,e=f.pathfinder;f=f.renderer;var l="start"===b?this.fromPoint:this.toPoint,c=l.getPathfinderAnchorPoint(d);if(d.enabled){a="start"===b?{x:a[4],y:a[5]}:{x:a[a.length-5],y:a[a.length-4]};a=l.getRadiansToVector(a,c);
c=l.getMarkerVector(a,d.radius,c);a=-a/k;if(d.width&&d.height){var g=d.width;var h=d.height}else g=h=2*d.radius;this.graphics=this.graphics||{};c={x:c.x-g/2,y:c.y-h/2,width:g,height:h,rotation:a,rotationOriginX:c.x,rotationOriginY:c.y};this.graphics[b]?this.graphics[b].animate(c):(this.graphics[b]=f.symbol(d.symbol).addClass("highcharts-point-connecting-path-"+b+"-marker").attr(c).add(e.group),f.styledMode||this.graphics[b].attr({fill:d.color||this.fromPoint.color,stroke:d.lineColor,"stroke-width":d.lineWidth,
opacity:0}).animate({opacity:1},l.series.options.animation))}},getPath:function(b){var d=this.pathfinder,a=this.chart,f=d.algorithms[b.type],c=d.chartObstacles;if("function"!==typeof f)e.error('"'+b.type+'" is not a Pathfinder algorithm.');else return f.requiresObstacles&&!c&&(c=d.chartObstacles=d.getChartObstacles(b),a.options.connectors.algorithmMargin=b.algorithmMargin,d.chartObstacleMetrics=d.getObstacleMetrics(c)),f(this.fromPoint.getPathfinderAnchorPoint(b.startMarker),this.toPoint.getPathfinderAnchorPoint(b.endMarker),
B({chartObstacles:c,lineObstacles:d.lineObstacles||[],obstacleMetrics:d.chartObstacleMetrics,hardBounds:{xMin:0,xMax:a.plotWidth,yMin:0,yMax:a.plotHeight},obstacleOptions:{margin:b.algorithmMargin},startDirectionX:d.getAlgorithmStartDirection(b.startMarker)},b))},render:function(){var b=this.fromPoint,d=b.series,a=d.chart,f=a.pathfinder,c=B(a.options.connectors,d.options.connectors,b.options.connectors,this.options),e={};a.styledMode||(e.stroke=c.lineColor||b.color,e["stroke-width"]=c.lineWidth,c.dashStyle&&
(e.dashstyle=c.dashStyle));e["class"]="highcharts-point-connecting-path highcharts-color-"+b.colorIndex;c=B(e,c);w(c.marker.radius)||(c.marker.radius=E(q(Math.ceil((c.algorithmMargin||8)/2)-1,1),5));b=this.getPath(c);a=b.path;b.obstacles&&(f.lineObstacles=f.lineObstacles||[],f.lineObstacles=f.lineObstacles.concat(b.obstacles));this.renderPath(a,e,d.options.animation);this.addMarker("start",B(c.marker,c.startMarker),a);this.addMarker("end",B(c.marker,c.endMarker),a)},destroy:function(){this.graphics&&
(c(this.graphics,function(b){b.destroy()}),delete this.graphics)}};t.prototype={algorithms:h,init:function(b){this.chart=b;this.connections=[];G(b,"redraw",function(){this.pathfinder.update()})},update:function(b){var d=this.chart,c=this,f=c.connections;c.connections=[];d.series.forEach(function(b){b.visible&&!b.options.isInternal&&b.points.forEach(function(b){var f,g=b.options&&b.options.connect&&a(b.options.connect);b.visible&&!1!==b.isInside&&g&&g.forEach(function(a){f=d.get("string"===typeof a?
a:a.to);f instanceof e.Point&&f.series.visible&&f.visible&&!1!==f.isInside&&c.connections.push(new v(b,f,"string"===typeof a?{}:a))})})});for(var g=0,h,k,p=f.length,m=c.connections.length;g<p;++g){k=!1;for(h=0;h<m;++h)if(f[g].fromPoint===c.connections[h].fromPoint&&f[g].toPoint===c.connections[h].toPoint){c.connections[h].graphics=f[g].graphics;k=!0;break}k||f[g].destroy()}delete this.chartObstacles;delete this.lineObstacles;c.renderConnections(b)},renderConnections:function(b){b?this.chart.series.forEach(function(b){var a=
function(){var a=b.chart.pathfinder;(a&&a.connections||[]).forEach(function(a){a.fromPoint&&a.fromPoint.series===b&&a.render()});b.pathfinderRemoveRenderEvent&&(b.pathfinderRemoveRenderEvent(),delete b.pathfinderRemoveRenderEvent)};!1===b.options.animation?a():b.pathfinderRemoveRenderEvent=G(b,"afterAnimate",a)}):this.connections.forEach(function(b){b.render()})},getChartObstacles:function(b){for(var a=[],c=this.chart.series,f=r(b.algorithmMargin,0),e,g=0,h=c.length;g<h;++g)if(c[g].visible&&!c[g].options.isInternal)for(var k=
0,m=c[g].points.length,n;k<m;++k)n=c[g].points[k],n.visible&&(n=u(n))&&a.push({xMin:n.xMin-f,xMax:n.xMax+f,yMin:n.yMin-f,yMax:n.yMax+f});a=a.sort(function(b,a){return b.xMin-a.xMin});w(b.algorithmMargin)||(e=b.algorithmMargin=p(a),a.forEach(function(b){b.xMin-=e;b.xMax+=e;b.yMin-=e;b.yMax+=e}));return a},getObstacleMetrics:function(b){for(var a=0,c=0,f,e,g=b.length;g--;)f=b[g].xMax-b[g].xMin,e=b[g].yMax-b[g].yMin,a<f&&(a=f),c<e&&(c=e);return{maxHeight:c,maxWidth:a}},getAlgorithmStartDirection:function(b){var a=
"top"!==b.verticalAlign&&"bottom"!==b.verticalAlign;return"left"!==b.align&&"right"!==b.align?a?void 0:!1:a?!0:void 0}};e.Connection=v;e.Pathfinder=t;g(e.Point.prototype,{getPathfinderAnchorPoint:function(b){var a=u(this);switch(b.align){case "right":var c="xMax";break;case "left":c="xMin"}switch(b.verticalAlign){case "top":var f="yMin";break;case "bottom":f="yMax"}return{x:c?a[c]:(a.xMin+a.xMax)/2,y:f?a[f]:(a.yMin+a.yMax)/2}},getRadiansToVector:function(b,a){w(a)||(a=u(this),a={x:(a.xMin+a.xMax)/
2,y:(a.yMin+a.yMax)/2});return Math.atan2(a.y-b.y,b.x-a.x)},getMarkerVector:function(b,a,c){var d=2*Math.PI,e=u(this),g=e.xMax-e.xMin,h=e.yMax-e.yMin,k=Math.atan2(h,g),l=!1;g/=2;var n=h/2,p=e.xMin+g;e=e.yMin+n;for(var q=p,r=e,t={},v=1,w=1;b<-Math.PI;)b+=d;for(;b>Math.PI;)b-=d;d=Math.tan(b);b>-k&&b<=k?(w=-1,l=!0):b>k&&b<=Math.PI-k?w=-1:b>Math.PI-k||b<=-(Math.PI-k)?(v=-1,l=!0):v=-1;l?(q+=v*g,r+=w*g*d):(q+=h/(2*d)*v,r+=w*n);c.x!==p&&(q=c.x);c.y!==e&&(r=c.y);t.x=q+a*Math.cos(b);t.y=r-a*Math.sin(b);return t}});
e.Chart.prototype.callbacks.push(function(a){!1!==a.options.connectors.enabled&&(A(a),this.pathfinder=new t(this),this.pathfinder.update(!0))})});t(h,"masters/modules/pathfinder.src.js",[],function(){})});
//# sourceMappingURL=pathfinder.js.map