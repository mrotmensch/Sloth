import graph_tool.all as gt
import math
import numpy as np
import sys
sys.path.append('../misc')
import utils


threshold = '5e-5'

# nested block model
state = utils.pickleLoad('graph14_pagerank_purge_%s_nested.pk1' % threshold)

# underlying graph
g = state.g

t = gt.get_hierarchy_tree(state)[0]


tpos = pos = gt.radial_tree_layout(t, t.vertex(t.num_vertices() - 1), weighted=True)

pos = g.own_property(tpos)
text_rot = g.new_vertex_property('double')
g.vertex_properties['text_rot'] = text_rot
cts = gt.get_hierarchy_control_points(g, t, tpos)



for v in g.vertices():
    if pos[v][0] > 0:
        text_rot[v] = math.atan(pos[v][1]/pos[v][0])
    else:
        text_rot[v] = math.pi + math.atan(pos[v][1]/pos[v][0])


gt.draw_hierarchy(state,
                    pos = pos,
                    vertex_text = g.vertex_properties['label'], 
                    edge_control_points=cts,
                    vertex_font_size = 14,
                    vertex_text_position = 1, 
                    vertex_text_rotation=g.vertex_properties['text_rot'],
                    output_size = (3000,3000),
                    output = 'nested_%s.png' % threshold,
                    bg_color=[1,1,1,1])
                    
gt.draw_hierarchy(state,
                    pos = pos,
                    edge_control_points=cts,
                    vertex_font_size = 14,
                    vertex_text_position = 1, 
                    vertex_text_rotation=g.vertex_properties['text_rot'],
                    output_size = (1000,1000),
                    output = 'nested_%s_nolabels.png' % threshold)
                    
'''
gt.graph_draw(g,pos = pos,
                    vertex_color = state.levels[0].b,                  
                    vertex_text = g.vertex_properties['label'],    
                    vertex_size = 10, 
                    vertex_anchor = 0,
                    edge_control_points=cts,
                    vertex_font_size = 9,
                    vertex_text_position = 2, 
                    vertex_text_rotation=g.vertex_properties['text_rot'],
                    output_size = (1000,1000),
                    output = 'nested_5e-5.png',
                    bg_color=[0,0,0,1])
'''


