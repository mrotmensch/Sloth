 
var width = 1000,
    height = 700,
    root;
 
var force = d3.layout.force()
    .linkDistance(50)
    .charge(-500)
    .gravity(.05)
    .size([width, height])
    .on("tick", tick);
 
var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);
 
var link = svg.selectAll(".link"),
    node = svg.selectAll(".node");

d3.json("data", function(error, json) {
  root = json;
  update();
  bindNameClick();
});


//======== Start: Bind jQuery to click event ========

//function bindNameClick() {$('svg g.node').bind('dblclick', function() {var name = $(this).context.__data__.name; console.log(name);})};

function bindNameClick() {$('svg g.node').bind('dblclick', function() {var name = $(this).context.__data__.name; $.getJSON('/_trapClick',{target: name}, 
function(data) {$("#result").text(data.result);}
)
})};

//======== End: Bind jQuery to click event ========


function update() {

  var nodes = flatten(root),
      links = d3.layout.tree().links(nodes);
 
  // Restart the force layout.
  force
      .nodes(nodes)
      .links(links)
      .start();
 
  // Update links.
  link = link.data(links, function(d) { return d.target.id; });
 
  link.exit().remove();
 
  link.enter().insert("line", ".node")
      .attr("class", "link");
 
  // Update nodes.
  node = node.data(nodes, function(d) { return d.id; });
 
  node.exit().remove();
 
  var nodeEnter = node.enter().append("g")
      .attr("class", "node")
      //.on("click", click)
      //.on("click", getName)
      .call(force.drag);
 
  nodeEnter.append("circle")
//      .attr("r", function(d) { return Math.sqrt(d.size) / 1 || 5; });
      .attr("r", function(d) {return 25;});
 
  nodeEnter.append("text")
      .attr("dy", ".35em")
      .text(function(d) { return d.name; });
 
  node.select("circle")
      .style("fill", color);
}
 
function tick() {
  link.attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });
 
  node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
}
 

function color(d,c1,c2) {

  return d.children ? "#2ca02c" // collapsed package
      : "#c7e9c0";
}

 
// Toggle children on click.
function click(d) {
  if (d3.event.defaultPrevented) return; // ignore drag
  if (d.children) {
    d._children = d.children;
    d.children = null;
  } else {
    d.children = d._children;
    d._children = null;
  }
  update();
}
 
// Returns a list of all nodes under the root.
function flatten(root) {
  var nodes = [], i = 0;
 
  function recurse(node) {
    if (node.children) node.children.forEach(recurse);
    if (!node.id) node.id = ++i;
    nodes.push(node);
  }
 
  recurse(root);
  return nodes;
}
 
