import os
from IPython.display import Image

def visual(workflow):
    # Check if images folder exists, if not create it
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # Get the PNG data from the workflow
    png_data = workflow.get_graph().draw_mermaid_png()
    
    # Save the image
    with open('images/workflow.png', 'wb') as f:
        f.write(png_data)
    
    print("Workflow visualization saved to images/workflow.png")