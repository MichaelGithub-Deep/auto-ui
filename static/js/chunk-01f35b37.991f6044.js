(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-01f35b37"],{"04d0":function(e,t,i){"use strict";i.r(t);var a=function(){var e=this,t=e.$createElement;e._self._c;return e._m(0)},s=[function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("div",{staticClass:"app-container",staticStyle:{padding:"15px"}},[i("div",{staticClass:"sys_div",attrs:{id:"main"}},[e._v(" 来不及开发了 ")])])}],n={name:"hello",data:function(){return{msg:"Welcome to Your Vue.js App",studyTime:{before:2,course:3,simulation:5,after:6}}},mounted:function(){this.drawLine()},methods:{drawLine:function(){var e=this.$echarts.init(document.getElementById("main"));e.setOption({title:{text:"用例状态",subtext:"状态",left:"center"},tooltip:{trigger:"item"},legend:{orient:"vertical",left:"left"},series:[{name:"访问来源",type:"pie",radius:"50%",data:[{value:this.studyTime.before,name:"失败"},{value:this.studyTime.course,name:"故障"},{value:this.studyTime.simulation,name:"通过"},{value:this.studyTime.after,name:" 跳过"},{value:this.studyTime.after,name:" 未知"}],emphasis:{itemStyle:{shadowBlur:10,shadowOffsetX:0,shadowColor:"rgba(0, 0, 0, 0.5)"}}}]})}}},u=n,r=(i("0ed2"),i("2877")),o=Object(r["a"])(u,a,s,!1,null,"dc1a85da",null);t["default"]=o.exports},"0ed2":function(e,t,i){"use strict";i("7426")},7426:function(e,t,i){}}]);