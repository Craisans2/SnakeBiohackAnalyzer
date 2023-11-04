import cv2 as cv
import numpy as np
import tensorflow as tf
from object_detection.utils import config_util
from object_detection.builders import model_builder
from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import label_map_util

#hello world
#imports
#Function to seperate the video into images
def imageParser(video_file):
    vidMedCap = cv2.VideoCapture(video_file)
    frameNum = 0
    frames = [] 
    while(True):
        #process the frames
        
        success,frame = vidMedCap.read()
        if success:
            cv2.imwrite(frames,frame)
        else:
            break
        
        frameNum=frameNum+1
vidMedCap.release()

#

#Presurgery Risk factors that increase infection risk
highrisk = False
hasDiabetes = True
hasInfectionHistory = False
hasObesity = False
hasSmokes = False
if hasDiabetes or hasInfectionHistory or hasObesity or hasDiabetes or hasSmokes:
    highrisk = True
    
#Butz Code

def scanIm():
    # Path to the pre-trained model checkpoint
    model_dir = 'path/to/model/directory'

    # Path to the label map
    label_map_path = 'path/to/label_map.pbtxt'

    # Path to the image you want to analyze
    image_path = 'path/to/your/image.jpg'

    # Load the model checkpoint and label map
    configs = config_util.get_configs_from_pipeline_file(model_dir + '/pipeline.config')
    model_config = configs['model']
    detection_model = model_builder.build(model_config=model_config, is_training=False)

    ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
    ckpt.restore(model_dir + '/checkpoint' + '/ckpt-0').expect_partial()

    @tf.function
    def detect_fn(image):
        image, shapes = detection_model.preprocess(image)
        prediction_dict = detection_model.predict(image, shapes)
        detections = detection_model.postprocess(prediction_dict, shapes)
        return detections

    category_index = label_map_util.create_category_index_from_labelmap(label_map_path)

    # Load the image
    image_np = np.array(tf.image.decode_image(tf.io.read_file(image_path)))

    # Perform object detection
    input_tensor = tf.convert_to_tensor(image_np)
    detections = detect_fn(input_tensor)

    # Visualization of detected objects
    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np,
        detections['detection_boxes'][0].numpy(),
        detections['detection_classes'][0].numpy().astype(np.int32),
        detections['detection_scores'][0].numpy(),
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=0.30,
    )

    # Display or save the image with bounding boxes
    import cv2
    cv2.imshow('Scalpel Detection', image_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
