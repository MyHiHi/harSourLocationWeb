function draw_c_s_resp_graph(x1,y1,x2,y2){
  //graph=$("#c_s_resp_graph");
//  graph.css({"width":$("#line-chart").width()+"px","height":$("#line-chart").height()+"px"});
  var myChart = echarts.init(document.getElementById('c_s_resp_graph'));
// console.log("********:",$("#c_s_resp_graph").width())
  option = {
  visualMap: [{
      show: false,
      type: 'continuous',
      seriesIndex: 0,
      min: 0,
      max: 400
  }, {
      show: false,
      type: 'continuous',
      seriesIndex: 1,
      dimension: 0,
      min: 0,
      max: x1.length - 1
  }],


  title: [{
      left: 'center',
      text: '用户侧谐波责任图'
  }, {
      top: '55%',
      left: 'center',
      text: '系统侧谐波责任图'
  }],
  tooltip: {
      trigger: 'axis'
  },
  xAxis: [{
      data: x1
  }, {
      data: x2,
      gridIndex: 1
  }],
  yAxis: [{
      splitLine: {show: false}
  }, {
      splitLine: {show: false},
      gridIndex: 1
  }],
  grid: [{
      bottom: '60%'
  }, {
      top: '60%'
  }],
  series: [{
      type: 'line',
      showSymbol: false,
      data: y1
  }, {
      type: 'line',
      showSymbol: false,
      data: y2,
      xAxisIndex: 1,
      yAxisIndex: 1
  }]
};
  myChart.setOption(option);

}



function draw_ordered_graph(x1, y1) {
  var myChart = echarts.init(document.getElementById('ordered_graph'));
  option = {
    xAxis: {
      type: 'category',
      data: x1
    },
    tooltip: {
      trigger: 'axis'
    },
    yAxis: {
      type: 'value'
    },
    series: [{
      data: y1,
      type: 'line'
    }]
  };
  myChart.setOption(option);
}