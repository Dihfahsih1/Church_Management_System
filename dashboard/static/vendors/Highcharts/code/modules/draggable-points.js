/*
 Highcharts JS v7.2.0 (2019-09-03)

 (c) 2009-2019 Torstein Honsi

 License: www.highcharts.com/license
*/
(function(e){"object"===typeof module&&module.exports?(e["default"]=e,module.exports=e):"function"===typeof define&&define.amd?define("highcharts/modules/draggable-points",["highcharts"],function(r){e(r);e.Highcharts=r;return e}):e("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(e){function r(k,e,r,A){k.hasOwnProperty(e)||(k[e]=A.apply(null,r))}e=e?e._modules:{};r(e,"modules/draggable-points.src.js",[e["parts/Globals.js"],e["parts/Utilities.js"]],function(k,e){function r(a){return{left:"right",
right:"left",top:"bottom",bottom:"top"}[a]}function A(a){var b=["draggableX","draggableY"],c;n(a.dragDropProps,function(a){a.optionName&&b.push(a.optionName)});for(c=b.length;c--;)if(a.options.dragDrop[b[c]])return!0}function K(a){var b=a.series?a.series.length:0;if(a.hasCartesianSeries&&!a.polar)for(;b--;)if(a.series[b].options.dragDrop&&A(a.series[b]))return!0}function L(a){var b=a.series,c=b.options.dragDrop||{};a=a.options&&a.options.dragDrop;var d,f;n(b.dragDropProps,function(a){"x"===a.axis&&
a.move?d=!0:"y"===a.axis&&a.move&&(f=!0)});return(c.draggableX&&d||c.draggableY&&f)&&!(a&&!1===a.draggableX&&!1===a.draggableY)&&b.yAxis&&b.xAxis}function w(a,b){return void 0===a.chartX||void 0===a.chartY?b.pointer.normalize(a):a}function x(a,b,c,d){var f=b.map(function(b){return p(a,b,c,d)});return function(){f.forEach(function(a){a()})}}function M(a,b,c){var d=b.dragDropData.origin;b=d.chartX;d=d.chartY;var f=a.chartX;a=a.chartY;return Math.sqrt((f-b)*(f-b)+(a-d)*(a-d))>c}function N(a,b,c){var d=
{chartX:a.chartX,chartY:a.chartY,guideBox:c&&{x:c.attr("x"),y:c.attr("y"),width:c.attr("width"),height:c.attr("height")},points:{}};b.forEach(function(b){var c={};n(b.series.dragDropProps,function(d,f){d=b.series[d.axis+"Axis"];c[f]=b[f];c[f+"Offset"]=d.toPixels(b[f])-(d.horiz?a.chartX:a.chartY)});c.point=b;d.points[b.id]=c});return d}function O(a){var b=a.series,c=[],d=b.options.dragDrop.groupBy;b.isSeriesBoosting?b.options.data.forEach(function(a,d){c.push((new b.pointClass).init(b,a));c[c.length-
1].index=d}):c=b.points;return a.options[d]?c.filter(function(b){return b.options[d]===a.options[d]}):[a]}function D(a,b){var c=O(b),d=b.series,f=d.chart,m;v(d.options.dragDrop&&d.options.dragDrop.liveRedraw,!0)||(f.dragGuideBox=m=d.getGuideBox(c),f.setGuideBoxState("default",d.options.dragDrop.guideBox).add(d.group));f.dragDropData={origin:N(a,c,m),point:b,groupedPoints:c,isDragging:!0}}function P(a,b){var c=a.point,d=q(c.series.options.dragDrop,c.options.dragDrop),f={},m=a.updateProp,C={};n(c.series.dragDropProps,
function(a,b){if(!m||m===b&&a.resize&&(!a.optionName||!1!==d[a.optionName]))if(m||a.move&&("x"===a.axis&&d.draggableX||"y"===a.axis&&d.draggableY))f[b]=a});(m?[c]:a.groupedPoints).forEach(function(c){C[c.id]={point:c,newValues:c.getDropValues(a.origin,b,f)}});return C}function E(a,b){var c=a.dragDropData.newPoints;b=!1===b?!1:q({duration:400},a.options.chart.animation);a.isDragDropAnimating=!0;n(c,function(a){a.point.update(a.newValues,!1)});a.redraw(b);setTimeout(function(){delete a.isDragDropAnimating;
a.hoverPoint&&!a.dragHandles&&a.hoverPoint.showDragHandles()},b.duration)}function F(a){var b=a.series&&a.series.chart,c=b&&b.dragDropData;!b||!b.dragHandles||c&&(c.isDragging&&c.draggedPastSensitivity||c.isHoveringHandle===a.id)||b.hideDragHandles()}function G(a){var b=0,c;for(c in a)Object.hasOwnProperty.call(a,c)&&b++;return b}function H(a){for(var b in a)if(Object.hasOwnProperty.call(a,b))return a[b]}function Q(a,b){if(!b.zoomOrPanKeyPressed(a)){var c=b.dragDropData;var d=0;if(c&&c.isDragging){var f=
c.point;d=f.series.options.dragDrop;a.preventDefault();c.draggedPastSensitivity||(c.draggedPastSensitivity=M(a,b,v(f.options.dragDrop&&f.options.dragDrop.dragSensitivity,d&&d.dragSensitivity,2)));c.draggedPastSensitivity&&(c.newPoints=P(c,a),b=c.newPoints,d=G(b),b=1===d?H(b):null,f.firePointEvent("drag",{origin:c.origin,newPoints:c.newPoints,newPoint:b&&b.newValues,newPointId:b&&b.point.id,numNewPoints:d,chartX:a.chartX,chartY:a.chartY},function(){var b=f.series,c=b.chart,d=c.dragDropData,e=q(b.options.dragDrop,
f.options.dragDrop),h=e.draggableX,l=e.draggableY;b=d.origin;var k=a.chartX-b.chartX,y=a.chartY-b.chartY,t=k;d=d.updateProp;c.inverted&&(k=-y,y=-t);if(v(e.liveRedraw,!0))E(c,!1),f.showDragHandles();else if(d){h=k;c=y;t=f.series;l=t.chart;d=l.dragDropData;e=t.dragDropProps[d.updateProp];var g=d.newPoints[f.id].newValues;var n="function"===typeof e.resizeSide?e.resizeSide(g,f):e.resizeSide;e.beforeResize&&e.beforeResize(l.dragGuideBox,g,f);l=l.dragGuideBox;t="x"===e.axis&&t.xAxis.reversed||"y"===e.axis&&
t.yAxis.reversed?r(n):n;h="x"===e.axis?h-(d.origin.prevdX||0):0;c="y"===e.axis?c-(d.origin.prevdY||0):0;switch(t){case "left":var p={x:l.attr("x")+h,width:Math.max(1,l.attr("width")-h)};break;case "right":p={width:Math.max(1,l.attr("width")+h)};break;case "top":p={y:l.attr("y")+c,height:Math.max(1,l.attr("height")-c)};break;case "bottom":p={height:Math.max(1,l.attr("height")+c)}}l.attr(p)}else c.dragGuideBox.translate(h?k:0,l?y:0);b.prevdX=k;b.prevdY=y}))}}}function B(a,b){var c=b.dragDropData;if(c&&
c.isDragging&&c.draggedPastSensitivity){var d=c.point,f=c.newPoints,m=G(f),e=1===m?H(f):null;b.dragHandles&&b.hideDragHandles();a.preventDefault();b.cancelClick=!0;d.firePointEvent("drop",{origin:c.origin,chartX:a.chartX,chartY:a.chartY,newPoints:f,numNewPoints:m,newPoint:e&&e.newValues,newPointId:e&&e.point.id},function(){E(b)})}delete b.dragDropData;b.dragGuideBox&&(b.dragGuideBox.destroy(),delete b.dragGuideBox)}function R(a){var b=a.container,c=k.doc;K(a)&&(x(b,["mousedown","touchstart"],function(b){b=
w(b,a);var c=a.hoverPoint,d=k.merge(c&&c.series.options.dragDrop,c&&c.options.dragDrop),e=d.draggableX||!1;d=d.draggableY||!1;a.cancelClick=!1;!e&&!d||a.zoomOrPanKeyPressed(b)||(a.dragDropData&&a.dragDropData.isDragging?B(b,a):c&&L(c)&&(a.mouseIsDown=!1,D(b,c),c.firePointEvent("dragStart",b)))}),x(b,["mousemove","touchmove"],function(b){Q(w(b,a),a)}),p(b,"mouseleave",function(b){B(w(b,a),a)}),a.unbindDragDropMouseUp=x(c,["mouseup","touchend"],function(b){B(w(b,a),a)}),a.hasAddedDragDropEvents=!0,
p(a,"destroy",function(){a.unbindDragDropMouseUp&&a.unbindDragDropMouseUp()}))}var n=e.objectEach,p=k.addEvent,v=k.pick,q=k.merge,h=k.seriesTypes;e=function(a){a=a.shapeArgs||a.graphic.getBBox();var b=a.r||0,c=a.height/2;return["M",0,b,"L",0,c-5,"A",1,1,0,0,0,0,c+5,"A",1,1,0,0,0,0,c-5,"M",0,c+5,"L",0,a.height-b]};var z=h.line.prototype.dragDropProps={x:{axis:"x",move:!0},y:{axis:"y",move:!0}};h.flags&&(h.flags.prototype.dragDropProps=z);var g=h.column.prototype.dragDropProps={x:{axis:"x",move:!0},
y:{axis:"y",move:!1,resize:!0,beforeResize:function(a,b,c){var d=c.series.translatedThreshold,f=a.attr("y");b.y>=c.series.options.threshold?(b=a.attr("height"),a.attr({height:Math.max(0,Math.round(b+(d?d-(f+b):0)))})):a.attr({y:Math.round(f+(d?d-f:0))})},resizeSide:function(a,b){var c=b.series.chart.dragHandles;a=a.y>=(b.series.options.threshold||0)?"top":"bottom";b=r(a);c[b]&&(c[b].destroy(),delete c[b]);return a},handlePositioner:function(a){var b=a.shapeArgs||a.graphic.getBBox();return{x:b.x,y:a.y>=
(a.series.options.threshold||0)?b.y:b.y+b.height}},handleFormatter:function(a){a=a.shapeArgs;var b=a.r||0,c=a.width/2;return["M",b,0,"L",c-5,0,"A",1,1,0,0,0,c+5,0,"A",1,1,0,0,0,c-5,0,"M",c+5,0,"L",a.width-b,0]}}};h.bullet&&(h.bullet.prototype.dragDropProps={x:g.x,y:g.y,target:{optionName:"draggableTarget",axis:"y",move:!0,resize:!0,resizeSide:"top",handlePositioner:function(a){var b=a.targetGraphic.getBBox();return{x:a.barX,y:b.y+b.height/2}},handleFormatter:g.y.handleFormatter}});h.columnrange&&
(h.columnrange.prototype.dragDropProps={x:{axis:"x",move:!0},low:{optionName:"draggableLow",axis:"y",move:!0,resize:!0,resizeSide:"bottom",handlePositioner:function(a){a=a.shapeArgs||a.graphic.getBBox();return{x:a.x,y:a.y+a.height}},handleFormatter:g.y.handleFormatter,propValidate:function(a,b){return a<=b.high}},high:{optionName:"draggableHigh",axis:"y",move:!0,resize:!0,resizeSide:"top",handlePositioner:function(a){a=a.shapeArgs||a.graphic.getBBox();return{x:a.x,y:a.y}},handleFormatter:g.y.handleFormatter,
propValidate:function(a,b){return a>=b.low}}});h.boxplot&&(h.boxplot.prototype.dragDropProps={x:g.x,low:{optionName:"draggableLow",axis:"y",move:!0,resize:!0,resizeSide:"bottom",handlePositioner:function(a){return{x:a.shapeArgs.x,y:a.lowPlot}},handleFormatter:g.y.handleFormatter,propValidate:function(a,b){return a<=b.q1}},q1:{optionName:"draggableQ1",axis:"y",move:!0,resize:!0,resizeSide:"bottom",handlePositioner:function(a){return{x:a.shapeArgs.x,y:a.q1Plot}},handleFormatter:g.y.handleFormatter,
propValidate:function(a,b){return a<=b.median&&a>=b.low}},median:{axis:"y",move:!0},q3:{optionName:"draggableQ3",axis:"y",move:!0,resize:!0,resizeSide:"top",handlePositioner:function(a){return{x:a.shapeArgs.x,y:a.q3Plot}},handleFormatter:g.y.handleFormatter,propValidate:function(a,b){return a<=b.high&&a>=b.median}},high:{optionName:"draggableHigh",axis:"y",move:!0,resize:!0,resizeSide:"top",handlePositioner:function(a){return{x:a.shapeArgs.x,y:a.highPlot}},handleFormatter:g.y.handleFormatter,propValidate:function(a,
b){return a>=b.q3}}});h.ohlc&&(h.ohlc.prototype.dragDropProps={x:g.x,low:{optionName:"draggableLow",axis:"y",move:!0,resize:!0,resizeSide:"bottom",handlePositioner:function(a){return{x:a.shapeArgs.x,y:a.plotLow}},handleFormatter:g.y.handleFormatter,propValidate:function(a,b){return a<=b.open&&a<=b.close}},high:{optionName:"draggableHigh",axis:"y",move:!0,resize:!0,resizeSide:"top",handlePositioner:function(a){return{x:a.shapeArgs.x,y:a.plotHigh}},handleFormatter:g.y.handleFormatter,propValidate:function(a,
b){return a>=b.open&&a>=b.close}},open:{optionName:"draggableOpen",axis:"y",move:!0,resize:!0,resizeSide:function(a){return a.open>=a.close?"top":"bottom"},handlePositioner:function(a){return{x:a.shapeArgs.x,y:a.plotOpen}},handleFormatter:g.y.handleFormatter,propValidate:function(a,b){return a<=b.high&&a>=b.low}},close:{optionName:"draggableClose",axis:"y",move:!0,resize:!0,resizeSide:function(a){return a.open>=a.close?"bottom":"top"},handlePositioner:function(a){return{x:a.shapeArgs.x,y:a.plotClose}},
handleFormatter:g.y.handleFormatter,propValidate:function(a,b){return a<=b.high&&a>=b.low}}});if(h.arearange){z=h.columnrange.prototype.dragDropProps;var I=function(a){a=a.graphic?a.graphic.getBBox().width/2+1:4;return["M",0-a,0,"a",a,a,0,1,0,2*a,0,"a",a,a,0,1,0,-2*a,0]};h.arearange.prototype.dragDropProps={x:z.x,low:{optionName:"draggableLow",axis:"y",move:!0,resize:!0,resizeSide:"bottom",handlePositioner:function(a){return(a=a.lowerGraphic&&a.lowerGraphic.getBBox())?{x:a.x+a.width/2,y:a.y+a.height/
2}:{x:-999,y:-999}},handleFormatter:I,propValidate:z.low.propValidate},high:{optionName:"draggableHigh",axis:"y",move:!0,resize:!0,resizeSide:"top",handlePositioner:function(a){return(a=a.upperGraphic&&a.upperGraphic.getBBox())?{x:a.x+a.width/2,y:a.y+a.height/2}:{x:-999,y:-999}},handleFormatter:I,propValidate:z.high.propValidate}}}h.waterfall&&(h.waterfall.prototype.dragDropProps={x:g.x,y:q(g.y,{handleFormatter:function(a){return a.isSum||a.isIntermediateSum?null:g.y.handleFormatter(a)}})});if(h.xrange){var J=
function(a,b){var c=a.series,d=c.xAxis,f=c.yAxis;c=c.chart.inverted;b=d.toPixels(a[b],!0);var e=f.toPixels(a.y,!0);c?(b=d.len-b,e=f.len-e-a.shapeArgs.height/2):e-=a.shapeArgs.height/2;return{x:Math.round(b),y:Math.round(e)}};e=h.xrange.prototype.dragDropProps={y:{axis:"y",move:!0},x:{optionName:"draggableX1",axis:"x",move:!0,resize:!0,resizeSide:"left",handlePositioner:function(a){return J(a,"x")},handleFormatter:e,propValidate:function(a,b){return a<=b.x2}},x2:{optionName:"draggableX2",axis:"x",
move:!0,resize:!0,resizeSide:"right",handlePositioner:function(a){return J(a,"x2")},handleFormatter:e,propValidate:function(a,b){return a>=b.x}}};h.gantt&&(h.gantt.prototype.dragDropProps={y:e.y,start:q(e.x,{optionName:"draggableStart",validateIndividualDrag:function(a){return!a.milestone}}),end:q(e.x2,{optionName:"draggableEnd",validateIndividualDrag:function(a){return!a.milestone}})})}"gauge pie sunburst wordcloud sankey histogram pareto vector windbarb treemap bellcurve sma map mapline".split(" ").forEach(function(a){h[a]&&
(h[a].prototype.dragDropProps=null)});var S={"default":{className:"highcharts-drag-box-default",lineWidth:1,lineColor:"#888",color:"rgba(0, 0, 0, 0.1)",cursor:"move",zIndex:900}},T={className:"highcharts-drag-handle",color:"#fff",lineColor:"rgba(0, 0, 0, 0.6)",lineWidth:1,zIndex:901};k.Chart.prototype.setGuideBoxState=function(a,b){var c=this.dragGuideBox;b=q(S,b);a=q(b["default"],b[a]);return c.attr({className:a.className,stroke:a.lineColor,strokeWidth:a.lineWidth,fill:a.color,cursor:a.cursor,zIndex:a.zIndex}).css({pointerEvents:"none"})};
k.Point.prototype.getDropValues=function(a,b,c){var d=this,f=d.series,e=q(f.options.dragDrop,d.options.dragDrop),h={},k=a.points[d.id],g;for(g in c)if(Object.hasOwnProperty.call(c,g)){if(void 0!==p){var p=!1;break}p=!0}n(c,function(a,c){var m=k[c],g=f[a.axis+"Axis"];g=g.toValue((g.horiz?b.chartX:b.chartY)+k[c+"Offset"]);var u=a.axis.toUpperCase(),l=f[u.toLowerCase()+"Axis"].categories?1:0;l=v(e["dragPrecision"+u],l);var n=v(e["dragMin"+u],-Infinity);u=v(e["dragMax"+u],Infinity);l&&(g=Math.round(g/
l)*l);g=Math.max(n,Math.min(u,g));p&&a.propValidate&&!a.propValidate(g,d)||void 0===m||(h[c]=g)});return h};k.Series.prototype.getGuideBox=function(a){var b=this.chart,c=Infinity,d=-Infinity,e=Infinity,m=-Infinity,h;a.forEach(function(a){(a=a.graphic&&a.graphic.getBBox()||a.shapeArgs)&&(a.width||a.height||a.x||a.y)&&(h=!0,c=Math.min(a.x,c),d=Math.max(a.x+a.width,d),e=Math.min(a.y,e),m=Math.max(a.y+a.height,m))});return h?b.renderer.rect(c,e,d-c,m-e):b.renderer.g()};k.Point.prototype.showDragHandles=
function(){var a=this,b=a.series,c=b.chart,d=c.renderer,e=q(b.options.dragDrop,a.options.dragDrop);n(b.dragDropProps,function(f,h){var g=q(T,f.handleOptions,e.dragHandle),k={className:g.className,"stroke-width":g.lineWidth,fill:g.color,stroke:g.lineColor},m=g.pathFormatter||f.handleFormatter,l=f.handlePositioner;var n=f.validateIndividualDrag?f.validateIndividualDrag(a):!0;f.resize&&n&&f.resizeSide&&m&&(e["draggable"+f.axis.toUpperCase()]||e[f.optionName])&&!1!==e[f.optionName]&&(c.dragHandles||(c.dragHandles=
{group:d.g("drag-drop-handles").add(b.markerGroup||b.group)}),c.dragHandles.point=a.id,l=l(a),k.d=n=m(a),m="function"===typeof f.resizeSide?f.resizeSide(a.options,a):f.resizeSide,!n||0>l.x||0>l.y||(k.cursor=g.cursor||"x"===f.axis!==!!c.inverted?"ew-resize":"ns-resize",(f=c.dragHandles[m])||(f=c.dragHandles[m]=d.path().add(c.dragHandles.group)),f.translate(l.x,l.y).attr(k),x(f.element,["touchstart","mousedown"],function(b){b=w(b,c);var d=a.series.chart;d.zoomOrPanKeyPressed(b)||(d.mouseIsDown=!1,D(b,
a),d.dragDropData.updateProp=b.updateProp=h,a.firePointEvent("dragStart",b),b.stopPropagation(),b.preventDefault())}),p(c.dragHandles.group.element,"mouseover",function(){c.dragDropData=c.dragDropData||{};c.dragDropData.isHoveringHandle=a.id}),x(c.dragHandles.group.element,["touchend","mouseout"],function(){var b=a.series.chart;b.dragDropData&&a.id===b.dragDropData.isHoveringHandle&&delete b.dragDropData.isHoveringHandle;b.hoverPoint||F(a)})))})};k.Chart.prototype.hideDragHandles=function(){this.dragHandles&&
(n(this.dragHandles,function(a,b){"group"!==b&&a.destroy&&a.destroy()}),this.dragHandles.group&&this.dragHandles.group.destroy&&this.dragHandles.group.destroy(),delete this.dragHandles)};p(k.Point,"mouseOver",function(){var a=this;setTimeout(function(){var b=a.series,c=b&&b.chart,d=c&&c.dragDropData;!c||d&&d.isDragging&&d.draggedPastSensitivity||c.isDragDropAnimating||!b.options.dragDrop||c.options&&c.options.chart&&c.options.chart.options3d||(c.dragHandles&&c.hideDragHandles(),a.showDragHandles())},
12)});p(k.Point,"mouseOut",function(){var a=this;setTimeout(function(){a.series&&F(a)},10)});p(k.Point,"remove",function(){var a=this.series.chart,b=a.dragHandles;b&&b.point===this.id&&a.hideDragHandles()});k.Chart.prototype.zoomOrPanKeyPressed=function(a){var b=this.userOptions.chart||{},c=b.panKey&&b.panKey+"Key";return a[b.zoomKey&&b.zoomKey+"Key"]||a[c]};p(k.Chart,"render",function(){this.hasAddedDragDropEvents||R(this)})});r(e,"masters/modules/draggable-points.src.js",[],function(){})});
//# sourceMappingURL=draggable-points.js.map