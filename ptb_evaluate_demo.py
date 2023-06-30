import os
import cv2


names = ['bag1', 'basketball1', 'basketball2', 'basketball2.2', 'basketballnew', 
         'bdog_occ2', 'bear_back', 'bear_change', 'bird1.1_no', 'bird3.1_no', 
         'book_move1', 'book_turn', 'book_turn2', 'box_no_occ', 'br_occ1', 'br_occ_0', 
         'br_occ_turn0', 'cafe_occ1', 'cc_occ1', 'cf_difficult', 'cf_no_occ', 'cf_occ2', 
         'cf_occ3', 'child_no2', 'computerbar1', 'computerBar2', 'cup_book', 'dog_no_1', 
         'dog_occ_2', 'dog_occ_3', 'express1_occ', 'express2_occ', 'express3_static_occ', 
         'face_move1', 'face_occ2', 'face_occ3', 'face_turn2', 'flower_red_occ', 
         'gre_book', 'hand_no_occ', 'hand_occ', 'library2.1_occ', 'library2.2_occ', 
         'mouse_no1', 'new_ex_no_occ', 'new_ex_occ1', 'new_ex_occ2', 'new_ex_occ3', 
         'new_ex_occ5_long', 'new_ex_occ6', 'new_ex_occ7.1', 'new_student_center1', 
         'new_student_center2', 'new_student_center3', 'new_student_center4', 
         'new_student_center_no_occ', 'new_ye_no_occ', 'new_ye_occ', 'one_book_move', 
         'rose1.2', 'static_sign1', 'studentcenter2.1', 'studentcenter3.1', 
         'studentcenter3.2', 'three_people', 'toy_car_no', 'toy_car_occ', 'toy_green_occ', 
         'toy_mo_occ', 'toy_no', 'toy_no_occ', 'toy_wg_no_occ', 'toy_wg_occ', 'toy_wg_occ1', 
         'toy_yellow_no', 'tracking4', 'tracking7.1', 'two_book', 'two_dog_occ1', 
         'two_people_1.1', 'two_people_1.2', 'two_people_1.3', 'walking_no_occ', 
         'walking_occ1', 'walking_occ_long', 'wdog_no1', 'wdog_occ3', 'wr_no', 'wr_no1', 
         'wr_occ2', 'wuguiTwo_no', 'zballpat_no1', 'zball_no1', 'zball_no2', 'zball_no3']

root = './subset'
for name in names:
    
    boxes_result = []
    for i in range(1, 5000):
        image_rgb_dir = os.path.join(root, name, 'rgb', str(i).zfill(3) + '.png')
        image_depth_dir = os.path.join(root, name, 'depth', str(i).zfill(3) + '.png')
        if not os.path.exists(image_rgb_dir):
            break
        
        img_rgb = cv2.imread(image_rgb_dir)
        img_depth = cv2.imread(image_depth_dir)
        
        #####################
        # Use your algrothm test data above, and get boxes_estimated: [x1, y1, x2, y2]
        box_estimated = []
        boxes_result.append(box_estimated)
        #####################

    for box in boxes_result:
        result_dir = os.path.join('./result', name + '.txt')
        with open(result_dir, 'w') as f:
            f.write(str(box[0]) + ',' +
                    str(box[1]) + ',' +
                    str(box[2]) + ',' +
                    str(box[3]))
            f.write('\n')
