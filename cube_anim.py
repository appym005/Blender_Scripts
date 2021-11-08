import bpy

def animate(x,c,dz_):
    c = c + anim_speed_1*(c-1)
    frame = c
    bpy.data.collections['Cubes'].objects[xx].keyframe_insert('location', frame=frame)
    bpy.data.collections['Cubes'].objects[xx].keyframe_insert('scale', frame=frame)
    bpy.data.collections['Cubes'].objects[xx].scale[2] += dz_ 
    bpy.data.collections['Cubes'].objects[xx].location[2] += dz_
    
    frame = c+anim_speed_2
    bpy.data.collections['Cubes'].objects[xx].keyframe_insert('location', frame=frame)
    bpy.data.collections['Cubes'].objects[xx].keyframe_insert('scale', frame=frame)
    bpy.data.collections['Cubes'].objects[xx].scale[2] -= dz_ 
    bpy.data.collections['Cubes'].objects[xx].location[2] -= dz_
    
    frame = c+anim_speed_2*2
    bpy.data.collections['Cubes'].objects[xx].keyframe_insert('location', frame=frame)
    bpy.data.collections['Cubes'].objects[xx].keyframe_insert('scale', frame=frame)

#setup
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

#grid size and distancing btwn objects
N = 10
spacing = 2

#change rate
dz = 1

#placing cubes
for x in range(N):
    for  y in range(N):
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(x*spacing, y*spacing, 0), scale=(1, 1, 1))

#animation speed
anim_speed_1 = 2
anim_speed_2 = 10

for c in range(1,N+1):        
    for i in range(0,c):
        if i < c - 1:
            j = c - 1
            xx = i * N + j
            animate(bpy.data.collections['Cubes'].objects[xx],c,dz/((c-1)/(i+.5)) if c > 1 else dz)
        else:
            for j in range(0,c):
                xx = i * N + j
                animate(bpy.data.collections['Cubes'].objects[xx],c,dz/((c-1)/(j+.5)) if c > 1 else dz)    
    
                    
                
    