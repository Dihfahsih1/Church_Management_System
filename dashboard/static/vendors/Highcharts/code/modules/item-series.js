/*
 Highcharts JS v7.2.0 (2019-09-03)

 Item series type for Highcharts

 (c) 2019 Torstein Honsi

 License: www.highcharts.com/license
*/
(function(a){"object"===typeof module&&module.exports?(a["default"]=a,module.exports=a):"function"===typeof define&&define.amd?define("highcharts/modules/item-series",["highcharts"],function(b){a(b);a.Highcharts=b;return a}):a("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(a){function b(a,d,b,m){a.hasOwnProperty(d)||(a[d]=m.apply(null,b))}a=a?a._modules:{};b(a,"modules/item-series.src.js",[a["parts/Globals.js"],a["parts/Utilities.js"]],function(a,d){var b=d.defined,m=d.isNumber,E=d.objectEach,
F=a.extend,D=a.fireEvent;d=a.merge;var t=a.seriesTypes.pie.prototype.pointClass.prototype;a.seriesType("item","pie",{endAngle:void 0,innerSize:"40%",itemPadding:.1,layout:"vertical",marker:d(a.defaultOptions.plotOptions.line.marker,{radius:null}),rows:void 0,showInLegend:!0,startAngle:void 0},{translate:function(){this.slots||(this.slots=[]);m(this.options.startAngle)&&m(this.options.endAngle)?(a.seriesTypes.pie.prototype.translate.call(this),this.slots=this.getSlots()):(this.generatePoints(),D(this,
"afterTranslate"))},getSlots:function(){function c(a){0<C&&(a.row.colCount--,C--)}for(var a=this.center,q=a[2],b=a[3],d,n=this.slots,u,z,v,w,x,e,k,y,g=0,p,A=this.endAngleRad-this.startAngleRad,r=Number.MAX_VALUE,B,l,h,f=this.options.rows,m=(q-b)/q;r>this.total;)for(B=r,r=n.length=0,l=h,h=[],g++,p=q/g/2,f?(b=(p-f)/p*q,0<=b?p=f:(b=0,m=1)):p=Math.floor(p*m),d=p;0<d;d--)v=(b+d/p*(q-b-g))/2,w=A*v,x=Math.ceil(w/g),h.push({rowRadius:v,rowLength:w,colCount:x}),r+=x+1;if(l){for(var C=B-this.total;0<C;)l.map(function(a){return{angle:a.colCount/
a.rowLength,row:a}}).sort(function(a,c){return c.angle-a.angle}).slice(0,Math.min(C,Math.ceil(l.length/2))).forEach(c);l.forEach(function(c){var b=c.rowRadius;e=(c=c.colCount)?A/c:0;for(y=0;y<=c;y+=1)k=this.startAngleRad+y*e,u=a[0]+Math.cos(k)*b,z=a[1]+Math.sin(k)*b,n.push({x:u,y:z,angle:k})},this);n.sort(function(a,c){return a.angle-c.angle});this.itemSize=g;return n}},getRows:function(){var a=this.options.rows;if(!a){var b=this.chart.plotWidth/this.chart.plotHeight;a=Math.sqrt(this.total);if(1<
b)for(a=Math.ceil(a);0<a;){var d=this.total/a;if(d/a>b)break;a--}else for(a=Math.floor(a);a<this.total;){d=this.total/a;if(d/a<b)break;a++}}return a},drawPoints:function(){var c=this,d=this.options,q=c.chart.renderer,m=d.marker,t=this.borderWidth%2?.5:1,n=0,u=this.getRows(),z=Math.ceil(this.total/u),v=this.chart.plotWidth/z,w=this.chart.plotHeight/u,x=this.itemSize||Math.min(v,w);this.points.forEach(function(e){var k,y,g=e.marker||{},p=g.symbol||m.symbol;g=a.pick(g.radius,m.radius);var A=b(g)?2*g:
x,r=A*d.itemPadding,B;e.graphics=k=e.graphics||{};c.chart.styledMode||(y=c.pointAttribs(e,e.selected&&"select"));if(!e.isNull&&e.visible){e.graphic||(e.graphic=q.g("point").add(c.group));for(var l=0;l<e.y;l++){if(c.center&&c.slots){var h=c.slots.shift();var f=h.x-x/2;h=h.y-x/2}else"horizontal"===d.layout?(f=n%z*v,h=w*Math.floor(n/z)):(f=v*Math.floor(n/u),h=n%u*w);f+=r;h+=r;var D=B=Math.round(A-2*r);c.options.crisp&&(f=Math.round(f)-t,h=Math.round(h)+t);f={x:f,y:h,width:B,height:D};void 0!==g&&(f.r=
g);k[l]?k[l].animate(f):k[l]=q.symbol(p,null,null,null,null,{backgroundSize:"within"}).attr(F(f,y)).add(e.graphic);k[l].isActive=!0;n++}}E(k,function(a,c){a.isActive?a.isActive=!1:(a.destroy(),delete k[c])})})},drawDataLabels:function(){this.center&&this.slots?a.seriesTypes.pie.prototype.drawDataLabels.call(this):this.points.forEach(function(a){a.destroyElements({dataLabel:1})})},animate:function(a){a?this.group.attr({opacity:0}):(this.group.animate({opacity:1},this.options.animation),this.animate=
null)}},{connectorShapes:t.connectorShapes,getConnectorPath:t.getConnectorPath,setVisible:t.setVisible,getTranslate:t.getTranslate});""});b(a,"masters/modules/item-series.src.js",[],function(){})});
//# sourceMappingURL=item-series.js.map