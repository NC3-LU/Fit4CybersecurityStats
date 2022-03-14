var colors = ['rgba(230, 25, 75, 0.4)', 'rgba(60, 180, 75, 0.4)',
        'rgba(255, 225, 25, 0.4)', 'rgba(0, 130, 200, 0.4)', 'rgba(245, 130, 48, 0.4)',
        'rgba(145, 30, 180, 0.4)', 'rgba(70, 240, 240, 0.4)', 'rgba(240, 50, 230, 0.4)',
        'rgba(210, 245, 60, 0.4)', 'rgba(250, 190, 190, 0.4)', 'rgba(0, 128, 128, 0.4)',
        'rgb(148, 163, 209, 0.4)', 'rgba(170, 110, 40, 0.4)', 'rgb(141, 140, 255, 0.4)',
        'rgba(128, 0, 0, 0.4)', 'rgba(170, 255, 195, 0.4)', 'rgba(128, 128, 0, 0.4)',
        'rgba(255, 215, 180, 0.4)', 'rgba(0, 0, 128, 0.4)', 'rgb(241, 147, 241, 0.4)',
        'rgba(255, 255, 255, 0.4)', 'rgb(129, 181, 255, 0.4)', 'rgb(229, 236, 202, 0.4)',
        'rgb(157, 196, 241, 0.4)', 'rgb(253, 141, 211, 0.4)', 'rgb(180, 128, 253, 0.4)',
        'rgb(255, 195, 129, 0.4)', 'rgb(204, 228, 230, 0.4)'];

var categoryChart = {
  canvas: undefined,
  data: [],
};

function wrapLabel(label, maxwidth = 15){
  let sections = [];
  let words = label.split(" ");
  let temp = "";

  words.forEach(function(item, index){
    if(temp.length > 0)
    {
      var concat = temp + ' ' + item;

      if(concat.length > maxwidth){
        sections.push(temp);
        temp = "";
      }
      else{
        if(index == (words.length-1))
        {
          sections.push(concat);
          return;
        }
        else{
          temp = concat;
          return;
        }
      }
    }

    if(index == (words.length-1))
    {
      sections.push(item);
      return;
    }

    if(item.length < maxwidth) {
      temp = item;
    }
    else {
      sections.push(item);
    }
  });

  return sections;
}

function radarChart(labels,data_sets,ctx){
  let wrapedLabels = [];
  labels.forEach( label => {wrapedLabels.push(wrapLabel(label))});
  return new Chart(ctx, {
    type: 'radar',
    data: {
      labels: wrapedLabels,
      datasets: data_sets
    },
    options: {
      scale: {
        min: 0,
        max: 100,
      },
      elements: {
        line: {
          borderWidth: 3
        }
      },
      plugins: {
        legend: {
          position: 'bottom',
          display: true
        },
      },
    }
  });
}
