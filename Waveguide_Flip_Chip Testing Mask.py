'Author- Abhinandan Hazarika- 16/04/2023'

import nazca as nd


l = 1000
w = 5
angle1 = 2
angle2 = 5
posx= 100
posy= 100

nd.clear_layers()


nd.add_layer(name='Waveguide', layer=1)    


nd.add_layer(name='Etch ', layer=2)    
  

nd.add_layer(name='Au/Sn', layer=3)    

    

with nd.Cell ('YCombiner_12deg_5mm') as D:
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 5000, width= 5  , angle= 12, layer=1).put()
        nd.bend(radius= 5000, width= 5  , angle= -12, layer=1).put()
        nd.strt(length=5500  ,  width= 5  , layer = 1).put()
       
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 5000, width= 5  , angle= -12, layer=1).put()
        nd.bend(radius= 5000, width= 5  , angle= 12, layer=1).put()
        nd.strt(length=5500  ,  width= 5  , layer = 1).put()
       
        
        message = 'Y-Combiner 12 Deg_5mm_BendRadius_5um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)
        


with nd.Cell ('YCombiner_12deg_5mm_1') as DD:
        
        nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
        nd.bend(radius= 5000, width= 8  , angle= 12, layer=1).put()
        nd.bend(radius= 5000, width= 8  , angle= -12, layer=1).put()
        nd.strt(length=5500  ,  width= 8  , layer = 1).put()
        
        
        nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
        nd.bend(radius= 5000, width= 8  , angle= -12, layer=1).put()
        nd.bend(radius= 5000, width= 8  , angle= 12, layer=1).put()
        nd.strt(length=5500  ,  width= 8  , layer = 1).put()
        
        
        message = 'Y-Combiner 12 Deg_5mm_BendRadius_8um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)


with nd.Cell ('YCombiner_12deg_5mm_2') as DE:
        
        nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
        nd.bend(radius= 5000, width= 10  , angle= 12, layer=1).put()
        nd.bend(radius= 5000, width= 10  , angle= -12, layer=1).put()
        nd.strt(length=5500  ,  width= 10  , layer = 1).put()
       
        
        nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
        nd.bend(radius= 5000, width= 10  , angle= -12, layer=1).put()
        nd.bend(radius= 5000, width= 10  , angle= 12, layer=1).put()
        nd.strt(length=5500  ,  width= 10  , layer = 1).put()
       
        
        message = 'Y-Combiner 12 Deg_5mm_BendRadius_10um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)

with nd.Cell ('YCombiner_15deg_5mm') as E:
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 5000, width= 5  , angle= 15, layer=1).put()
        nd.bend(radius= 5000, width= 5  , angle= -15, layer=1).put()
        nd.strt(length=5000  ,  width= 5  , layer = 1).put()
       
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 5000, width= 5  , angle= -15, layer=1).put()
        nd.bend(radius= 5000, width= 5  , angle= 15, layer=1).put()
        nd.strt(length=5000  ,  width= 5  , layer = 1).put()
        
        
        message = 'Y-Combiner 15 Deg_5mm_BendRadius_5um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)

with nd.Cell ('YCombiner_15deg_5mm_1') as EE:
         
         nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
         nd.bend(radius= 5000, width= 8  , angle= 15, layer=1).put()
         nd.bend(radius= 5000, width= 8  , angle= -15, layer=1).put()
         nd.strt(length=5000  ,  width= 8  , layer = 1).put()
        
         
         nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
         nd.bend(radius= 5000, width= 8  , angle= -15, layer=1).put()
         nd.bend(radius= 5000, width= 8  , angle= 15, layer=1).put()
         nd.strt(length=5000  ,  width= 8  , layer = 1).put()
        
         
         message = 'Y-Combiner 15 Deg_5mm_BendRadius_8um Width'
         nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)

with nd.Cell ('YCombiner_15deg_5mm_2') as EF:
            
            nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
            nd.bend(radius= 5000, width= 10  , angle= 15, layer=1).put()
            nd.bend(radius= 5000, width= 10  , angle= -15, layer=1).put()
            nd.strt(length=5000  ,  width= 10  , layer = 1).put()
           
            
            nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
            nd.bend(radius= 5000, width= 10  , angle= -15, layer=1).put()
            nd.bend(radius= 5000, width= 10  , angle= 15, layer=1).put()
            nd.strt(length=5000  ,  width= 10  , layer = 1).put()
           
            
            message = 'Y-Combiner 15 Deg_5mm_BendRadius_10um Width'
            nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)  






with nd.Cell ('YCombiner_12deg_4mm') as D1:
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 4000, width= 5  , angle= 12, layer=1).put()
        nd.bend(radius= 4000, width= 5  , angle= -12, layer=1).put()
        nd.strt(length=5500  ,  width= 5  , layer = 1).put()
       
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 4000, width= 5  , angle= -12, layer=1).put()
        nd.bend(radius= 4000, width= 5  , angle= 12, layer=1).put()
        nd.strt(length=5500  ,  width= 5  , layer = 1).put()
       
        
        message = 'Y-Combiner 12 Deg_4mm_BendRadius_5um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)
        


with nd.Cell ('YCombiner_12deg_4mm_1') as DD1:
        
        nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
        nd.bend(radius= 4000, width= 8  , angle= 12, layer=1).put()
        nd.bend(radius= 4000, width= 8  , angle= -12, layer=1).put()
        nd.strt(length=5500  ,  width= 8  , layer = 1).put()
      
        
        nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
        nd.bend(radius= 4000, width= 8  , angle= -12, layer=1).put()
        nd.bend(radius= 4000, width= 8  , angle= 12, layer=1).put()
        nd.strt(length=5500  ,  width= 8  , layer = 1).put()
      
        
        message = 'Y-Combiner 12 Deg_5mm_BendRadius_8um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)


with nd.Cell ('YCombiner_12deg_4mm_2') as DE1:
        
        nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
        nd.bend(radius= 4000, width= 10  , angle= 12, layer=1).put()
        nd.bend(radius= 4000, width= 10  , angle= -12, layer=1).put()
        nd.strt(length=5500  ,  width= 10  , layer = 1).put()
       
        
        nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
        nd.bend(radius= 4000, width= 10  , angle= -12, layer=1).put()
        nd.bend(radius= 4000, width= 10  , angle= 12, layer=1).put()
        nd.strt(length=5500  ,  width= 10  , layer = 1).put()
       
        
        message = 'Y-Combiner 12 Deg_4mm_BendRadius_10um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)

with nd.Cell ('YCombiner_15deg_4mm') as E1:
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 4000, width= 5  , angle= 15, layer=1).put()
        nd.bend(radius= 4000, width= 5  , angle= -15, layer=1).put()
        nd.strt(length=5000  ,  width= 5  , layer = 1).put()
       
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 4000, width= 5  , angle= -15, layer=1).put()
        nd.bend(radius= 4000, width= 5  , angle= 15, layer=1).put()
        nd.strt(length=5000  ,  width= 5  , layer = 1).put()
       
        
        message = 'Y-Combiner 15 Deg_4mm_BendRadius_5um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)

with nd.Cell ('YCombiner_15deg_4mm_1') as EE1:
         
         nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
         nd.bend(radius= 4000, width= 8  , angle= 15, layer=1).put()
         nd.bend(radius= 4000, width= 8  , angle= -15, layer=1).put()
         nd.strt(length=5000  ,  width= 8  , layer = 1).put()
        
         
         nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
         nd.bend(radius= 4000, width= 8  , angle= -15, layer=1).put()
         nd.bend(radius= 4000, width= 8  , angle= 15, layer=1).put()
         nd.strt(length=5000  ,  width= 8  , layer = 1).put()
         
         
         message = 'Y-Combiner 15 Deg_4mm_BendRadius_8um Width'
         nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)

with nd.Cell ('YCombiner_15deg_4mm_2') as EF1:
            
            nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
            nd.bend(radius= 4000, width= 20  , angle= 15, layer=1).put()
            nd.bend(radius= 4000, width= 20  , angle= -15, layer=1).put()
            nd.strt(length=5000  ,  width= 20  , layer = 1).put()
            
            
            nd.strt(length=2000  ,  width= 20  , layer = 1).put(0)
            nd.bend(radius= 4000, width= 20  , angle= -15, layer=1).put()
            nd.bend(radius= 4000, width= 20  , angle= 15, layer=1).put()
            nd.strt(length=5000  ,  width= 20  , layer = 1).put()
            
            
            message = 'Y-Combiner 15 Deg_4mm_BendRadius_10um Width'
            nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)  



        


with nd.Cell ('YCombiner_12deg_7mm') as D2:
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 7000, width= 5  , angle= 12, layer=1).put()
        nd.bend(radius= 7000, width= 5  , angle= -12, layer=1).put()
        nd.strt(length=5500  ,  width= 5  , layer = 1).put()
        
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 7000, width= 5  , angle= -12, layer=1).put()
        nd.bend(radius= 7000, width= 5  , angle= 12, layer=1).put()
        nd.strt(length=5500  ,  width= 5  , layer = 1).put()
       
        
        message = 'Y-Combiner 12 Deg_7mm_BendRadius_5um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)
        


with nd.Cell ('YCombiner_12deg_7mm_1') as DD2:
        
        nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
        nd.bend(radius= 7000, width= 8  , angle= 12, layer=1).put()
        nd.bend(radius= 7000, width= 8  , angle= -12, layer=1).put()
        nd.strt(length=5500  ,  width= 8  , layer = 1).put()
        
        
        nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
        nd.bend(radius= 7000, width= 8  , angle= -12, layer=1).put()
        nd.bend(radius= 7000, width= 8  , angle= 12, layer=1).put()
        nd.strt(length=5500  ,  width= 8  , layer = 1).put()
        
        
        message = 'Y-Combiner 12 Deg_7mm_BendRadius_8um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)


with nd.Cell ('YCombiner_12deg_7mm_2') as DE2:
        
        nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
        nd.bend(radius= 7000, width= 10  , angle= 12, layer=1).put()
        nd.bend(radius= 7000, width= 10  , angle= -12, layer=1).put()
        nd.strt(length=5500  ,  width= 10  , layer = 1).put()
        
        
        nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
        nd.bend(radius= 7000, width= 10  , angle= -12, layer=1).put()
        nd.bend(radius= 7000, width= 10  , angle= 12, layer=1).put()
        nd.strt(length=5500  ,  width= 10  , layer = 1).put()
        
        
        message = 'Y-Combiner 12 Deg_7mm_BendRadius_10um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)

with nd.Cell ('YCombiner_15deg_7mm') as E2:
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 7000, width= 5  , angle= 15, layer=1).put()
        nd.bend(radius= 7000, width= 5  , angle= -15, layer=1).put()
        nd.strt(length=4776.80528  ,  width= 5  , layer = 1).put()
       
        
        nd.strt(length=2000  ,  width= 5  , layer = 1).put(0)
        nd.bend(radius= 7000, width= 5  , angle= -15, layer=1).put()
        nd.bend(radius= 7000, width= 5  , angle= 15, layer=1).put()
        nd.strt(length=4776.80528  ,  width= 5  , layer = 1).put()
       
        
        message = 'Y-Combiner 15 Deg_7mm_BendRadius_5um Width'
        nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)

with nd.Cell ('YCombiner_15deg_7mm_1') as EE2:
         
         nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
         nd.bend(radius= 7000, width= 8  , angle= 15, layer=1).put()
         nd.bend(radius= 7000, width= 8  , angle= -15, layer=1).put()
         nd.strt(length=4776.80528  ,  width= 8  , layer = 1).put()
         
         
         nd.strt(length=2000  ,  width= 8  , layer = 1).put(0)
         nd.bend(radius= 7000, width= 8  , angle= -15, layer=1).put()
         nd.bend(radius= 7000, width= 8  , angle= 15, layer=1).put()
         nd.strt(length=4776.80528  ,  width= 8  , layer = 1).put()
         
         
         message = 'Y-Combiner 15 Deg_7mm_BendRadius_8um Width'
         nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100)

with nd.Cell ('YCombiner_15deg_7mm_2') as EF2:
            
            nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
            nd.bend(radius= 7000, width= 10  , angle= 15, layer=1).put()
            nd.bend(radius= 7000, width= 10  , angle= -15, layer=1).put()
            nd.strt(length=4776.80528  ,  width= 10  , layer = 1).put()
           
            
            nd.strt(length=2000  ,  width= 10  , layer = 1).put(0)
            nd.bend(radius= 7000, width= 10  , angle= -15, layer=1).put()
            nd.bend(radius= 7000, width= 10  , angle= 15, layer=1).put()
            nd.strt(length=4776.80528  ,  width= 10  , layer = 1).put()
            
            
            message = 'Y-Combiner 15 Deg_7mm_BendRadius_10um Width'
            nd.text(text=message, height=50, layer=1, align='cc').put(2000, 100) 

    
            






with nd.Cell ('Cut_Back_Structure_1') as A4:
        
        nd.strt(length=600  ,  width= 5  , layer = 1).put(0)
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width= 5  , layer = 1).put()
        
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=800  , width= 5  , layer = 1).put()
        nd.strt(length=2637.723,width= 5  , layer = 1).put()
        
        


        
with nd.Cell ('Cut_Back_Structure_2') as A5:
        
        nd.strt(length=600  ,  width= 5  , layer = 1).put(0)
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=750, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=150  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=750, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=750, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=750, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=750, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=750, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=750, width= 5  , layer = 1).put()
       
       
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=720, width= 5  , layer = 1).put()
        nd.strt(length=2237.723, width= 5  , layer = 1).put()

        
with nd.Cell ('Cut_Back_Structure_3') as A6:
        
        nd.strt(length=600  ,  width= 5  , layer = 1).put(0)
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=170 ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=725, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=725, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=725, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=725, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=725, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=725, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=725, width= 5  , layer = 1).put()
       
       
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=725, width= 5  , layer = 1).put()
        nd.strt(length=2037.723, width= 5  , layer = 1).put()




with nd.Cell ('Cut_Back_Structure_4') as A7:
        
        nd.strt(length=600  ,  width= 5  , layer = 1).put(0)
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=700, width= 5  , layer = 1).put()
        
        
         
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=700, width= 5  , layer = 1).put()
        
        
         
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=700, width= 5  , layer = 1).put()
        
        
         
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=700, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=700, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=700, width= 5  , layer = 1).put()
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=700, width= 5  , layer = 1).put()
        
        
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width= 5  , layer = 1).put()
        nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
        nd.strt(length=700, width= 5  , layer = 1).put()
        nd.strt(length=1837.723, width= 5  , layer = 1).put()

        
with nd.Cell ('Cut_Back_Structure_5') as A8:
          
          nd.strt(length=600  ,  width= 5  , layer = 1).put(0)
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=675, width= 5  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=675, width= 5  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=675, width= 5  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=675, width= 5  , layer = 1).put()
          
            
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=675, width= 5  , layer = 1).put()
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=675, width= 5  , layer = 1).put() 
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=675, width= 5  , layer = 1).put() 
          
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=675, width= 5  , layer = 1).put()      
          nd.strt(length=1637.723, width= 5  , layer = 1).put()

with nd.Cell ('Cut_Back_Structure_6') as A9:
                  
          nd.strt(length=600  ,  width= 5  , layer = 1).put(0)
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=320  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=650, width= 5  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=650, width= 5  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=650, width= 5  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=650, width= 5  , layer = 1).put()
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=650, width= 5  , layer = 1).put()
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=650, width= 5  , layer = 1).put()
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=650, width= 5  , layer = 1).put()
         
          
            
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=650, width= 5  , layer = 1).put()
          nd.strt(length=1437.723, width= 5  , layer = 1).put()
                

        
with nd.Cell ('Cut_Back_Structure_7') as A10:
                  
          nd.strt(length=600  ,  width= 5  , layer = 1).put(0)
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length=370  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=625, width= 5  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=625, width= 5  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=625, width= 5  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=625, width= 5  , layer = 1).put()
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=625, width= 5  , layer = 1).put()
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=625, width= 5  , layer = 1).put()
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=625, width= 5  , layer = 1).put()
         
          
          
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width= 5  , layer = 1).put()
          nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
          nd.strt(length=625, width= 5  , layer = 1).put()
          nd.strt(length=1237.723, width= 5  , layer = 1).put()


          
          
with nd.Cell ('Cut_Back_Structure_8') as A11:
                     
             nd.strt(length=600  ,  width= 5  , layer = 1).put(0)
             
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.strt(length=420  ,  width= 5  , layer = 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.strt(length=600, width= 5  , layer = 1).put()
             
             
              
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width= 5  , layer = 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.strt(length=600, width= 5  , layer = 1).put()
             
             
              
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width= 5  , layer = 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.strt(length=600, width= 5  , layer = 1).put()
             
             
              
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width= 5  , layer = 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.strt(length=600, width= 5  , layer = 1).put()
             
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width= 5  , layer = 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.strt(length=600, width= 5  , layer = 1).put()  
             
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width= 5  , layer = 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.strt(length=600, width= 5  , layer = 1).put()  
             
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width= 5  , layer = 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.strt(length=600, width= 5  , layer = 1).put()  
               
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width= 5  , layer = 1).put()
             nd.bend(radius= 3000, width= 5  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width= 5  , angle= 10, layer= 1).put()
             nd.strt(length=600, width= 5  , layer = 1).put()      
             nd.strt(length=1037.723, width= 5  , layer = 1).put()
          
          
          
          


with nd.Cell ('Cut_Back_Structure_11') as A44:
        
        nd.strt(length=600  ,  width=10  , layer = 1).put(0)
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=823  , width=10  , layer = 1).put()
        
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=800  , width=10  , layer = 1).put()
        nd.strt(length=2637.723,width=10  , layer = 1).put()
        
        


        
with nd.Cell ('Cut_Back_Structure_22') as A55:
        
        nd.strt(length=600  ,  width=10  , layer = 1).put(0)
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=750, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=150  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=750, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=750, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=750, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=750, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=750, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=750, width=10  , layer = 1).put()
       
       
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=120  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=720, width=10  , layer = 1).put()
        nd.strt(length=2237.723, width=10  , layer = 1).put()

        
with nd.Cell ('Cut_Back_Structure_33') as A66:
        
        nd.strt(length=600  ,  width=10  , layer = 1).put(0)
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=170 ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=725, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=725, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=725, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=725, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=725, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=725, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=725, width=10  , layer = 1).put()
       
       
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=170  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=725, width=10  , layer = 1).put()
        nd.strt(length=2037.723, width=10  , layer = 1).put()




with nd.Cell ('Cut_Back_Structure_44') as A77:
        
        nd.strt(length=600  ,  width=10  , layer = 1).put(0)
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=700, width=10  , layer = 1).put()
        
        
         
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=700, width=10  , layer = 1).put()
        
        
         
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=700, width=10  , layer = 1).put()
        
        
         
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=700, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=700, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=700, width=10  , layer = 1).put()
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=700, width=10  , layer = 1).put()
        
        
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.strt(length=220  ,  width=10  , layer = 1).put()
        nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
        nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
        nd.strt(length=700, width=10  , layer = 1).put()
        nd.strt(length=1837.723, width=10  , layer = 1).put()

        
with nd.Cell ('Cut_Back_Structure_55') as A88:
          
          nd.strt(length=600  ,  width=10  , layer = 1).put(0)
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=675, width=10  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=675, width=10  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=675, width=10  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=675, width=10  , layer = 1).put()
          
            
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=675, width=10  , layer = 1).put()
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=675, width=10  , layer = 1).put() 
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=675, width=10  , layer = 1).put() 
          
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=270  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=675, width=10  , layer = 1).put()      
          nd.strt(length=1637.723, width=10  , layer = 1).put()

with nd.Cell ('Cut_Back_Structure_66') as A99:
                  
          nd.strt(length=600  ,  width=10  , layer = 1).put(0)
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=320  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=650, width=10  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=650, width=10  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=650, width=10  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=650, width=10  , layer = 1).put()
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=650, width=10  , layer = 1).put()
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=650, width=10  , layer = 1).put()
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=650, width=10  , layer = 1).put()
         
          
            
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 320  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=650, width=10  , layer = 1).put()
          nd.strt(length=1437.723, width=10  , layer = 1).put()
                

        
with nd.Cell ('Cut_Back_Structure_77') as A100:
                  
          nd.strt(length=600  ,  width=10  , layer = 1).put(0)
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length=370  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=625, width=10  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=625, width=10  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=625, width=10  , layer = 1).put()
          
          
           
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=625, width=10  , layer = 1).put()
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=625, width=10  , layer = 1).put()
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=625, width=10  , layer = 1).put()
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=625, width=10  , layer = 1).put()
         
          
          
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.strt(length= 370  ,  width=10  , layer = 1).put()
          nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
          nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
          nd.strt(length=625, width=10  , layer = 1).put()
          nd.strt(length=1237.723, width=10  , layer = 1).put()


          
          
with nd.Cell ('Cut_Back_Structure_88') as A101:
                     
             nd.strt(length=600  ,  width=10  , layer = 1).put(0)
             
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.strt(length=420  ,  width=10  , layer = 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.strt(length=600, width=10  , layer = 1).put()
             
             
              
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width=10  , layer = 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.strt(length=600, width=10  , layer = 1).put()
             
             
              
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width=10  , layer = 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.strt(length=600, width=10  , layer = 1).put()
             
             
              
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width=10  , layer = 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.strt(length=600, width=10  , layer = 1).put()
             
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width=10  , layer = 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.strt(length=600, width=10  , layer = 1).put()  
             
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width=10  , layer = 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.strt(length=600, width=10  , layer = 1).put()  
             
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width=10  , layer = 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.strt(length=600, width=10  , layer = 1).put()  
               
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.strt(length= 420  ,  width=10  , layer = 1).put()
             nd.bend(radius= 3000, width=10  , angle= -10, layer= 1).put()
             nd.bend(radius= 3000, width=10  , angle= 10, layer= 1).put()
             nd.strt(length=600, width=10  , layer = 1).put()      
             nd.strt(length=1037.723, width=10  , layer = 1).put()    

            

    
    
                         


             
             
with nd.Cell ('Bend_5mm_10deg_5umWidth') as Bc2:

           
           
           nd.strt(length=1500  ,  width= 5  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 5  , angle= 10, layer=1).put()
           nd.bend(radius= 5000, width= 5  , angle= -10, layer=1).put()
           nd.strt(length=500  ,  width= 5  , layer = 1).put()  
           nd.strt(length=5263  ,  width= 5  , layer = 1).put()
with nd.Cell ('Bend_5mm_12deg_5umWidth') as Bc3:

           
           
           nd.strt(length=1500  ,  width= 5  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 5  , angle= 12, layer=1).put()
           nd.bend(radius= 5000, width= 5  , angle= -12, layer=1).put()
           nd.strt(length=500  ,  width= 5  , layer = 1).put()
           nd.strt(length=4920  ,  width= 5  , layer = 1).put()
           
with nd.Cell ('Bend_5mm_15deg_5umWidth') as Bc4:

           
           
           nd.strt(length=1500  ,  width= 5  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 5  , angle= 15, layer=1).put()
           nd.bend(radius= 5000, width= 5  , angle= -15, layer=1).put()
           nd.strt(length=500  ,  width= 5  , layer = 1).put()
           nd.strt(length=4411  ,  width= 5  , layer = 1).put()
with nd.Cell ('Bend_5mm_18deg_5umWidth') as Bc5:

           
           
           nd.strt(length=1500  ,  width= 5  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 5  , angle= 18, layer=1).put()
           nd.bend(radius= 5000, width= 5  , angle= -18, layer=1).put()
           nd.strt(length=500  ,  width= 5  , layer = 1).put()
           nd.strt(length=3977  ,  width= 5  , layer = 1).put()
with nd.Cell ('Bend_5mm_20deg_5umWidth') as Bc6:

           
           
           nd.strt(length=1500  ,  width= 5  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 5  , angle= 20, layer=1).put()
           nd.bend(radius= 5000, width= 5  , angle= -20, layer=1).put()
           nd.strt(length=500  ,  width= 5  , layer = 1).put()
           nd.strt(length=3649  ,  width= 5  , layer = 1).put()
with nd.Cell ('Bend_5mm_25deg_5umWidth') as Bc7:

           
           
           nd.strt(length=1500  ,  width= 5  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 5  , angle= 25, layer=1).put()
           nd.bend(radius= 5000, width= 5  , angle= -25, layer=1).put()
           nd.strt(length=500  ,  width= 5  , layer = 1).put()
           nd.strt(length=2843  ,  width= 5  , layer = 1).put()
with nd.Cell ('Bend_5mm_30deg_5umWidth') as Bc8:

           
           
           nd.strt(length=1500  ,  width= 5  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 5  , angle= 30, layer=1).put()
           nd.bend(radius= 5000, width= 5  , angle= -30, layer=1).put()
           nd.strt(length=500  ,  width= 5  , layer = 1).put()           
           nd.strt(length=2060  ,  width= 5  , layer = 1).put()
with nd.Cell ('Bend_5mm_40deg_5umWidth') as Bc9:

           
           
           nd.strt(length=1500  ,  width= 5  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 5  , angle= 40, layer=1).put()
           nd.bend(radius= 5000, width= 5  , angle= -40, layer=1).put()
           nd.strt(length=500  ,  width= 5  , layer = 1).put()
           nd.strt(length=666  ,  width= 5  , layer = 1).put()
with nd.Cell ('Bend_5mm_45deg_5umWidth') as Bc11:

           
           
           nd.strt(length=1500  ,  width= 5  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 5  , angle= 45, layer=1).put()
           nd.bend(radius= 5000, width= 5  , angle= -45, layer=1).put()
           nd.strt(length=500  ,  width= 5  , layer = 1).put()
        



      
           

with nd.Cell ('Bend_5mm_10deg_8umWidth') as Bc20:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 10, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -10, layer=1).put()
           nd.strt(length=500  ,  width= 8  , layer = 1).put()  
           nd.strt(length=5263  ,  width= 8  , layer = 1).put()
with nd.Cell ('Bend_5mm_12deg_8umWidth') as Bc30:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 12, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -12, layer=1).put()
           nd.strt(length=500  ,  width= 8  , layer = 1).put()
           nd.strt(length=4920  ,  width= 8  , layer = 1).put()
           
with nd.Cell ('Bend_5mm_15deg_8umWidth') as Bc40:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 15, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -15, layer=1).put()
           nd.strt(length=500  ,  width= 8  , layer = 1).put()
           nd.strt(length=4411  ,  width= 8  , layer = 1).put()
with nd.Cell ('Bend_5mm_18deg_8umWidth') as Bc50:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 18, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -18, layer=1).put()
           nd.strt(length=500  ,  width= 8  , layer = 1).put()
           nd.strt(length=3977  ,  width= 8  , layer = 1).put()
with nd.Cell ('Bend_5mm_20deg_8umWidth') as Bc60:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 20, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -20, layer=1).put()
           nd.strt(length=500  ,  width= 8  , layer = 1).put()
           nd.strt(length=3649  ,  width= 8  , layer = 1).put()
with nd.Cell ('Bend_5mm_25deg_8umWidth') as Bc70:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 25, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -25, layer=1).put()
           nd.strt(length=500  ,  width= 8  , layer = 1).put()
           nd.strt(length=2843  ,  width= 8  , layer = 1).put()
with nd.Cell ('Bend_5mm_30deg_8umWidth') as Bc80:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 30, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -30, layer=1).put()
           nd.strt(length=500  ,  width= 8  , layer = 1).put()           
           nd.strt(length=2060  ,  width= 8  , layer = 1).put()
with nd.Cell ('Bend_5mm_40deg_8umWidth') as Bc90:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 40, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -40, layer=1).put()
           nd.strt(length=500  ,  width= 8  , layer = 1).put()
           nd.strt(length=666  ,  width= 8  , layer = 1).put()
           
with nd.Cell ('Bend_5mm_45deg_8umWidth') as Bc1000:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 45, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -45, layer=1).put()
           nd.strt(length=500  ,  width= 8  , layer = 1).put()
        





with nd.Cell ('Bend_5mm_10deg_10umWidth') as Bc200:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()  
           nd.strt(length=5263  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_5mm_12deg_10umWidth') as Bc300:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 12, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -12, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
           nd.strt(length=4920  ,  width= 10  , layer = 1).put()
           
with nd.Cell ('Bend_5mm_15deg_10umWidth') as Bc400:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
           nd.strt(length=4411  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_5mm_18deg_10umWidth') as Bc500:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 18, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -18, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
           nd.strt(length=3977  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_5mm_20deg_10umWidth') as Bc600:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
           nd.strt(length=3649  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_5mm_25deg_10umWidth') as Bc700:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 25, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -25, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
           nd.strt(length=2843  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_5mm_30deg_10umWidth') as Bc800:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 30, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -30, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()           
           nd.strt(length=2060  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_5mm_40deg_10umWidth') as Bc900:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 40, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -40, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
           nd.strt(length=666  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_5mm_45deg_10umWidth') as Bc10000:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 45, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -45, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
 


           

with nd.Cell ('Bend_.5mm_10deg_10umWidth') as Cc000:

          
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 500, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 500, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=3450  ,  width= 10  , layer = 1).put()             
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_1mm_10deg_10umWidth') as Cc100:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 1000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 1000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=3277  ,  width= 10  , layer = 1).put()             
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_2mm_10deg_10umWidth') as Cc200:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 2000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 2000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=2930  ,  width= 10  , layer = 1).put()  
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_3mm_10deg_10umWidth') as Cc300:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 3000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 3000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=2583  ,  width= 10  , layer = 1).put()
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()
           
with nd.Cell ('Bend_4mm_10deg_10umWidth') as Cc400:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 4000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 4000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=2238  ,  width= 10  , layer = 1).put()
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_5mm_10deg_10umWidth') as Cc500:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=1891  ,  width= 10  , layer = 1).put()
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_6mm_10deg_10umWidth') as Ccc600:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 6000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 6000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=1542  ,  width= 10  , layer = 1).put()
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_7mm_10deg_10umWidth') as Cc700:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 7000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 7000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=1194  ,  width= 10  , layer = 1).put()
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_8mm_10deg_10umWidth') as Cc800:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 8000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 8000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=847  ,  width= 10  , layer = 1).put()           
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_9mm_10deg_10umWidth') as Cc900:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 9000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 9000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()






with nd.Cell ('Bend_.5mm_15deg_10umWidth') as Dc000:

          
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 500, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 500, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=3450  ,  width= 10  , layer = 1).put()             
           nd.strt(length=3850  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_1mm_15deg_10umWidth') as Dc100:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 1000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 1000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=3277  ,  width= 10  , layer = 1).put()             
           nd.strt(length=3763.007  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_2mm_15deg_10umWidth') as Dc200:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 2000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 2000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=2930  ,  width= 10  , layer = 1).put()  
           nd.strt(length=3592.37  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_3mm_15deg_10umWidth') as Dc300:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 3000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 3000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=2583  ,  width= 10  , layer = 1).put()
           nd.strt(length=3421.74  ,  width= 10  , layer = 1).put()
           
with nd.Cell ('Bend_4mm_15deg_10umWidth') as Dc400:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 4000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 4000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=2238  ,  width= 10  , layer = 1).put()
           nd.strt(length=3249.093  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_5mm_15deg_10 umWidth') as Dc500:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=1891  ,  width= 10  , layer = 1).put()
           nd.strt(length=3078.46  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_6mm_15deg_10umWidth') as Dc600:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 6000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 6000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=1542  ,  width= 10  , layer = 1).put()
           nd.strt(length=2909.81534  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_7mm_15deg_10umWidth') as Dc700:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 7000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 7000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=1194  ,  width= 10  , layer = 1).put()
           nd.strt(length=2740.1773  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_8mm_15deg_10umWidth') as Dc800:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 8000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 8000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=847  ,  width= 10  , layer = 1).put()           
           nd.strt(length=2570.9436  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_9mm_15deg_10umWidth') as Dc900:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 9000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 9000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
           nd.strt(length=2401.52  ,  width= 10  , layer = 1).put()

        




with nd.Cell ('Bend_.5mm_20deg_10umWidth') as Ec000:

          
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 500, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 500, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=3450  ,  width= 10  , layer = 1).put()             
           nd.strt(length=3550  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_1mm_20deg_10umWidth') as Ec100:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 1000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 1000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=3277  ,  width= 10  , layer = 1).put()             
           nd.strt(length=3381.68788  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_2mm_20deg_10umWidth') as Ec200:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 2000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 2000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=2930  ,  width= 10  , layer = 1).put()  
           nd.strt(length=3046.37539  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_3mm_20deg_10umWidth') as Ec300:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 3000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 3000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=2583  ,  width= 10  , layer = 1).put()
           nd.strt(length=2709.33539  ,  width= 10  , layer = 1).put()
           
with nd.Cell ('Bend_4mm_20deg_10umWidth') as Ec400:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 4000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 4000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=2238  ,  width= 10  , layer = 1).put()
           nd.strt(length=2365.80128  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_5mm_20deg_10 umWidth') as Ec500:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=1891  ,  width= 10  , layer = 1).put()
           nd.strt(length=2031.6785  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_6mm_20deg_10umWidth') as Ec600:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 6000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 6000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=1542  ,  width= 10  , layer = 1).put()
           nd.strt(length= 1695.10344  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_7mm_20deg_10umWidth') as Ec700:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 7000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 7000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=1194  ,  width= 10  , layer = 1).put()
           nd.strt(length=1359.0634  ,  width= 10  , layer = 1).put()

with nd.Cell ('Bend_8mm_20deg_10umWidth') as Ec800:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 8000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 8000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=847  ,  width= 10  , layer = 1).put()           
           nd.strt(length=1020.6399  ,  width= 10  , layer = 1).put()
with nd.Cell ('Bend_9mm_20deg_10umWidth') as Ec900:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 9000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 9000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=500  ,  width= 10  , layer = 1).put()
           nd.strt(length=685.5446  ,  width= 10  , layer = 1).put()





with nd.Cell ('Waveguide Crossing_5mm_10deg_10um') as WC0:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 10, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -10, layer=1).put()
           nd.strt(length=1500  ,  width= 10  , layer = 1).put()
           nd.strt(length=5263  ,  width= 10  , layer = 1).put()

with nd.Cell ('Waveguide Crossing_5mm_15deg_10um') as WC1:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 15, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -15, layer=1).put()
           nd.strt(length=1500  ,  width= 10  , layer = 1).put()
           nd.strt(length=4416  ,  width= 10  , layer = 1).put()

with nd.Cell ('Waveguide Crossing_5mm_20deg_10um') as WC2:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 20, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -20, layer=1).put()
           nd.strt(length=1500  ,  width= 10  , layer = 1).put()
           nd.strt(length=3590  ,  width= 10  , layer = 1).put()

with nd.Cell ('Waveguide Crossing_5mm_30deg_10um') as WC3:

           
           
           nd.strt(length=1500  ,  width= 10  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 10  , angle= 30, layer=1).put()
           nd.bend(radius= 5000, width= 10  , angle= -30, layer=1).put()
           nd.strt(length=1500  ,  width= 10  , layer = 1).put()
           nd.strt(length=2000  ,  width= 10  , layer = 1).put()



with nd.Cell ('Waveguide Crossing_5mm_10deg_8um') as WCC0:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 10, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -10, layer=1).put()
           nd.strt(length=1500  ,  width= 8  , layer = 1).put()
           nd.strt(length=5263  ,  width= 8  , layer = 1).put()

with nd.Cell ('Waveguide Crossing_5mm_15deg_8um') as WCC1:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 15, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -15, layer=1).put()
           nd.strt(length=1500  ,  width= 8  , layer = 1).put()
           nd.strt(length=4416  ,  width= 8  , layer = 1).put()

with nd.Cell ('Waveguide Crossing_5mm_20deg_8um') as WCC2:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 20, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -20, layer=1).put()
           nd.strt(length=1500  ,  width= 8  , layer = 1).put()
           nd.strt(length=3590  ,  width= 8  , layer = 1).put()

with nd.Cell ('Waveguide Crossing_5mm_30deg_8um') as WCC3:

           
           
           nd.strt(length=1500  ,  width= 8  , layer = 1).put(0)
           nd.bend(radius= 5000, width= 8  , angle= 30, layer=1).put()
           nd.bend(radius= 5000, width= 8  , angle= -30, layer=1).put()
           nd.strt(length=1500  ,  width= 8  , layer = 1).put()
           nd.strt(length=2000  ,  width= 8  , layer = 1).put()


with nd.Cell ('Straight Waveguides') as Sc:

        
        
     
        with nd.Cell ('Straight WG0') as StrtWG0: 
       
       
             nd.strt(length=28000  ,  width= 5  , layer = 1).put()
             
        with nd.Cell ('Straight WG1') as StrtWG1:
             
             
             nd.strt(length=28000  ,  width= 8  , layer = 1).put()


        with nd.Cell ('Straight WG2') as StrtWG2:
              
              
             nd.strt(length=28000  ,  width= 10  , layer = 1).put()
             
        
        with nd.Cell ('Straight WG4') as StrtWG4:
              
              
             nd.strt(length=10000  ,  width= 8  , layer = 1).put()
             
        with nd.Cell ('Straight WG5') as StrtWG5:
              
              
             nd.strt(length=10000  ,  width= 10  , layer = 1).put()

        with nd.Cell ('Straight WG6') as StrtWG6:
              
              
             nd.strt(length=10000  ,  width= 5  , layer = 1).put()




with nd.Cell ('Etch Without Waveguide_1') as EWW1:
    
   
    nd.strt(length= 140  ,  width= 2500  , layer = 2).put()

    
with nd.Cell ('Etch Without Waveguide_2') as EWW2:
    
   
    nd.strt(length= 140  ,  width= 2500  , layer = 2).put()
  
with nd.Cell ('Au/Sn Pad') as AuSn:
    
    nd.strt(length= 30  ,  width= 2  , layer = 3).put(2,0)
    nd.strt(length= 30  ,  width= 2 , layer = 3).put(2,3)
    nd.strt(length= 30  ,  width= 2  , layer = 3).put(2,6)
    nd.strt(length= 30  ,  width= 2 , layer = 3).put(2,9)
    nd.strt(length= 30  ,  width= 2  , layer = 3).put(2,12)
    nd.strt(length= 1970  ,  width= 40  , layer = 3).put(32, 7)
    
      
with nd.Cell ('Boundary1') as BB1:
    
   
    nd.strt(length=27000  ,  width= 600  , layer = 1).put(0)
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=1).put()
    nd.strt(length=27000  ,  width= 600  , layer = 1).put()
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=1).put()
    nd.strt(length=27000  ,  width= 600  , layer = 1).put()
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=1).put()
    nd.strt(length=27000  ,  width= 600  , layer = 1).put()
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=1).put()

with nd.Cell ('Boundary2') as BB2:
    
   
    nd.strt(length=27000  ,  width= 600  , layer = 2).put(0)
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=2).put()
    nd.strt(length=27000  ,  width= 600  , layer = 2).put()
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=2).put()
    nd.strt(length=27000  ,  width= 600  , layer = 2).put()
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=2).put()
    nd.strt(length=27000  ,  width= 600  , layer = 2).put()
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=2).put()

with nd.Cell ('Boundary3') as BB3:
    
   
    nd.strt(length=27000  ,  width= 600  , layer = 3).put(0)
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=3).put()
    nd.strt(length=27000  ,  width= 600  , layer = 3).put()
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=3).put()
    nd.strt(length=27000  ,  width= 600  , layer = 3).put()
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=3).put()
    nd.strt(length=27000  ,  width= 600  , layer = 3).put()
    nd.bend(radius= 2000, width= 600  , angle= 90, layer=3).put()



with nd.Cell ('Cleaving Mark_1') as CB1:
    
   
    nd.strt(length=70  ,  width= 300  , layer = 1).put(0)
    nd.strt(length=70  ,  width= 300  , layer = 1).put(140,0)

with nd.Cell ('Cleaving Mark_2') as CB2:
    
   
    nd.strt(length=70  ,  width= 300  , layer = 3).put(0)
    nd.strt(length=70  ,  width= 300  , layer = 3).put(140,0) 


with nd.Cell ('Text_Waveguide Crossing') as WCtxt:

    message = 'WC_5mm_10_15_20_30Deg_5um'
    nd.text(text=message, height=50, layer=1, align='cc').put()
    
with nd.Cell ('Text_Waveguide Crossing') as WCtxt1:

    message = 'WC_5mm_10_15_20_30Deg_8um'
    nd.text(text=message, height=50, layer=1, align='cc').put()



with nd.Cell ('Text_Variable Bend_Radius_.5_1_2_3_4_5_6_7_8_9mm_10Deg') as WCtxt2:

    message = 'BendRadius_.5_1_2_3_4_5_6_7_8_9mm_10Deg_5um'
    nd.text(text=message, height=50, layer=1, align='cc').put()    

with nd.Cell ('Text_Variable Bend_Radius_.5_1_2_3_4_5_6_7_8_9mm_15Deg') as WCtxt3:

    message = 'BendRadius_.5_1_2_3_4_5_6_7_8_9mm_15Deg_8um'
    nd.text(text=message, height=50, layer=1, align='cc').put() 

with nd.Cell ('Text_Variable Bend_Radius_.5_1_2_3_4_5_6_7_8_9mm_20Deg') as WCtxt4:

    message = 'BendRadius_.5_1_2_3_4_5_6_7_8_9mm_20Deg_10um'
    nd.text(text=message, height=50, layer=1, align='cc').put() 






with nd.Cell ('Text_Variable Bend Angle 10-12-15-18_20_25-30_40_45Deg_5mm_5um') as WCtxt5:

    message = 'Bend Angle 10_12_15_18_20_25_30_40_45Deg_5mm_5um'
    nd.text(text=message, height=50, layer=1, align='cc').put()

with nd.Cell ('Text_Variable Bend Angle 10-12-15-18_20_25-30_40_45Deg_5mm_8um') as WCtxt6:

    message = 'Bend Angle 10_12_15_18_20_25_30_40_45Deg_5mm_8um'
    nd.text(text=message, height=50, layer=1, align='cc').put()

with nd.Cell ('Text_Variable Bend Angle 10-12-15-18_20_25-30_40_45Deg_5mm_10um') as WCtxt7:

    message = 'Bend Angle 10_12_15_18_20_25_30_40_45Deg_5mm_8um'
    nd.text(text=message, height=50, layer=1, align='cc').put()      




with nd.Cell ('Straight Waveguides_5_8_10um') as WCtxt8:

    message = 'Straight Waveguides_5_8_10um'
    nd.text(text=message, height=50, layer=1, align='cc').put()    


with nd.Cell ('Cut Back Structure_120_170_220_270_320_370_420um') as WCtxt9:

    message = 'Cut Back Structure_120_170_220_270_320_370_420um_5um_10um'
    nd.text(text=message, height=50, layer=1, align='cc').put()    


with nd.Cell ('Layer 1') as WCtxt10:

    message = 'SU-8 Waveguide Layer'
    nd.text(text=message, height=350, layer=1, align='cc').put()    

with nd.Cell ('Layer 2') as WCtxt11:

    message = 'Etch Layer'
    nd.text(text=message, height=350, layer=2, align='cc').put()    

 
with nd.Cell ('Layer 3') as WCtxt13:

    message = 'Au-Sn Eutectic Layer'
    nd.text(text=message, height=350, layer=3, align='cc').put()    


with nd.Cell ('Waveguide_Components') as Maincell:
    
 
  
    
    Sc.put(2000,20920)
    Sc.put(10000,20920)
    Sc.put(18000,20920)
    Sc.put(26000,20920)
   
   

    
    D.put(0,10500)
    DD.put(0,12000)
    DE.put(0,13500)

    E.put(0,15000)
    EE.put(0,16500)
    EF.put(0,18000)
    EF.put(0,6000)
    EF.put(0,7500)
    EF.put(0,9000)
    
    EF.put(13000,6000)
    EF.put(13000,7500)
    EF.put(13000,9000)

    D1.put(9000,10500)
    DD1.put(9000,12000)
    DE1.put(9000,13500)

    E1.put(9000,15000)
    EE1.put(9000,16500)
    EF1.put(9000,18000)




    D2.put(17600,10500)
    DD2.put(17600,12000)
    DE2.put(17600,13500)

    E2.put(17600,15000)
    EE2.put(17600,16500)
    EF2.put(17600,18000)
 
   
    
    A4.put(0,18580)
    A5.put(0,18690)
    A6.put(0,18780)
    A7.put(0,18870)
    A8.put(0,18960)
    A9.put(0,19050)
    A10.put(0,19140)
    A11.put(0,19230)
    
 
   
    A44.put(0,19500)
    A55.put(0,19590)
    A66.put(0,19680)
    A77.put(0,19770)
    A88.put(0,19860)
    A99.put(0,19950)
    A100.put(0,20040)
    A101.put(0,20130)
    

    
    StrtWG0.put(0,20500)
    StrtWG0.put(0,20540)
    StrtWG0.put(0,20580)
    StrtWG0.put(0,20620)
    StrtWG0.put(0,20660)
    StrtWG0.put(0,20700)
    StrtWG0.put(0,20740)
    StrtWG0.put(0,20780)
    
    StrtWG0.put(0,20820)
    StrtWG0.put(0,20860)
    StrtWG0.put(0,20900)
    StrtWG0.put(0,20940)
    StrtWG0.put(0,20980)
    StrtWG0.put(0,21020)
    StrtWG0.put(0,21060)
    StrtWG0.put(0,21100)
    
    
    StrtWG1.put(0,21200)
    StrtWG1.put(0,21240)
    StrtWG1.put(0,21280)
    StrtWG1.put(0,21320)
    StrtWG1.put(0,21360)
    StrtWG1.put(0,21400)
    StrtWG1.put(0,21440)
    StrtWG1.put(0,21480)
    
    StrtWG1.put(0,21520)
    StrtWG1.put(0,21560)
    StrtWG1.put(0,21600)
    StrtWG1.put(0,21640)
    StrtWG1.put(0,21680)
    StrtWG1.put(0,21720)
    StrtWG1.put(0,21760)
    StrtWG1.put(0,21800)
    



    StrtWG2.put(0,21900)
    StrtWG2.put(0,21940)
    StrtWG2.put(0,21980)
    StrtWG2.put(0,22020)
    StrtWG2.put(0,22060)
    StrtWG2.put(0,22100)
    StrtWG2.put(0,22140)
    StrtWG2.put(0,22180)

    StrtWG2.put(0,22220)
    StrtWG2.put(0,22260)
    StrtWG2.put(0,22300)
    StrtWG2.put(0,22340)
    StrtWG2.put(0,22380)
    StrtWG2.put(0,22420)
    StrtWG2.put(0,22460)
    StrtWG2.put(0,22500)
    
    

    Bc2.put(0,23090)
    Bc3.put(0,23140)
    Bc4.put(0,23190)
    Bc5.put(0,23240)
    Bc6.put(0,23290)
    Bc7.put(0,23340)
    Bc8.put(0,23390)
    Bc9.put(0,23440)
    Bc11.put(0,23490)
    

    Bc2.put(0,26490)
    Bc3.put(0,26540)
    Bc4.put(0,26590)
    Bc5.put(0,26640)
    Bc6.put(0,26690)
    Bc7.put(0,26740)
    Bc8.put(0,26790)
    Bc9.put(0,26840)
    Bc11.put(0,26890)


    Bc20.put(9500,23090)
    Bc30.put(9500,23140)
    Bc40.put(9500,23190)
    Bc50.put(9500,23240)
    Bc60.put(9500,23290)
    Bc70.put(9500,23340)
    Bc80.put(9500,23390)
    Bc90.put(9500,23440)
    Bc1000.put(9500,23490)
    

    Bc20.put(9500,26490)
    Bc30.put(9500,26540)
    Bc40.put(9500,26590)
    Bc50.put(9500,26640)
    Bc60.put(9500,26690)
    Bc70.put(9500,26740)
    Bc80.put(9500,26790)
    Bc90.put(9500,26840)
    Bc1000.put(9500,26890)
    

    Bc200.put(19000,23090)
    Bc300.put(19000,23140)
    Bc400.put(19000,23190)
    Bc500.put(19000,23240)
    Bc600.put(19000,23290)
    Bc700.put(19000,23340)
    Bc800.put(19000,23390)
    Bc900.put(19000,23440)
    Bc10000.put(19000,23490)
  

    Bc200.put(19000,26490)
    Bc300.put(19000,26540)
    Bc400.put(19000,26590)
    Bc500.put(19000,26640)
    Bc600.put(19000,26690)
    Bc700.put(19000,26740)
    Bc800.put(19000,26790)
    Bc900.put(19000,26840)
    Bc10000.put(19000,26890)
    
    Cc000.put(0,29900)
    Cc100.put(0,29980)
    Cc200.put(0,30060)
    Cc300.put(0,30140)
    Cc400.put(0,30220)
    Cc500.put(0,30300)
    Ccc600.put(0,30380)
    Cc700.put(0,30460)
    Cc800.put(0,30540)
    Cc900.put(0,30620)

    Dc000.put(9500,29900)
    Dc100.put(9500,30000)
    Dc200.put(9500,30100)
    Dc300.put(9500,30200)
    Dc400.put(9500,30300)
    Dc500.put(9500,30400)
    Dc600.put(9500,30500)
    Dc700.put(9500,30600)
    Dc800.put(9500,30700)
    Dc900.put(9500,30800)
    
    Ec000.put(19000,29900)
    Ec100.put(19000,30040)
    Ec200.put(19000,30180)
    Ec300.put(19000,30320)
    Ec400.put(19000,30460)
    Ec500.put(19000,30600)
    Ec600.put(19000,30740)
    Ec700.put(19000,30880)
    Ec800.put(19000,31020)
    Ec900.put(19000,31160)
    
    WC0.put(0,31650)
    StrtWG5.put(0,31725.8)
    
    WC1.put(0,31850)
    StrtWG5.put(0,32020.8)
    
    WC2.put(0,32150)
    StrtWG5.put(0,32451)
    
    WC3.put(0,32550)
    StrtWG5.put(0,33220)
    
    WCC0.put(12000,31650)
    StrtWG4.put(12000,31725.8)
    
    WCC1.put(12000,31850)
    StrtWG4.put(12000,32020.8)
    
    WCC2.put(12000,32150)
    StrtWG4.put(12000,32451)
    
    WCC3.put(12000,32550)
    StrtWG4.put(12000,33220)
    
   
       
    BB1.put(500,4284)
    BB2.put(500,4284)
    BB3.put(500,4284)
   
    
    EWW1.put(10838.19,6269.742,90)
    EWW1.put(10839.19,7770.742,90)
    EWW1.put(10840.19,9270.742,90)
    
    EWW2.put(10838.19,5589.742,90)
    EWW2.put(10839.19,7090.742,90)
    EWW2.put(10840.19,8589.742,90)
    
    EWW1.put(23830.19,6269.742,90)
    EWW1.put(23832.19,7770.742,90)
    EWW1.put(23834.19,9270.742,90)
    
    EWW2.put(23830.19,5589.742,90)
    EWW2.put(23832.19,7090.742,90)
    EWW2.put(23834.19,8589.742,90)
    
    AuSn.put(9593.19,6334.701206)
    AuSn.put(9593.19,5653.23945725)
    
    AuSn.put(22585.19,6334.701206)
    AuSn.put(22585.19,5653.23945725)
    
    AuSn.put(9593.19,9334.701206)
    AuSn.put(9593.19,8653.23945725)
    
    AuSn.put(22585.19,9334.701206)
    AuSn.put(22585.19,8653.23945725)
   
    AuSn.put(9593.19,7834.701206)
    AuSn.put(9593.19,7153.23945725)
   
    AuSn.put(22585.19,7834.701206)
    AuSn.put(22585.19,7153.23945725)
   
    CB1.put(1500,5200)
    CB2.put(1500,5200)
    
    
    CB1.put(3500,5200)
    CB2.put(3500,5200)
    
    CB1.put(5500,5200)
    CB2.put(5500,5200)
    
    CB1.put(7500,5200)
    CB2.put(7500,5200)
    
    CB1.put(9500,5200)
    CB2.put(9500,5200)
    
    CB1.put(11500,5200)
    CB2.put(11500,5200)
    
    CB1.put(13500,5200)
    CB2.put(13500,5200)
    
    CB1.put(15500,5200)
    CB2.put(15500,5200)
    
    CB1.put(17500,5200)
    CB2.put(17500,5200)
    
    CB1.put(19500,5200)
    CB2.put(19500,5200)
    
    CB1.put(21500,5200)
    CB2.put(21500,5200)
    
    CB1.put(23500,5200)
    CB2.put(23500,5200)
    
    CB1.put(25500,5200)
    CB2.put(25500,5200)
    
    CB1.put(27500,5200)
    CB2.put(27500,5200)
    
    
    
    CB1.put(1500,34200)
    CB2.put(1500,34200)
    
    
    CB1.put(3500,34200)
    CB2.put(3500,34200)
    
    CB1.put(5500,34200)
    CB2.put(5500,34200)
    
    CB1.put(7500,34200)
    CB2.put(7500,34200)
    
    CB1.put(9500,34200)
    CB2.put(9500,34200)
    
    CB1.put(11500,34200)
    CB2.put(11500,34200)
    
    CB1.put(13500,34200)
    CB2.put(13500,34200)
    
    CB1.put(15500,34200)
    CB2.put(15500,34200)
    
    CB1.put(17500,34200)
    CB2.put(17500,34200)
    
    CB1.put(19500,34200)
    CB2.put(19500,34200)
    
    CB1.put(21500,34200)
    CB2.put(21500,34200)
    
    CB1.put(23500,34200)
    CB2.put(23500,34200)
    
    CB1.put(25500,34200)
    CB2.put(25500,34200)
    
    CB1.put(27500,34200)
    CB2.put(27500,34200)
    
    
    
    
    CB1.put(0,6600,90)
    CB2.put(0,6600,90)
    
    CB1.put(0,8100, 90)
    CB2.put(0,8100, 90)
    
    CB1.put(0,9600, 90)
    CB2.put(0,9600, 90)
    
    
    
    CB1.put(13000,6600,90)
    CB2.put(13000,6600,90)
    
    CB1.put(13000,8100, 90)
    CB2.put(13000,8100, 90)
    
    CB1.put(13000,9600, 90)
    CB2.put(13000,9600, 90)
    
    
    CB1.put(28000,6600,90)
    CB2.put(28000,6600,90)
    
    CB1.put(28000,8100, 90)
    CB2.put(28000,8100, 90)
    
    CB1.put(28000,9600, 90)
    CB2.put(28000,9600, 90)
    
    
    
    CB1.put(1500,14200)
    CB2.put(1500,14200)
    
    
    CB1.put(3500,14200)
    CB2.put(3500,14200)
    
    CB1.put(5500,14200)
    CB2.put(5500,14200)
    
    CB1.put(7500,14200)
    CB2.put(7500,14200)
    
    CB1.put(9500,14200)
    CB2.put(9500,14200)
    
    CB1.put(11500,14200)
    CB2.put(11500,14200)
    
    CB1.put(13500,14200)
    CB2.put(13500,14200)
    
    CB1.put(15500,14200)
    CB2.put(15500,14200)
    
    CB1.put(17500,14200)
    CB2.put(17500,14200)
    
    CB1.put(19500,14200)
    CB2.put(19500,14200)
    
    CB1.put(21500,14200)
    CB2.put(21500,14200)
    
    CB1.put(23500,14200)
    CB2.put(23500,14200)
    
    CB1.put(25500,14200)
    CB2.put(25500,14200)
    
    CB1.put(27500,14200)
    CB2.put(27500,14200)
    
    
    CB1.put(1500,22800)
    CB2.put(1000,22800)
    
    CB1.put(3500,22800)
    CB2.put(3500,22800)
    
    CB1.put(5500,22800)
    CB2.put(5500,22800)
    
    CB1.put(7500,22800)
    CB2.put(7500,22800)
    
    CB1.put(9500,22800)
    CB2.put(9500,22800)
    
    CB1.put(11500,22800)
    CB2.put(11500,22800)
    
    CB1.put(13500,22800)
    CB2.put(13500,22800)
    
    CB1.put(15500,22800)
    CB2.put(15500,22800)
    
    CB1.put(17500,22800)
    CB2.put(17500,22800)
    
    CB1.put(19500,22800)
    CB2.put(19500,22800)
    
    CB1.put(21500,22800)
    CB2.put(21500,22800)
    
    CB1.put(23500,22800)
    CB2.put(23500,22800)
    
    CB1.put(25500,22800)
    CB2.put(25500,22800)
    
    CB1.put(27500,22800)
    CB2.put(27500,22800)
    
    WCtxt.put(2000,33750)
    WCtxt1.put(14000,33750)
    
    WCtxt2.put(2000,31100)
    WCtxt3.put(12000,31100)
    WCtxt4.put(21000,31500)
    
    WCtxt5.put(2500,25100)
    WCtxt6.put(12500,25100)
    WCtxt7.put(21500,25100)
    
    WCtxt5.put(2500,28100)
    WCtxt6.put(12500,28100)
    WCtxt7.put(21500,28100)
    
    WCtxt8.put(2300,22600)
  
    WCtxt8.put(4300,22600)
  
    WCtxt8.put(6300,22600)
   
    WCtxt8.put(8300,22600)
    
    WCtxt8.put(10300,22600)
    
    WCtxt8.put(12300,22600)
    
    WCtxt8.put(14300,22600)
    
    WCtxt8.put(16300,22600)
    
    WCtxt8.put(18300,22600)
    
    WCtxt8.put(20300,22600)
    
    WCtxt8.put(22300,22600)
    
    WCtxt8.put(26300,22600)
    
    WCtxt8.put(26300,22600)
    
    
    
    
    WCtxt9.put(2300,20300)
  
    WCtxt9.put(4300,20300)
  
    WCtxt9.put(6300,20300)
   
    WCtxt9.put(8300,20300)
    
    WCtxt9.put(10300,20300)
    
    WCtxt9.put(12300,20300)
    
    WCtxt9.put(14300,20300)
    
    WCtxt9.put(16300,20300)
    
    WCtxt9.put(18300,20300)
    
    WCtxt9.put(20300,20300)
    
    WCtxt9.put(22300,20300)
    
    WCtxt9.put(24300,20300)
    
    WCtxt10.put(25000,33700)
    WCtxt11.put(25000,33300)
    WCtxt13.put(25000,32900)
   
nd.export_gds(Maincell)